import unittest
import os
import shutil
import tempfile
import json
from pathlib import Path

# Adiciona o diretório de scripts ao path para importar o oracle
import sys
REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / ".context" / "_scripts"
sys.path.append(str(SCRIPTS_DIR))

try:
    import context_oracle
except ImportError:
    # Fallback se rodar fora da estrutura esperada
    context_oracle = None

class TestOracleV3(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox (Independência de OS via pathlib)
        self.test_dir = Path(tempfile.mkdtemp())
        self.context_dir = self.test_dir / ".context"
        self.wiki_dir = self.test_dir / "market" / "WIKI"
        self.wiki_dir.mkdir(parents=True, exist_ok=True)
        
        # Mock do ambiente Antigravity
        (self.test_dir / "market" / "compliance").mkdir(parents=True, exist_ok=True)
        
        # Monkeypatch do CONTEXT_DIR no módulo oracle
        if context_oracle:
            self.old_context_dir = context_oracle.CONTEXT_DIR
            context_oracle.CONTEXT_DIR = self.test_dir

    def tearDown(self):
        # Restaura o diretório original e limpa sandbox
        if context_oracle:
            context_oracle.CONTEXT_DIR = self.old_context_dir
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def create_article(self, name, content, tags=None):
        path = self.wiki_dir / f"{name}.md"
        path.write_text(content, encoding="utf-8")
        if tags:
            index_file = self.wiki_dir / "_index.md"
            with open(index_file, "a", encoding="utf-8") as f:
                f.write(f"- [[{name}]] | tags: {', '.join(tags)}\n")
        return path

    # --- TESTES BASELINE (Devem passar agora) ---

    def test_basic_query_returns_result(self):
        """Query com termo existente retorna resultado com confidence > 0."""
        self.create_article("harness", "# Test Harness\nConteúdo sobre automação.")
        res = context_oracle.query_oracle("harness")
        self.assertGreater(res["confidence"], 0)
        self.assertEqual(Path(res["sources"][0]).name, "harness.md")

    def test_empty_query_returns_missing(self):
        """Query sem match retorna status missing (ou msg informativa) e confidence 0."""
        res = context_oracle.query_oracle("termo_inexistente_total")
        self.assertEqual(res["confidence"], 0.0)
        self.assertIn("não encontrado", res["answer"])

    def test_known_term_finds_correct_file(self):
        """Busca por 'harness' retorna artigo de harness, não outro."""
        self.create_article("harness", "# Harness\nInfo do harness.")
        self.create_article("oracle", "# Oracle\nInfo do oracle.")
        res = context_oracle.query_oracle("harness")
        self.assertEqual(Path(res["sources"][0]).name, "harness.md")

    def test_index_file_is_read(self):
        """Tags do _index.md geram hits com peso 1.0."""
        self.create_article("governança", "# Governança\nDoc.", tags=["harness", "controle"])
        res = context_oracle.query_oracle("controle")
        self.assertGreaterEqual(res["confidence"], 1.0) # Tag no índice = peso 1.0

    def test_json_output_is_valid(self):
        """O retorno do query_oracle é um dicionário compatível com JSON."""
        res = context_oracle.query_oracle("teste")
        # Se não quebrar e for dict, o teste do main() que usa json.dumps passaria
        self.assertIsInstance(res, dict)
        self.assertIn("answer", res)
        self.assertIn("confidence", res)
        self.assertIn("sources", res)
        self.assertIn("warnings", res)

    # --- TESTES TARGET (Fases 0.x e 1.x - Marcados com expectedFailure) ---

    def test_markdown_in_query(self):
        """Query com '**Harness**' deve funcionar como 'Harness'."""
        self.create_article("harness", "# Test Harness\nHarness é automação.")
        res = context_oracle.query_oracle("**Harness**")
        self.assertGreater(res["confidence"], 0.5)

    def test_accent_normalization(self):
        """Busca por 'configuracao' deve encontrar 'configuração'."""
        self.create_article("config", "# Configuração\nComo configurar.")
        res = context_oracle.query_oracle("configuracao")
        self.assertGreater(res["confidence"], 0.5)

    def test_aliases_indexed(self):
        """Artigo com aliases no frontmatter deve ser encontrado por alias."""
        # Nota: O teste cria o arquivo e o _index.md manualmente no setUp/helper.
        # No Oracle v3 real, o ingest_wiki_guard geraria isso. 
        # Aqui o helper create_article usa tags, mas vamos simular o hit de alias via tags.
        self.create_article("harness", "# Harness", tags=["integração", "ci"])
        res = context_oracle.query_oracle("integração")
        self.assertGreater(res["confidence"], 0.5)

    def test_siglas_2_chars(self):
        """Busca por 'QA' não deve retornar vazio."""
        self.create_article("qa_doc", "# Quality Assurance\nProcessos de QA.")
        res = context_oracle.query_oracle("QA")
        self.assertGreater(res["confidence"], 0)

    def test_stem_converges(self):
        """Buscas por 'testar', 'teste' e 'testes' devem convergir para a mesma raiz."""
        self.create_article("qa", "# Teste de Software\nProcesso de testes e validação.")
        res1 = context_oracle.query_oracle("testar")
        res2 = context_oracle.query_oracle("testes")
        self.assertEqual(res1["sources"], res2["sources"])
        self.assertGreater(res1["confidence"], 0.2)

    def test_confidence_calibrated(self):
        """Match por tag (1.0) deve ter confidence > match por corpo acumulado."""
        # Cria um arquivo com 6 ocorrências de 'palavra' (0.2 * 6 = 1.2 -> cap 1.0)
        self.create_article("corpo", "# Doc\npalavra palavra palavra palavra palavra palavra")
        # Cria um arquivo com match de tag no index (peso 1.0)
        self.create_article("tag", "# Doc", tags=["palavra"])
        
        res_corpo = context_oracle.query_oracle("palavra")
        # Aqui, no Oracle v2, o hit pode estar vindo de ambos. 
        # Queremos que o resultado da query 'palavra' seja o arquivo 'tag.md' com confidence maior
        # que se fosse apenas corpo acumulado.
        
        # Atualmente o Oracle v2 retorna o primeiro most_common(1). 
        # Se os scores forem iguais (ambos 1.0), a ordem é arbitrária.
        
        # Na Fase 1.2, queremos que 'tag' tenha score > 1.0 (antes do cap) ou que a normalização diferencie.
        # Por enquanto, forçamos a falha se o score for igual.
        self.assertEqual(Path(res_corpo["sources"][0]).name, "tag.md")
        self.assertGreater(res_corpo["confidence"], 0.9)

    def test_top_n_graduated(self):
        """Top-N: Rank 1 retorna integral, Ranks 2 e 3 retornam apenas o ## Resumo se aplicável."""
        # Cria artigo Rank 1 (Score alto via tag)
        self.create_article("rank1", "# Alpha\nConteudo longo Alpha.\n## Resumo\nResumo alpha.", tags=["alpha"])
        # Cria artigo Rank 2 (Score via body/title, mas menor que tag)
        self.create_article("rank2", "# Alpha Beta\nConteudo longo Beta.\n## Resumo\nResumo beta.")
        # Cria artigo Rank 3 (Score via body)
        self.create_article("rank3", "# Gama\nAlpha aparece aqui.\n## Resumo\nResumo gama.")
        
        res = context_oracle.query_oracle("alpha")
        # O answer deve conter o texto completo do rank1, e apenas o resumo do rank2 e rank3
        self.assertIn("Conteudo longo Alpha", res["answer"])
        self.assertNotIn("Conteudo longo Beta", res["answer"])
        self.assertIn("Resumo beta", res["answer"])
        source_names = [Path(s).name for s in res["sources"]]
        self.assertIn("rank1.md", source_names)
        self.assertIn("rank2.md", source_names)

if __name__ == "__main__":
    unittest.main()
