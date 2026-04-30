#!/usr/bin/env python3
"""
🛡️ ingest_wiki_guard.py — Guardião de Ingestão Wiki (H.O.K v2.5)
Valida conformidade Karpathy antes de permitir a entrada de novos artigos.
"""
import re, sys, os, time
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
WIKI_DIR = CONTEXT_DIR / "market" / "WIKI"

# Import utilitário de log
sys.path.append(str(CONTEXT_DIR / "_scripts"))
try:
    from _wiki_log_utils import append_to_wiki_log
except ImportError:
    def append_to_wiki_log(*args): pass

def validate_article(path):
    content = path.read_text(encoding="utf-8")
    errors = []

    # 1. Validação de Frontmatter
    frontmatter_match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not frontmatter_match:
        errors.append("Frontmatter (---) ausente ou mal formado.")
    else:
        fields = frontmatter_match.group(1)
        required = ['id:', 'entity:', 'concept:', 'tags:', 'source:', 'last_updated:']
        for r in required:
            if r not in fields:
                errors.append(f"Campo obrigatório '{r}' ausente no frontmatter.")

    # 2. Validação de Fonte (Karpathy Rule)
    if not re.search(r'^>\s*Fonte:\s*(market/)?RAW/.+\.md', content, re.MULTILINE):
        errors.append("Citação de fonte '> Fonte: RAW/...' ausente ou inválida.")

    # 3. Estrutura Mínima
    if "## Key Takeaways" not in content:
        errors.append("Seção '## Key Takeaways' ausente.")
    
    if "## Related" not in content and "[[" not in content:
        errors.append("Conectividade ausente (Seção '## Related' ou '[[wikilinks]]' necessários).")

    return errors

def rebuild_index_atomic(articles):
    """Reconstrói o _index.md de forma atômica para evitar corrupção de leitura."""
    header = "# WIKI Index Raiz\n> Fonte: SSOT_MAP.md\n\n## Topicos\n"
    lines = []
    for art in articles:
        content = art.read_text(encoding="utf-8")
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        tag_list = []
        if match:
            fields = match.group(1)
            for line in fields.split('\n'):
                # Captura tags: e aliases:
                if line.strip().startswith('tags:') or line.strip().startswith('aliases:'):
                    # Limpa o prefixo, espaços e colchetes
                    val = re.sub(r'^(tags|aliases):\s*', '', line.strip()).strip('[]')
                    if val:
                        tag_list.extend([t.strip() for t in val.split(',')])
        
        # Consolida tudo em uma string separada por vírgula para o _index.md
        tags_str = ", ".join(sorted(set(tag_list)))
        lines.append(f"- [[{art.stem}]] | tags: {tags_str}\n")
    
    # Ordem alfabética para determinismo
    lines.sort()
    index_content = header + "".join(lines)
    
    index_path = WIKI_DIR / "_index.md"
    tmp_path = WIKI_DIR / "_index.md.tmp"
    
    tmp_path.write_text(index_content, encoding="utf-8")
    
    # Retry Backoff para contornar travamentos de I/O no Windows (PermissionError)
    for attempt in range(3):
        try:
            os.replace(tmp_path, index_path)
            break
        except PermissionError:
            if attempt == 2:
                print("⚠️ Falha ao regenerar o _index.md (Arquivo travado por outro processo).")
                raise
            time.sleep(0.5 * (attempt + 1))

def main():
    if not WIKI_DIR.exists():
        print("[OK] Diretório WIKI não encontrado. Ignorando.")
        sys.exit(0)

    # Coleta arquivos para validar (excluindo templates e indices)
    articles = [p for p in WIKI_DIR.rglob("*.md") if not p.name.startswith("_")]
    
    if not articles:
        print("[OK] Nenhum artigo novo para validar.")
        append_to_wiki_log("SKIP", "Nenhum artigo detectado para ingestão", "-", "OK")
        sys.exit(0)

    all_errors = {}
    for art in articles:
        rel_path = art.relative_to(CONTEXT_DIR).as_posix()
        errs = validate_article(art)
        if errs:
            all_errors[rel_path] = errs

    if all_errors:
        print("❌ FALHA NA INGESTÃO WIKI:")
        paths = []
        for path, errs in all_errors.items():
            paths.append(path)
            print(f"\n📄 {path}:")
            for e in errs:
                print(f"  - {e}")
        append_to_wiki_log("INGEST", "Falha de conformidade Karpathy", ", ".join(paths), "FAIL")
        sys.exit(1)

    rebuild_index_atomic(articles)
    print(f"✅ Todos os {len(articles)} artigos WIKI estão em conformidade e o índice foi regenerado.")
    filenames = [a.name for a in articles]
    append_to_wiki_log("INGEST", f"Ingestão de {len(articles)} artigos", ", ".join(filenames), "OK")
    sys.exit(0)

if __name__ == "__main__":
    # Garante UTF-8 no Windows
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()
