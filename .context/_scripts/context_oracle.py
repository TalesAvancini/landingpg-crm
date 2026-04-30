#!/usr/bin/env python3
"""
🔍 context_oracle.py — Oráculo de consulta local (H.O.K v2.5 Optimized)
Busca determinística na camada WIKI/Compliance com retorno integral de arquivos.
"""
import re, sys, json, os, unicodedata, warnings
from pathlib import Path
from collections import Counter

# 🎯 Siglas de 2 caracteres preservadas pelo filtro léxico
DOMAIN_ACRONYMS = {'qa', 'ci', 'pr', 'ux', 'db', 'ai', 'io', 'os'}

# 🧠 Stemming estrito para termos do domínio (Evita regressões do nltk)
STEM_WHITELIST = {
    'testar': 'teste', 'testes': 'teste', 'testando': 'teste',
    'arquiteturas': 'arquitetura',
    'configurar': 'configuracao', 'configurando': 'configuracao', 'configuracoes': 'configuracao',
    'integrar': 'integracao', 'integracoes': 'integracao',
    'automatizar': 'automacao', 'automacoes': 'automacao',
    'governancas': 'governanca'
}

CONTEXT_DIR = Path(__file__).resolve().parents[1]

# Import utilitário de log
sys.path.append(str(CONTEXT_DIR / "_scripts"))
try:
    from _wiki_log_utils import append_to_wiki_log
except ImportError:
    def append_to_wiki_log(*args): pass

def normalize_text(text):
    """Remove acentos, markdown e normaliza para lowercase."""
    if not text: return ""
    # 1. Remove Markdown básico
    text = re.sub(r'\*\*|`|#|\[\[|\]\]', '', text)
    # 2. Normaliza Acentos (NFD extrai os acentos dos caracteres)
    text = "".join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    return text.lower().strip()

def simple_stem(word):
    """Reduz palavras a sua raiz com base em uma whitelist rigorosa."""
    return STEM_WHITELIST.get(word, word)

def load_index_file():
    """Lê o índice mestre WIKI para roteamento determinístico."""
    index_file = CONTEXT_DIR / "market" / "WIKI" / "_index.md"
    mapping = {}
    if index_file.exists():
        content = index_file.read_text(encoding="utf-8")
        # Encontra padrões como: - [[link]] | tags: t1, t2
        matches = re.finditer(r'- \[\[(.+?)\]\]\s*\|\s*tags:\s*(.+)', content)
        for m in matches:
            path_stub = m.group(1).strip()
            tags = [normalize_text(t) for t in m.group(2).split(",")]
            # Procura o arquivo real dentro de WIKI (suporta subdiretórios como concepts/)
            wiki_dir = CONTEXT_DIR / "market" / "WIKI"
            found = list(wiki_dir.rglob(f"{path_stub}.md"))
            if not found:
                continue
            
            full_path = found[0].relative_to(CONTEXT_DIR).as_posix()
            for tag in tags:
                # Peso 10.0 para tags explícitas no índice
                mapping.setdefault(tag, []).append({"path": full_path, "weight": 10.0})
    return mapping

def build_index():
    index = {}
    search_paths = [
        CONTEXT_DIR / "market" / "WIKI",
        CONTEXT_DIR / "market" / "compliance"
    ]
    
    for search_dir in search_paths:
        if not search_dir.exists(): continue
        # rglob para varredura recursiva
        for p in search_dir.rglob("*.md"):
            try:
                rel = p.relative_to(CONTEXT_DIR).as_posix()
                text = p.read_text(encoding="utf-8")
                # Normalização integral do conteúdo para indexação
                clean_text = normalize_text(text)
                
                # Heurística de Matching 1: Palavras-chave no corpo (Min 3 chars OU Sigla do domínio)
                all_words = re.findall(r'\b\w{2,}\b', clean_text)
                words = {simple_stem(w) for w in all_words if len(w) >= 3 or w in DOMAIN_ACRONYMS}
                for w in words:
                    index.setdefault(w, []).append({"path": rel, "weight": 0.2})
                
                # Heurística de Matching 2: Nome do arquivo (stem)
                stem = normalize_text(p.stem)
                index.setdefault(stem, []).append({"path": rel, "weight": 0.5})
                
                # Heurística de Matching 3: Título / Keywords no Título
                title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
                if title_match:
                    title = normalize_text(title_match.group(1))
                    # Match exato do título (0.8)
                    index.setdefault(title, []).append({"path": rel, "weight": 0.8})
                    # Keywords dentro do título (0.6 por palavra do título)
                    all_title_words = re.findall(r'\b\w{2,}\b', title)
                    title_words = {simple_stem(w) for w in all_title_words if len(w) >= 3 or w in DOMAIN_ACRONYMS}
                    for w in title_words:
                        index.setdefault(w, []).append({"path": rel, "weight": 0.6})
            except Exception as e:
                warnings.warn(f"⚠️ Falha na indexação de {p}: {e}")
                append_to_wiki_log("ERROR", f"Falha na indexação: {rel}", str(e), "FAIL")
                continue

    return index

def query_oracle(question):
    """
    Busca no oráculo de forma imparcial e robusta.
    O parâmetro 'role' foi removido para garantir que a confiança seja puramente técnica.
    """
    idx = build_index()
    det_idx = load_index_file()
    
    clean_question = normalize_text(question)
    all_kws = re.findall(r'\b\w{2,}\b', clean_question)
    keywords = {simple_stem(w) for w in all_kws if len(w) >= 3 or w in DOMAIN_ACRONYMS}
    hits = Counter()
    
    # 1. Busca Determinística (Peso absoluto superior para garantir prioridade sobre corpo)
    for kw in keywords:
        for match in det_idx.get(kw, []):
            hits[match["path"]] += 10.0  # Peso Massivo (Garante Top 1)
            
    # 2. Busca Léxica (Pesos variados - Vindo do build_index dinâmico)
    for kw in keywords:
        for match in idx.get(kw, []):
            # Se já houver um hit determinístico, somamos apenas se for o mesmo arquivo
            hits[match["path"]] += match["weight"]
    
    if not hits:
        return {
            "answer": "[INFO] Termo não encontrado na WIKI de Mercado. Para lógica interna (schema, PRD), consulte o bundle do projeto.",
            "confidence": 0.0, 
            "sources": [],
            "warnings": []
        }
    
    # Seleciona os top 3 matches
    top_hits = hits.most_common(3)
    
    # Processa Rank 1 (Arquivo completo)
    top_file, top_score = top_hits[0]
    if top_score >= 0.6:
        content = (CONTEXT_DIR / top_file).read_text(encoding="utf-8")
        answer = f"📄 ARQUIVO COMPLETO ({top_file}):\n\n{content}"
        sources = [top_file]
        warnings_list = []
        
        # Processa Rank 2 e 3 (Apenas Resumos)
        for file, score in top_hits[1:]:
            if score >= 0.6:
                text = (CONTEXT_DIR / file).read_text(encoding="utf-8")
                # Extrai apenas a seção ## Resumo (ignora case, pega até o próximo ## ou fim do arquivo)
                resumo_match = re.search(r'(?i)##\s*resumo\s*\n(.*?)(?=\n##\s|$)', text, re.DOTALL)
                if resumo_match:
                    resumo = resumo_match.group(1).strip()
                    answer += f"\n\n---\n📎 RESUMO SECUNDÁRIO ({file}):\n{resumo}"
                else:
                    warnings_list.append(f"Arquivo {file} sem seção ## Resumo.")
                sources.append(file)
                
        return {
            "answer": answer.strip(),
            "confidence": min(1.0, top_score),
            "sources": sources,
            "warnings": warnings_list
        }
    
    return {
        "answer": "[WARN] Referência encontrada, mas com baixa confiança. Refine a pesquisa.",
        "confidence": min(1.0, top_score),
        "sources": [top_file],
        "warnings": ["Confiança abaixo do limiar de 0.6"]
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python context_oracle.py \"sua pergunta aqui\"")
        sys.exit(1)
    res = query_oracle(sys.argv[1])
    
    # Log de Query (Resumido)
    q_stub = sys.argv[1][:30] + "..." if len(sys.argv[1]) > 30 else sys.argv[1]
    status = "OK" if res["confidence"] >= 0.5 else "FAIL"
    source = res["sources"][0] if res["sources"] else "-"
    append_to_wiki_log("QUERY", f"Busca: {q_stub} (conf: {res['confidence']:.2f})", source, status)

    try:
        print(json.dumps(res, indent=2, ensure_ascii=True))
    except Exception as e:
        print(f"[ERROR] Fail encoding json: {e}")
        
    sys.exit(0 if res["confidence"] >= 0.5 else 2)
