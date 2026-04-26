# Project Context Bundle

---
schema_version: 1
generated_at: 2026-04-23T18:33:30.791110+00:00
root: template_inicío_de_projeto
mode: full
profile: ai-default
file_count: 74
byte_count: 230293
ignored_dirs:
  - .cache
  - .cursor
  - .git
  - .idea
  - .mypy_cache
  - .netlify
  - .next
  - .nuxt
  - .pytest_cache
  - .ruff_cache
  - .tox
  - .venv
  - .vercel
  - .vite
  - .vscode
  - RAW
  - __pycache__
  - _archive_context
  - bin
  - build
  - captura_projeto
  - coverage
  - dist
  - node_modules
  - obj
  - out
  - planos
  - target
  - venv
sensitive_rules:
  - *.cert
  - *.key
  - *.p12
  - *.pem
  - *.pfx
  - .env*
  - credentials*.json
  - id_rsa*
  - secrets.*
---

## INDEX_BY_DOMAIN
- `config`:
  - `.context/maintenance/version_targets.json` -> [file_51ed93c9d8ab](#file_51ed93c9d8ab)
  - `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
  - `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `db`:
  - `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `docs`:
  - ` .specs/features/docs_resenha/STATE.md` -> [file_f6a9dd4e6c97](#file_f6a9dd4e6c97)
  - ` .specs/features/docs_resenha/spec.md` -> [file_736dc30bc94f](#file_736dc30bc94f)
  - ` .specs/features/hardening_v2.5/STATE.md` -> [file_5f4ef6860006](#file_5f4ef6860006)
  - ` .specs/features/hardening_v2.5/spec.md` -> [file_f941f64c38fb](#file_f941f64c38fb)
  - ` .specs/features/sync_maintenance/STATE.md` -> [file_39347a56c033](#file_39347a56c033)
  - ` .specs/features/sync_maintenance/spec.md` -> [file_9c99344c7962](#file_9c99344c7962)
  - `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
  - `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
  - `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
  - `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
  - `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
  - `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
  - `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
  - `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
  - `.context/brain/START_HERE.md` -> [file_e11d89201917](#file_e11d89201917)
  - `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
  - `.context/brain/VISION.md` -> [file_d2f31e4696a6](#file_d2f31e4696a6)
  - `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
  - `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
  - `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
  - `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
  - `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
  - `.context/market/WIKI/_index.md` -> [file_578d56cac1a4](#file_578d56cac1a4)
  - `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
  - `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
  - `.context/market/wiki_log.md` -> [file_c255058b56fe](#file_c255058b56fe)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
  - `.context/specs/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_37fb63b0fac5](#file_37fb63b0fac5)
  - `.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_0511c79bd7d2](#file_0511c79bd7d2)
  - `.specs/_template.md` -> [file_b838611f038c](#file_b838611f038c)
  - `.specs/features/harness_fail_closed/STATE.md` -> [file_d4f64fc3b549](#file_d4f64fc3b549)
  - `.specs/features/harness_fail_closed/spec.md` -> [file_a32e3bf74e3d](#file_a32e3bf74e3d)
  - `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
  - `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
  - `.specs/features/wiki_level2/STATE.md` -> [file_638d6695a3f1](#file_638d6695a3f1)
  - `.specs/features/wiki_level2/spec.md` -> [file_86778e912e18](#file_86778e912e18)
  - `.specs/features/wiki_level2/tasks.md` -> [file_fafce66dc671](#file_fafce66dc671)
  - `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
  - `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
  - `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
  - `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
  - `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
  - `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `source`:
  - `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
  - `.context/_scripts/_wiki_log_utils.py` -> [file_9ee5d49278ad](#file_9ee5d49278ad)
  - `.context/_scripts/check_version_consistency.py` -> [file_4ffe1a34765a](#file_4ffe1a34765a)
  - `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
  - `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
  - `.context/_scripts/enrich_context.py` -> [file_e94b4e40315c](#file_e94b4e40315c)
  - `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
  - `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
  - `.context/_scripts/ingest_wiki_guard.py` -> [file_0731dcfd7873](#file_0731dcfd7873)
  - `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
  - `.context/_scripts/migration_registry.py` -> [file_d65b48a9d56c](#file_d65b48a9d56c)
  - `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
  - `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
  - `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
  - `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
  - `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
  - `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
  - `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
  - `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
  - `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
  - `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
  - `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

## INDEX_BY_PATH
- ` .specs/features/docs_resenha/STATE.md` -> [file_f6a9dd4e6c97](#file_f6a9dd4e6c97)
- ` .specs/features/docs_resenha/spec.md` -> [file_736dc30bc94f](#file_736dc30bc94f)
- ` .specs/features/hardening_v2.5/STATE.md` -> [file_5f4ef6860006](#file_5f4ef6860006)
- ` .specs/features/hardening_v2.5/spec.md` -> [file_f941f64c38fb](#file_f941f64c38fb)
- ` .specs/features/sync_maintenance/STATE.md` -> [file_39347a56c033](#file_39347a56c033)
- ` .specs/features/sync_maintenance/spec.md` -> [file_9c99344c7962](#file_9c99344c7962)
- `.context/_scripts/_tz_utils.py` -> [file_dbef1acce0d4](#file_dbef1acce0d4)
- `.context/_scripts/_wiki_log_utils.py` -> [file_9ee5d49278ad](#file_9ee5d49278ad)
- `.context/_scripts/check_version_consistency.py` -> [file_4ffe1a34765a](#file_4ffe1a34765a)
- `.context/_scripts/cleanup_specs.py` -> [file_82cd6bde54ff](#file_82cd6bde54ff)
- `.context/_scripts/context_oracle.py` -> [file_10081abf87e1](#file_10081abf87e1)
- `.context/_scripts/enrich_context.py` -> [file_e94b4e40315c](#file_e94b4e40315c)
- `.context/_scripts/harness_runner.py` -> [file_1edef35c2f56](#file_1edef35c2f56)
- `.context/_scripts/health_sync.py` -> [file_a642d240b9ab](#file_a642d240b9ab)
- `.context/_scripts/ingest_wiki_guard.py` -> [file_0731dcfd7873](#file_0731dcfd7873)
- `.context/_scripts/lint_wiki.py` -> [file_ab41b07fb3fb](#file_ab41b07fb3fb)
- `.context/_scripts/migration_registry.py` -> [file_d65b48a9d56c](#file_d65b48a9d56c)
- `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
- `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
- `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
- `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
- `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
- `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
- `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
- `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
- `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
- `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
- `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
- `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
- `.context/brain/START_HERE.md` -> [file_e11d89201917](#file_e11d89201917)
- `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
- `.context/brain/VISION.md` -> [file_d2f31e4696a6](#file_d2f31e4696a6)
- `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
- `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
- `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
- `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
- `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/maintenance/version_targets.json` -> [file_51ed93c9d8ab](#file_51ed93c9d8ab)
- `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
- `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
- `.context/market/WIKI/_index.md` -> [file_578d56cac1a4](#file_578d56cac1a4)
- `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
- `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
- `.context/market/wiki_log.md` -> [file_c255058b56fe](#file_c255058b56fe)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
- `.context/specs/DIRECTIVA_V2.4.1_HARDENED.md` -> [file_37fb63b0fac5](#file_37fb63b0fac5)
- `.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md` -> [file_0511c79bd7d2](#file_0511c79bd7d2)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `.specs/_template.md` -> [file_b838611f038c](#file_b838611f038c)
- `.specs/features/harness_fail_closed/STATE.md` -> [file_d4f64fc3b549](#file_d4f64fc3b549)
- `.specs/features/harness_fail_closed/spec.md` -> [file_a32e3bf74e3d](#file_a32e3bf74e3d)
- `.specs/features/meta-inception/STATE.md` -> [file_238a0e1da225](#file_238a0e1da225)
- `.specs/features/meta-inception/spec.md` -> [file_9801af51c558](#file_9801af51c558)
- `.specs/features/wiki_level2/STATE.md` -> [file_638d6695a3f1](#file_638d6695a3f1)
- `.specs/features/wiki_level2/spec.md` -> [file_86778e912e18](#file_86778e912e18)
- `.specs/features/wiki_level2/tasks.md` -> [file_fafce66dc671](#file_fafce66dc671)
- `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
- `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
- `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
- `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `captura_projeto.py` -> [file_c3916196f58f](#file_c3916196f58f)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)

---
<a id="file_f6a9dd4e6c97"></a>
FILE_START id=file_f6a9dd4e6c97 path= .specs/features/docs_resenha/STATE.md domain=docs lang=markdown lines=5 bytes=82 mtime=2026-04-23T14:06:00.087931+00:00 sha1=55b3a4ebae1aa940ec05b1cdd1a340d3d2a43372
CHUNK_START id=f6a9dd4e6c97_c001 start_line=1 end_line=5
```markdown
---
status: ✅ PASSED
updated: 2026-04-21
detail: Resenha gerada e validada.
---

```
CHUNK_END id=f6a9dd4e6c97_c001
FILE_END id=file_f6a9dd4e6c97

---
<a id="file_736dc30bc94f"></a>
FILE_START id=file_736dc30bc94f path= .specs/features/docs_resenha/spec.md domain=docs lang=markdown lines=9 bytes=274 mtime=2026-04-23T14:06:00.089930+00:00 sha1=8a2e4d88781bc7bcdd94940eb3d745ccb40a0143
CHUNK_START id=736dc30bc94f_c001 start_line=1 end_line=9
```markdown
---
status: ATIVO
definition_of_done: Criação da resenha.md na raiz explicando o framework v2.5.
qa_signoff: true
signed_by: "@qa-validator"
---

# Spec: Documentação Mestre v2.5 (Resenha)
Este documento autoriza a geração da resenha.md conforme pedido pelo usuário.

```
CHUNK_END id=736dc30bc94f_c001
FILE_END id=file_736dc30bc94f

---
<a id="file_5f4ef6860006"></a>
FILE_START id=file_5f4ef6860006 path= .specs/features/hardening_v2.5/STATE.md domain=docs lang=markdown lines=5 bytes=84 mtime=2026-04-23T14:06:00.092132+00:00 sha1=bc5c3f83bfe9e8fbb1ee3058dc9dfcda6dcdce91
CHUNK_START id=5f4ef6860006_c001 start_line=1 end_line=5
```markdown
---
status: ✅ PASSED
updated: 2026-04-21
detail: Matriz formadora concluída.
---

```
CHUNK_END id=5f4ef6860006_c001
FILE_END id=file_5f4ef6860006

---
<a id="file_f941f64c38fb"></a>
FILE_START id=file_f941f64c38fb path= .specs/features/hardening_v2.5/spec.md domain=docs lang=markdown lines=13 bytes=449 mtime=2026-04-23T14:06:00.093643+00:00 sha1=54b211d4df661279c1738893d9a114caab2314e7
CHUNK_START id=f941f64c38fb_c001 start_line=1 end_line=13
```markdown
---
status: ATIVO
definition_of_done: Finalização do Hardening v2.5 com injeção de hooks e atualização do MASTER_FLOW.
qa_signoff: true
signed_by: "@qa-validator"
---

# Spec: Hardening v2.5 Matriz Final
Esta spec autoriza o commit de encerramento da versão 2.5 (Karpathy Hardened).
Ações:
- Injeção de System Hooks nos placeholders.
- Atualização da Tabela de 4 Atos no MASTER_FLOW.md.
- Atualização do ROADMAP.md e ARCHITECTURE.md.

```
CHUNK_END id=f941f64c38fb_c001
FILE_END id=file_f941f64c38fb

---
<a id="file_39347a56c033"></a>
FILE_START id=file_39347a56c033 path= .specs/features/sync_maintenance/STATE.md domain=docs lang=markdown lines=5 bytes=101 mtime=2026-04-23T14:06:00.095644+00:00 sha1=bf670324c5382439ece01583d60d3bc540025347
CHUNK_START id=39347a56c033_c001 start_line=1 end_line=5
```markdown
---
status: ✅ PASSED
updated: 2026-04-22
detail: Arquivos de manutenção prontos para commit.
---

```
CHUNK_END id=39347a56c033_c001
FILE_END id=file_39347a56c033

---
<a id="file_9c99344c7962"></a>
FILE_START id=file_9c99344c7962 path= .specs/features/sync_maintenance/spec.md domain=docs lang=markdown lines=9 bytes=327 mtime=2026-04-23T14:06:00.096642+00:00 sha1=4dc412152491353d37e335453581463266a7c1cb
CHUNK_START id=9c99344c7962_c001 start_line=1 end_line=9
```markdown
---
status: ATIVO
definition_of_done: Sincronização de arquivos de manutenção (Journal, Health, Tech Reqs) e arquivamento de specs históricas.
qa_signoff: true
signed_by: "@qa-validator"
---

# Spec: Sincronia de Manutenção
Autoriza o commit das atualizações automáticas de contexto e arquivamento de specs de ontem.

```
CHUNK_END id=9c99344c7962_c001
FILE_END id=file_9c99344c7962

---
<a id="file_dbef1acce0d4"></a>
FILE_START id=file_dbef1acce0d4 path=.context/_scripts/_tz_utils.py domain=source lang=python lines=37 bytes=1257 mtime=2026-04-12T02:47:25.198957+00:00 sha1=a49568f45d4b962ab01f0ed4b359ee4c09f65741
CHUNK_START id=dbef1acce0d4_c001 start_line=1 end_line=37
```python
#!/usr/bin/env python3
"""
🕐 _tz_utils.py — Motor de Fuso Horário (Stdlib Only)
Padrão: America/Sao_Paulo (UTC-3). Configurável via env var CONTEXT_TIMEZONE.
"""
import os
from datetime import datetime, timezone, timedelta

# Dicionário de Timezones (Brasília offset fixo)
TZ_MAP = {
    "America/Sao_Paulo": timedelta(hours=-3),
    "America/Recife": timedelta(hours=-3),
    "America/Manaus": timedelta(hours=-4),
    "America/Los_Angeles": timedelta(hours=-8),
    "America/New_York": timedelta(hours=-5),
    "Europe/London": timedelta(hours=0),
    "Europe/Berlin": timedelta(hours=1),
    "Asia/Tokyo": timedelta(hours=9),
    "UTC": timedelta(hours=0),
}

def get_now_tz():
    """Retorna o datetime atual no timezone configurado."""
    tz_name = os.environ.get("CONTEXT_TIMEZONE", "America/Sao_Paulo")
    offset = TZ_MAP.get(tz_name, timedelta(hours=-3))
    return datetime.now(timezone(offset))

def format_ts(dt=None, fmt="%Y-%m-%d %H:%M"):
    """Formata o datetime para string legível."""
    if dt is None:
        dt = get_now_tz()
    return dt.strftime(fmt)

if __name__ == "__main__":
    # Teste isolado
    tz_env = os.environ.get("CONTEXT_TIMEZONE", "America/Sao_Paulo")
    print(f"[OK] Agora em {tz_env}: {format_ts()}")

```
CHUNK_END id=dbef1acce0d4_c001
FILE_END id=file_dbef1acce0d4

---
<a id="file_9ee5d49278ad"></a>
FILE_START id=file_9ee5d49278ad path=.context/_scripts/_wiki_log_utils.py domain=source lang=python lines=66 bytes=2541 mtime=2026-04-22T23:47:25.409048+00:00 sha1=eb8650ba121fe8cc8aaabaca70de01214509937e
CHUNK_START id=9ee5d49278ad_c001 start_line=1 end_line=66
```python
#!/usr/bin/env python3
"""
🛠️ _wiki_log_utils.py — Utilitário de Rastreabilidade Wiki (H.O.K v2.5.1)
Centraliza a escrita robusta e sincronizada no wiki_log.md.
"""
import os
import sys
import time
from datetime import datetime
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = CONTEXT_DIR / "market/wiki_log.md"
LOCK_FILE = CONTEXT_DIR / "_scripts/_wiki_log.lock"

def append_to_wiki_log(mode, description, files, status):
    """
    Adiciona uma entrada ao log da Wiki de forma robusta e sincronizada.
    mode: INGEST | LINT | QUERY | SKIP
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Escape de pipes para não quebrar a tabela Markdown
    safe_desc = str(description).replace("|", "\\|")
    safe_files = str(files).replace("|", "\\|")
    
    line = f"| [{timestamp}] | {mode} | {safe_desc} | {safe_files} | {status} |\n"
    
    # Sincronização Simples (Spin Lock) para evitar concorrência
    timeout = 5 # 5 segundos de timeout
    start_time = time.time()
    
    while True:
        try:
            # Tenta criar o arquivo de lock de forma exclusiva
            fd = os.open(LOCK_FILE, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            try:
                # Se não existir o log, cria com cabeçalhos
                if not LOG_FILE.exists():
                    headers = [
                        "# Wiki Log (Append-only)\n\n",
                        "| Timestamp | Mode | Description | Files | Status |\n",
                        "|-----------|------|-------------|-------|--------|\n"
                    ]
                    LOG_FILE.write_text("".join(headers), encoding="utf-8")
                
                with open(LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(line)
                break # Sucesso
            finally:
                os.close(fd)
                os.remove(LOCK_FILE)
        except FileExistsError:
            if time.time() - start_time > timeout:
                print(f"[WARN] Timeout ao aguardar lock do wiki_log.md", file=sys.stderr)
                break
            time.sleep(0.1)
        except Exception as e:
            print(f"[WARN] Falha ao gravar no wiki_log.md: {e}", file=sys.stderr)
            break

if __name__ == "__main__":
    # Teste rápido se chamado diretamente
    test_mode = sys.argv[1] if len(sys.argv) > 1 else "TEST"
    append_to_wiki_log(test_mode, "Teste de utilitário", "test.py", "OK")
    print(f"[OK] Entrada de teste '{test_mode}' gravada.")

```
CHUNK_END id=9ee5d49278ad_c001
FILE_END id=file_9ee5d49278ad

---
<a id="file_4ffe1a34765a"></a>
FILE_START id=file_4ffe1a34765a path=.context/_scripts/check_version_consistency.py domain=source lang=python lines=80 bytes=2486 mtime=2026-04-22T12:37:52.914197+00:00 sha1=0f0bcd180ff803df099fc5f865ce6d3106e196d2
CHUNK_START id=4ffe1a34765a_c001 start_line=1 end_line=80
```python
#!/usr/bin/env python3
"""Verifica consistencia de versao via SSOT (VERSION.md) e matriz declarativa."""

import json
import re
import sys
from pathlib import Path

# .../.context/_scripts/check_version_consistency.py -> raiz em parents[2]
ROOT = Path(__file__).resolve().parents[2]
VERSION_FILE = ROOT / "VERSION.md"
TARGETS_FILE = ROOT / ".context" / "maintenance" / "version_targets.json"


def get_ssot_version():
    if not VERSION_FILE.exists():
        return None
    text = VERSION_FILE.read_text(encoding="utf-8")
    # Aceita vX.Y ou vX.Y.Z e normaliza para X.Y.Z
    match = re.search(r"^\s*v?(\d+)\.(\d+)(?:\.(\d+))?\s*$", text, re.MULTILINE)
    if not match:
        return None
    major, minor, patch = match.group(1), match.group(2), match.group(3) or "0"
    return f"{major}.{minor}.{patch}"


def normalize_version(value):
    value = value.strip()
    m = re.match(r"^(\d+)\.(\d+)(?:\.(\d+))?$", value)
    if not m:
        return value
    return f"{m.group(1)}.{m.group(2)}.{m.group(3) or '0'}"


def validate_targets(version):
    if not TARGETS_FILE.exists():
        return [".context/maintenance/version_targets.json (ausente)"]

    data = json.loads(TARGETS_FILE.read_text(encoding="utf-8"))
    targets = data.get("targets", [])
    mismatches = []

    for target in targets:
        rel_path = target["path"]
        fpath = ROOT / rel_path
        if not fpath.exists():
            mismatches.append(f"{rel_path} (ausente)")
            continue

        content = fpath.read_text(encoding="utf-8")
        flags = re.MULTILINE if target.get("multiline") else 0
        m = re.search(target["pattern"], content, flags)

        if not m:
            mismatches.append(f"{rel_path} (padrao nao encontrado)")
            continue

        found = normalize_version(m.group(1))
        if found != version:
            mismatches.append(f"{rel_path} (esperado {version}, achado {found})")

    return mismatches


if __name__ == "__main__":
    ssot_version = get_ssot_version()
    if not ssot_version:
        print("[FATAL] VERSION.md invalido ou ausente.")
        sys.exit(1)

    errors = validate_targets(ssot_version)
    if errors:
        print(f"\n[ERROR] Drift de versao detectado (SSOT: v{ssot_version}):")
        for err in errors:
            print(f"  - {err}")
        print("\n[FATAL] Corrija manualmente os arquivos-alvo e rode novamente.")
        sys.exit(1)

    print(f"[OK] Versao consistente: v{ssot_version}")
    sys.exit(0)

```
CHUNK_END id=4ffe1a34765a_c001
FILE_END id=file_4ffe1a34765a

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=71 bytes=2335 mtime=2026-04-11T02:29:19.704104+00:00 sha1=8567b3ea9b8c513859bab8793632e38aef509fd5
CHUNK_START id=82cd6bde54ff_c001 start_line=1 end_line=71
```python
#!/usr/bin/env python3
"""
🧹 cleanup_specs.py
Gerencia a efemeridade da bancada de trabalho (.specs/).
Aplica a regra de 48h de inatividade e limite de 3 specs ativas simultâneas.
Arquiva specs excedentes ou obsoletas em _archive_context/specs/.
"""
import os
import shutil
import time
from pathlib import Path
from datetime import datetime

# Caminhos base
SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
SPECS_DIR = CONTEXT_DIR.parent / ".specs" / "features"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "specs"

# Configurações
MAX_INACTIVITY_SECONDS = 48 * 3600  # 48 horas
MAX_ACTIVE_SPECS = 3

def get_specs():
    if not SPECS_DIR.exists():
        return []
    return [d for d in SPECS_DIR.iterdir() if d.is_dir()]

def archive_spec(spec_path):
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"{spec_path.name}_{timestamp}"
    dest_path = ARCHIVE_DIR / archive_name
    
    print(f"[INFO] Arquivando spec: {spec_path.name} -> {archive_name}")
    shutil.move(str(spec_path), str(dest_path))

def cleanup():
    specs = get_specs()
    if not specs:
        print("[OK] Nenhuma spec ativa encontrada.")
        return

    now = time.time()
    active_specs = []

    # 1. Limpeza por inatividade (48h)
    for spec in specs:
        last_mod = max(os.path.getmtime(root) for root, _, _ in os.walk(spec))
        if (now - last_mod) > MAX_INACTIVITY_SECONDS:
            print(f"[AUTO] Inatividade detectada (>48h) em: {spec.name}")
            archive_spec(spec)
        else:
            active_specs.append(spec)

    # 2. Limpeza por limite de volume (Max 3)
    # Ordena por data de modificação (mais antiga primeiro)
    active_specs.sort(key=lambda s: max(os.path.getmtime(root) for root, _, _ in os.walk(s)))
    
    while len(active_specs) > MAX_ACTIVE_SPECS:
        oldest = active_specs.pop(0)
        print(f"[AUTO] Limite de volume excedido (Max {MAX_ACTIVE_SPECS}). Removendo spec mais antiga: {oldest.name}")
        archive_spec(oldest)

    print(f"[OK] Manutencao de specs concluida. Specs ativas: {len(active_specs)}/{MAX_ACTIVE_SPECS}")

if __name__ == "__main__":
    try:
        cleanup()
    except Exception as e:
        print(f"[ERROR] Falha na limpeza de specs: {e}")

```
CHUNK_END id=82cd6bde54ff_c001
FILE_END id=file_82cd6bde54ff

---
<a id="file_10081abf87e1"></a>
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=133 bytes=5290 mtime=2026-04-22T23:34:52.248624+00:00 sha1=61d7e4d041f8821d2240f83a9ad8b5c26baa9cb9
CHUNK_START id=10081abf87e1_c001 start_line=1 end_line=133
```python
#!/usr/bin/env python3
"""
🔍 context_oracle.py — Oráculo de consulta local (H.O.K v2.5 Optimized)
Busca determinística na camada WIKI/Compliance com retorno integral de arquivos.
"""
import re, sys, json, os
from pathlib import Path
from collections import Counter

CONTEXT_DIR = Path(__file__).resolve().parents[1]

# Import utilitário de log
sys.path.append(str(CONTEXT_DIR / "_scripts"))
try:
    from _wiki_log_utils import append_to_wiki_log
except ImportError:
    def append_to_wiki_log(*args): pass

def load_index_file():
    """Lê o índice mestre WIKI para roteamento determinístico."""
    index_file = CONTEXT_DIR / "market/WIKI/_index.md"
    mapping = {}
    if index_file.exists():
        content = index_file.read_text(encoding="utf-8")
        # Encontra padrões como: - [[link]] | tags: t1, t2
        matches = re.finditer(r'- \[\[(.+?)\]\]\s*\|\s*tags:\s*(.+)', content)
        for m in matches:
            path_stub = m.group(1).strip()
            tags = [t.strip().lower() for t in m.group(2).split(",")]
            for tag in tags:
                # Peso 1.0 para tags explícitas no índice
                mapping.setdefault(tag, []).append({"path": f"market/WIKI/{path_stub}.md", "weight": 1.0})
    return mapping

def build_index():
    index = {}
    # 🔒 Restringe busca APENAS a WIKI e compliance (Princípio do Menor Privilégio)
    search_paths = [
        CONTEXT_DIR / "market/WIKI",
        CONTEXT_DIR / "market/compliance"
    ]
    
    for search_dir in search_paths:
        if not search_dir.exists(): continue
        # rglob para varredura recursiva
        for p in search_dir.rglob("*.md"):
            try:
                rel = p.relative_to(CONTEXT_DIR).as_posix()
                text = p.read_text(encoding="utf-8")
                
                # Heurística de Matching 1: Palavras-chave no corpo
                words = re.findall(r'\b\w{3,}\b', text.lower())
                for w in set(words):
                    index.setdefault(w, []).append({"path": rel, "weight": 0.2})
                
                # Heurística de Matching 2: Nome do arquivo (stem)
                stem = p.stem.lower()
                index.setdefault(stem, []).append({"path": rel, "weight": 0.5})
                
                # Heurística de Matching 3: Título / Keywords no Título
                title_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
                if title_match:
                    title = title_match.group(1).strip().lower()
                    # Match exato do título (0.8)
                    index.setdefault(title, []).append({"path": rel, "weight": 0.8})
                    # Keywords dentro do título (0.6 por palavra do título)
                    title_words = re.findall(r'\b\w{3,}\b', title)
                    for tw in set(title_words):
                        index.setdefault(tw, []).append({"path": rel, "weight": 0.6})
            except Exception:
                continue
    return index

def query_oracle(question, role="unknown"):
    idx = build_index()
    det_idx = load_index_file()
    keywords = set(re.findall(r'\b\w{3,}\b', question.lower()))
    hits = Counter()
    
    # 1. Busca Determinística (Peso 1.0 - Vindo do _index.md)
    for kw in keywords:
        for match in det_idx.get(kw, []):
            hits[match["path"]] += match["weight"]
            
    # 2. Busca Léxica (Pesos variados - Vindo do build_index dinâmico)
    for kw in keywords:
        for match in idx.get(kw, []):
            # Se já houver um hit determinístico, somamos apenas se for o mesmo arquivo
            hits[match["path"]] += match["weight"]
    
    if not hits:
        return {
            "answer": "[INFO] Termo não encontrado na WIKI de Mercado. Para lógica interna (schema, PRD), consulte o bundle do projeto.",
            "confidence": 0.0, 
            "sources": []
        }
    
    # Seleciona apenas o match mais relevante (1 arquivo atômico por vez)
    top_file, score = hits.most_common(1)[0]
    
    # Retorno Integral (Anti-Bloat)
    if score >= 0.6:
        content = (CONTEXT_DIR / top_file).read_text(encoding="utf-8")
        return {
            "answer": f"📄 ARQUIVO COMPLETO ({top_file}):\n\n{content}",
            "confidence": min(1.0, score),
            "sources": [top_file]
        }
    
    return {
        "answer": "[WARN] Referência encontrada, mas com baixa confiança. Refine a pesquisa.",
        "confidence": score,
        "sources": [top_file]
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python context_oracle.py \"sua pergunta aqui\"")
        sys.exit(1)
    res = query_oracle(sys.argv[1], os.environ.get("AGENT_ROLE", "manual"))
    
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

```
CHUNK_END id=10081abf87e1_c001
FILE_END id=file_10081abf87e1

---
<a id="file_e94b4e40315c"></a>
FILE_START id=file_e94b4e40315c path=.context/_scripts/enrich_context.py domain=source lang=python lines=125 bytes=4876 mtime=2026-04-17T00:17:17.361963+00:00 sha1=6ab638ce0553fdafde495ea2f64fc30ae300f765
CHUNK_START id=e94b4e40315c_c001 start_line=1 end_line=125
```python
#!/usr/bin/env python3
"""
🕵️‍♂️ enrich_context.py — Valida gaps de mercado e prepara scaffolding.
Exit: 0 (PRD ready) | 2 (Research needed) | 1 (Structural error)
"""
import re, sys
# Forçar UTF-8 em Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from datetime import date
from pathlib import Path

# Configuração de caminhos relativos ao script
CONTEXT_DIR = Path(__file__).resolve().parents[1]
INCEPTION = CONTEXT_DIR / "brain" / "INCEPTION.md"
MARKET = CONTEXT_DIR / "market"
INBOX = MARKET / "MARKET_INBOX.md"

def scan_entities():
    if not INCEPTION.exists(): return [], "INCEPTION.md ausente"
    text = INCEPTION.read_text(encoding="utf-8")
    # Captura entidades conhecidas (case-insensitive)
    entities = re.findall(r'(META|Stripe|Supabase|Firebase|AWS|LGPD|PCI|HIPAA|Oracle|MongoDB|PostgreSQL|React|Node|Python)\b', text, re.I)
    return list(set(entities)), "OK"

def check_market_coverage(entities):
    """Verifica se entidades críticas possuem lastro REAL em compliance/ ou research/."""
    missing = []
    # 🔒 Restringe busca APENAS às pastas de fonte (ignora inbox, ssot, economics)
    search_paths = [MARKET / "compliance", MARKET / "research"]
    
    for e in entities:
        found = False
        for search_dir in search_paths:
            if not search_dir.exists(): continue
            for p in search_dir.rglob("*.md"):
                # 1. Check por nome/arquivo (rápido)
                if e.lower() in p.stem.lower() or e.lower() in p.name.lower():
                    found = True; break
                # 2. Check por conteúdo (primeiros 1000 chars para performance)
                try:
                    text = p.read_text(encoding="utf-8", errors="ignore")[:1000].lower()
                    if e.lower() in text:
                        found = True; break
                except: continue
            if found: break
        if not found:
            missing.append(e)
    return missing

def update_inbox(missing):
    """Registra gaps detectados no MARKET_INBOX.md (uma linha por entidade)."""
    if not missing: return
    today = date.today().isoformat()
    
    new_entries = ""
    for e in missing:
        new_entries += f"| Integração {e} | `> Fonte: raw/docs_oficiais.md` | Crítica | 🔍 Pesquisa | {today}\n"
    
    if INBOX.exists():
        text = INBOX.read_text(encoding="utf-8")
        # Filtra entradas que já existem para evitar duplicatas
        final_entries = ""
        for line in new_entries.strip().split("\n"):
            if line.split("|")[1].strip() not in text:
                final_entries += line + "\n"
        
        if final_entries:
            INBOX.write_text(text.rstrip() + "\n" + final_entries, encoding="utf-8")
    else:
        header = "# MARKET INBOX\n| Gap | Fonte | Prioridade | Status | Data |\n|-----|-------|------------|--------|------|\n"
        INBOX.write_text(header + new_entries, encoding="utf-8")

def get_inception_status():
    """Lê o status do Inception mestre."""
    if not INCEPTION.exists(): return "MISSING"
    try:
        content = INCEPTION.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"

def main():
    print("[RUN] Spec Enricher (Gap Check & Strategy Sync)...")
    
    # Nova lógica de Onboarding Híbrido
    status = get_inception_status()
    vision_exists = (CONTEXT_DIR / "brain" / "VISION.md").exists()
    
    if status == "DRAFT":
        if vision_exists:
            print("[TRANSLATION_PENDING] Visão detectada. Solicite à IA: \"@spec-enricher proponha o INCEPTION.md\".")
            sys.exit(2)
        else:
            print("[ONBOARDING_MODE] Inception em DRAFT e sem VISION.md. Consulte START_HERE.md.")
            sys.exit(0)
            
    if status == "TRANSLATION_LOCK":
        print("[TRANSLATION_LOCK] INCEPTION.proposed.md gerado. Revise, renomeie e mude status para ACTIVE.")
        sys.exit(2)

    entities, scan_status = scan_entities()
    if scan_status != "OK":
        print(f"[ERROR] {scan_status}")
        sys.exit(1)

    missing = check_market_coverage(entities)
    if missing:
        update_inbox(missing)
        print(f"[ACTION] Gaps detectados: {', '.join(missing)}")
        print("[EXIT 2] Popule market/ e rode 'npm run context:enrich' novamente.")
        sys.exit(2)

    print("[OK] Market coverage validada. Pronto para cristalização do PRD.")
    sys.exit(0)

if __name__ == "__main__":
    main()

```
CHUNK_END id=e94b4e40315c_c001
FILE_END id=file_e94b4e40315c

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=377 bytes=13475 mtime=2026-04-23T15:09:13.334620+00:00 sha1=c76d3a65d6be246539305f89c25c0963f6184a60
CHUNK_START id=1edef35c2f56_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""
🛡️ harness_runner.py — Validação reativa de contratos (Harness Layer)
Valida spec vs schema, PRD vs código, e integridade de handoffs.
"""

import os, re, sys, json, io
from datetime import datetime
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(
        fmt
    )
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
JOURNAL = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SCHEMA = CONTEXT_DIR / "maintenance" / "schema.sql"
HARNESS_REG = CONTEXT_DIR / "brain" / "HARNESS_REGISTRY.md"
PRD = CONTEXT_DIR / "brain" / "PRD.md"
INCEPTION = CONTEXT_DIR / "brain" / "INCEPTION.md"


def check_schema_contract(spec_path):
    """Valida se campos/tabelas da spec existem no schema.sql"""
    if not spec_path.exists() or not SCHEMA.exists():
        return True, "Schema/spec indisponivel (skip)"
    spec_text = spec_path.read_text(encoding="utf-8")
    schema_text = SCHEMA.read_text(encoding="utf-8")
    tables_spec = set(re.findall(r"`(tabela|table)[\s_]+(\w+)", spec_text, re.I))
    tables_schema = set(
        re.findall(
            r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?[\"\']?(\w+)", schema_text, re.I
        )
    )

    # We only care about the table name captured in group 2 for specs if the matched syntax was used.
    # A robust extraction gets just the table name.
    spec_tnames = {t[1] for t in tables_spec}
    missing = spec_tnames - tables_schema
    if missing:
        return False, f"Spec pede tabelas inexistentes: {missing}"
    return True, "Schema contract OK"


def check_handoff_integrity(journal_text):
    """Verifica se handoffs recentes estao completos (suporta historico e padrao atual)"""
    fails = []

    # Previne loop: ignora linhas de log do próprio harness (- **Detalhe:** handoff: ...)
    clean_lines = [
        line
        for line in journal_text.splitlines()
        if "[HARNESS-" not in line and "Handoffs malformados:" not in line
    ]
    clean_text = "\n".join(clean_lines)

    # 1. Checa padrão legado: [handoff:...]
    legados = re.findall(r"\[handoff:(.*?)\]", clean_text, re.I)
    for h in legados:
        if h.count("|") < 2:
            fails.append(f"Legado incompleto: {h[:30]}")

    # 2. Checa padrão moderno: (🔄 )Handoff: RoleA -> RoleB | Info | Info
    modernos = re.findall(r"(?:🔄\s*)?Handoff:\s*(.*?)(?=\n|$)", clean_text, re.I)
    for h in modernos:
        if h.count("|") < 2:
            fails.append(f"Handoff incompleto: {h[:30]}")

    if fails:
        return False, f"Handoffs malformados: {fails}"
    return True, "Handoffs integros"


def check_strategic_alignment():
    if not INCEPTION.exists() or not PRD.exists():
        return True, "INCEPTION/PRD ausentes (skip estratégico)"
    prd_text = PRD.read_text(encoding="utf-8").lower()
    inception_text = INCEPTION.read_text(encoding="utf-8")
    boundaries = re.findall(r"^-\s*NUNCA:\s*(.+)$", inception_text, re.I | re.MULTILINE)
    violations = [
        b.strip()
        for b in boundaries
        if re.search(re.escape(b.strip().lower()), prd_text)
    ]
    if violations:
        return False, f"PRD viola boundaries estrategicas: {violations}"
    return True, "Strategic alignment OK"


def check_enrichment_integrity(prd_path: Path):
    """Valida seção Critical Dependencies semanticamente (bullet + Fonte: + market/)."""
    if not prd_path.exists():
        return True, "PRD ausente (skip)"
    text = prd_path.read_text(encoding="utf-8")
    text_lower = text.lower()

    # Só exige a seção se o PRD mencionar integrações, compliance ou APIs externas
    trigger_keywords = [
        "integração",
        "integracao",
        "integration",
        "compliance",
        "api externa",
        "external api",
        "stripe",
        "lgpd",
        "meta",
        "aws",
        "webhook",
    ]
    if not any(kw in text_lower for kw in trigger_keywords):
        return True, "Sem menção a integrações/compliance (skip)"

    section_match = re.search(
        r"^##\s*.*?Critical Dependencies.*?\n(.*?)(?=\n## |\Z)",
        text,
        re.I | re.DOTALL | re.MULTILINE,
    )
    if not section_match:
        return (
            False,
            "Seção Critical Dependencies obrigatória para PRDs com integrações/compliance",
        )

    deps_text = section_match.group(1)
    missing = []
    for line in deps_text.splitlines():
        line = line.strip()
        if line.startswith("-"):
            # Validação semântica: deve conter "Fonte:" e "market/"
            if "fonte:" not in line.lower() or "market/" not in line.lower():
                missing.append(line[:60])

    if missing:
        return False, f"Dependencies sem lastro em market/: {missing}"
    return True, "Enrichment contract OK"


def check_sprint_contract(spec_path: Path):
    """Valida se a spec possui contrato explícito e assinatura do QA."""
    if not spec_path.exists():
        return (
            False,
            "Nenhuma Spec ativa detectada. Commits sem Spec validada no The Workshop estão PROIBIDOS.",
        )

    text = spec_path.read_text(encoding="utf-8")
    # Extrai bloco YAML entre --- e ---
    yaml_match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not yaml_match:
        return False, "Bloco de contrato (---) ausente no topo da spec"

    contract = yaml_match.group(1)

    # Validação semântica leve (stdlib-only)
    has_dod = "definition_of_done:" in contract
    has_signoff = re.search(r"qa_signoff:\s*true", contract, re.I)
    has_signed_by = re.search(r'signed_by:\s*["\']?@qa-validator["\']?', contract, re.I)

    if not has_dod:
        return False, "Campo definition_of_done obrigatório"
    if not has_signoff:
        return False, "Contrato não assinado pelo @qa-validator (qa_signoff: false)"
    if not has_signed_by:
        return False, "Campo signed_by inválido ou ausente"

    # Regra v2.5.2: segregação de contexto para specs standard
    type_match = re.search(r'^\s*type:\s*["\']?(\w+)["\']?\s*$', contract, re.I | re.M)
    spec_type = type_match.group(1).strip().lower() if type_match else None

    if spec_type == "standard":
        exec_match = re.search(
            r"^\s*executor_context_id:\s*(.+?)\s*$", contract, re.I | re.M
        )
        valid_match = re.search(
            r"^\s*validator_context_id:\s*(.+?)\s*$", contract, re.I | re.M
        )

        executor_id = (
            exec_match.group(1).strip().strip('"').strip("'") if exec_match else ""
        )
        validator_id = (
            valid_match.group(1).strip().strip('"').strip("'") if valid_match else ""
        )

        missing_tokens = {"", "null", "none"}
        if (
            executor_id.lower() in missing_tokens
            or validator_id.lower() in missing_tokens
        ):
            return (
                False,
                "Spec standard requer executor_context_id e validator_context_id preenchidos",
            )

        if executor_id == validator_id:
            return (
                False,
                "Spec standard requer segregação: executor_context_id deve ser diferente de validator_context_id",
            )

    return True, "Sprint contract validado e assinado"


def log_harness(status, detail, spec_name="unknown"):
    """Registra no JOURNAL.md de forma compacta e atomica"""
    entry = f"\n## [HARNESS-{status.upper()}] Report | spec:{spec_name}\n- **Detalhe:** {detail}\n"
    try:
        tmp = JOURNAL.with_suffix(".tmp")
        content = (
            JOURNAL.read_text(encoding="utf-8")
            if JOURNAL.exists()
            else "# JOURNAL.md\n"
        )
        tmp.write_text(content + entry, encoding="utf-8")
        tmp.replace(JOURNAL)
    except Exception as e:
        print(f"[WARN] Falha ao logar harness: {e}")


def update_state_md(spec_dir: Path, status: str, detail: str = ""):
    state = spec_dir / "STATE.md"
    if not state.exists():
        return
    content = f"---\nstatus: {status}\nupdated: {format_ts()}\ndetail: {detail}\n---\n"
    tmp = state.with_suffix(".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(state)
    status_print = status.replace("✅", "[OK]").replace("❌", "[FAIL]")
    print(f"[STATE.md] -> {status_print} na spec {spec_dir.name}")


def get_inception_status():
    """Lê o status do Inception mestre."""
    if not INCEPTION.exists():
        return "MISSING"
    try:
        content = INCEPTION.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"


def main():
    # 0. Verificação de Estado (Hybrid Discovery)
    status = get_inception_status()
    if status == "DRAFT":
        root = CONTEXT_DIR.parent
        code_exts = {
            ".py",
            ".js",
            ".jsx",
            ".ts",
            ".tsx",
            ".go",
            ".rs",
            ".java",
            ".kt",
            ".cs",
            ".php",
        }
        ignore_names = {".gitkeep", ".keep"}
        ignore_prefixes = ("README",)
        ignore_dirs = {"node_modules", ".git", ".venv", "__pycache__", "dist", "build"}

        def has_real_code_activity():
            for code_root in ["src", "app", "packages", "services", "lib"]:
                base = root / code_root
                if not base.exists() or not base.is_dir():
                    continue
                for cur, dirs, files in os.walk(base):
                    dirs[:] = [d for d in dirs if d not in ignore_dirs]
                    for fname in files:
                        if fname in ignore_names:
                            continue
                        if fname.startswith(ignore_prefixes):
                            continue
                        path = Path(cur) / fname
                        if path.suffix.lower() in code_exts and path.stat().st_size > 0:
                            return True
            return False

        def has_real_spec_activity():
            specs_dir = root / ".specs" / "features"
            if not specs_dir.exists() or not specs_dir.is_dir():
                return False
            for spec in specs_dir.iterdir():

```
CHUNK_END id=1edef35c2f56_c001
CHUNK_START id=1edef35c2f56_c002 start_line=301 end_line=377
```python
                if not spec.is_dir() or spec.name.startswith("_"):
                    continue
                spec_file = spec / "spec.md"
                state_file = spec / "STATE.md"
                if (
                    spec_file.exists()
                    and state_file.exists()
                    and spec_file.stat().st_size > 0
                ):
                    return True
            return False

        if has_real_code_activity() or has_real_spec_activity():
            print(
                "[FATAL] Projeto possui atividade real (código/specs) mas INCEPTION.md está em DRAFT."
            )
            print(
                "[DICA] Ative a governança: altere status para ACTIVE em INCEPTION.md."
            )
            sys.exit(1)

        print("[INFO] Modo Onboarding (DRAFT). Bypass permitido até ativação.")
        sys.exit(0)

    # 1. Definindo a pasta spec ativa
    features_dir = CONTEXT_DIR.parent / ".specs" / "features"
    spec_dir_env = os.environ.get("ACTIVE_SPEC")

    if spec_dir_env and (features_dir / spec_dir_env).exists():
        spec_dir = features_dir / spec_dir_env
    else:
        # Fallback: spec modificada mais recentemente
        if features_dir.exists():
            active = sorted(
                [
                    d
                    for d in features_dir.iterdir()
                    if d.is_dir() and not d.name.startswith("_")
                ],
                key=os.path.getmtime,
                reverse=True,
            )
            spec_dir = active[0] if active else None
        else:
            spec_dir = None

    spec_name = spec_dir.name if spec_dir else "manual"
    spec_path = spec_dir / "spec.md" if spec_dir else Path("dummy")

    checks = {
        "schema": check_schema_contract(spec_path),
        "handoff": check_handoff_integrity(
            JOURNAL.read_text(encoding="utf-8") if JOURNAL.exists() else ""
        ),
        "strategy": check_strategic_alignment(),
        "enrichment": check_enrichment_integrity(PRD),
        "sprint_contract": check_sprint_contract(spec_path),
    }

    fails = [f"{k}: {v[1]}" for k, v in checks.items() if not v[0]]
    if fails:
        detail = " | ".join(fails)
        log_harness("fail", detail, spec_name)
        if spec_dir:
            update_state_md(spec_dir, "❌ FAILED", detail)
        print(f"[ERROR] Harness fail: {detail}")
        sys.exit(1)

    log_harness("pass", "All contracts valid", spec_name)
    if spec_dir:
        update_state_md(spec_dir, "✅ PASSED", "All checks passed")
    print("[OK] Harness pass: Contracts validated.")
    sys.exit(0)


if __name__ == "__main__":
    main()

```
CHUNK_END id=1edef35c2f56_c002
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=111 bytes=4132 mtime=2026-04-12T03:40:11.302253+00:00 sha1=1f23d31d0c88fe19ee916b4d6dd9676fb2f0018b
CHUNK_START id=a642d240b9ab_c001 start_line=1 end_line=111
```python
#!/usr/bin/env python3
"""
📊 health_sync.py — Atualizador Dinâmico do Dashboard (Fase 2)
Gera a tabela de métricas em CONTEXT_HEALTH.md baseada na realidade física do repositório.
"""
import re, sys, os
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

CONTEXT_DIR = Path(__file__).resolve().parents[1]
HEALTH_PATH = CONTEXT_DIR / "monitoring" / "CONTEXT_HEALTH.md"
JOURNAL_PATH = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
SCHEMA_PATH = CONTEXT_DIR / "maintenance" / "schema.sql"

def count_journal_metrics():
    if not JOURNAL_PATH.exists(): return 0, 0, "No Data"
    text = JOURNAL_PATH.read_text(encoding="utf-8")
    lines = len(text.splitlines())
    chars = len(text)
    
    # Busca a última entrada do Harness
    harness_matches = re.findall(r'\[HARNESS-(FAIL|PASS)\]', text)
    last_harness = harness_matches[-1] if harness_matches else "N/A"
    
    return lines, chars, last_harness

def count_schema_tables():
    if not SCHEMA_PATH.exists(): return 0
    text = SCHEMA_PATH.read_text(encoding="utf-8")
    tables = re.findall(r'CREATE\s+TABLE', text, re.I)
    return len(tables)

def count_pending_migrations():
    mig_dir = CONTEXT_DIR / "maintenance" / "migrations"
    if not mig_dir.exists(): return 0
    return len(list(mig_dir.glob("*.sql")))

def estimate_tokens():
    total_chars = 0
    # Vasculha todos os arquivos do contexto
    for root, _, files in os.walk(CONTEXT_DIR):
        for file in files:
            p = Path(root) / file
            if p.suffix in {'.md', '.py', '.sql', '.sh'}:
                try:
                    total_chars += len(p.read_text(encoding="utf-8"))
                except: pass
    return total_chars // 4

def update_dashboard():
    j_lines, j_chars, harness = count_journal_metrics()
    tables = count_schema_tables()
    tokens = estimate_tokens()
    migs = count_pending_migrations()
    
    now = format_ts()
    
    # Determinar status heurísticos
    lines_status = "[OK]" if j_lines < 550 else "[WARN] Limpar!"
    chars_status = "[OK]" if j_chars < 45000 else "[WARN] Pesado"
    tokens_status = "[OK]" if tokens < 100000 else "[WARN] Context Bloat"
    harness_status = f"[{harness}]" if harness != "N/A" else "N/A"
    migs_status = f"{migs} file(s)" if migs > 0 else "N/A"
    
    table_content = f"""<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Manutencao** | | | | |
| Linhas do Journal | {j_lines} | 600 | Tracker | {lines_status} |
| Carga do Journal | {j_chars // 1000}k chars | 50k chars | Tracker | {chars_status} |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~{tokens // 1000}k | 128k (Max) | Eficiencia | {tokens_status} |
| **Consistencia** | | | | |
| Tabelas no Schema | {tables} | N/A | DB-First | [OK] |
| Migrations Pendentes | {migs_status} | N/A | DB-First | [OK] |
| Ultimo Harness | Role Check | Pass/Fail | Integridade | {harness_status} |
| Ultima Sincronia | {now} | Real-Time | Automacao | [OK] |
<!-- HEALTH_TABLE_END -->"""

    # Ler o arquivo atual e substituir a tabela usando regex
    if not HEALTH_PATH.exists():
        print(f"[ERROR] {HEALTH_PATH.name} não encontrado.")
        return
        
    content = HEALTH_PATH.read_text(encoding="utf-8")
    new_content = re.sub(
        r'<!-- HEALTH_TABLE_START -->.*?<!-- HEALTH_TABLE_END -->',
        table_content,
        content,
        flags=re.DOTALL
    )
    
    # Atualizar metadado de update se existir
    new_content = re.sub(
        r'(Última Atualização:|Ultima Atualizacao:).*',
        f'Ultima Atualizacao: {now}',
        new_content
    )
    
    HEALTH_PATH.write_text(new_content, encoding="utf-8")
    print(f"[OK] {HEALTH_PATH.name} atualizado (Tokens: ~{tokens//1000}k, Linhas: {j_lines}).")

if __name__ == "__main__":
    update_dashboard()

```
CHUNK_END id=a642d240b9ab_c001
FILE_END id=file_a642d240b9ab

---
<a id="file_0731dcfd7873"></a>
FILE_START id=file_0731dcfd7873 path=.context/_scripts/ingest_wiki_guard.py domain=source lang=python lines=88 bytes=3112 mtime=2026-04-22T23:34:30.558813+00:00 sha1=8cf96a678ced2d689deb51608c115dcd75a632a8
CHUNK_START id=0731dcfd7873_c001 start_line=1 end_line=88
```python
#!/usr/bin/env python3
"""
🛡️ ingest_wiki_guard.py — Guardião de Ingestão Wiki (H.O.K v2.5)
Valida conformidade Karpathy antes de permitir a entrada de novos artigos.
"""
import re, sys, os
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
WIKI_DIR = CONTEXT_DIR / "market/WIKI"

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

    print(f"✅ Todos os {len(articles)} artigos WIKI estão em conformidade.")
    filenames = [a.name for a in articles]
    append_to_wiki_log("INGEST", f"Ingestão de {len(articles)} artigos", ", ".join(filenames), "OK")
    sys.exit(0)

if __name__ == "__main__":
    # Garante UTF-8 no Windows
    if sys.platform == "win32":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()

```
CHUNK_END id=0731dcfd7873_c001
FILE_END id=file_0731dcfd7873

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=116 bytes=4999 mtime=2026-04-22T23:34:42.090035+00:00 sha1=844cbc05474f73fa7addd3038fbbc60b86ab460a
CHUNK_START id=ab41b07fb3fb_c001 start_line=1 end_line=116
```python
#!/usr/bin/env python3
"""
📖 lint_wiki.py — Validacao Epistemologica (Karpathy Layer v2.5)
Enforce de rastreabilidade mandatória para a Wiki de Mercado.
"""
import sys
import re
import argparse
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]

# Import utilitário de log
sys.path.append(str(CONTEXT_DIR / "_scripts"))
try:
    from _wiki_log_utils import append_to_wiki_log
except ImportError:
    def append_to_wiki_log(*args): pass
# RAW centralizado na nova estrutura Fase 3
RAW_DIR = CONTEXT_DIR / "market" / "RAW"
# Diretórios de Wiki (Adicionada a nova market/WIKI)
WIKI_DIRS = [CONTEXT_DIR / "brain", CONTEXT_DIR / "maintenance", CONTEXT_DIR / "market" / "WIKI"]

# Regex para capturar claims técnicos
CLAIM_REGEX = re.compile(
    r'^(?![\s\-\*#>])'
    r'([A-ZÁÉÍÓÚÂÊÎÔÛÃÕÇ][a-záéíóúâêîôûãõç\s,]{15,}'
    r'(?:utiliza|implementa|segue|requer|garante|valida|integra|usa|e|é)\s'
    r'.+?\.)',
    re.MULTILINE
)

def find_raw_sources():
    """Lista arquivos na inbox RAW para sugestão."""
    if not RAW_DIR.exists(): return []
    return [f.name for f in RAW_DIR.iterdir() if f.suffix == '.md']

def suggest_source(claim_text, raw_files):
    """Heurística simples: busca palavras-chave do claim nos nomes dos arquivos RAW."""
    words = set(re.findall(r'\b\w{5,}\b', claim_text.lower()))
    ignore = {'deve', 'como', 'para', 'sistema', 'projeto', 'este', 'esta', 'ser', 'com', 'sobre'}
    words -= ignore
    if not words: return None
    
    matches = []
    for raw_file in raw_files:
        if any(w in raw_file.lower() for w in words):
            matches.append(f"RAW/{raw_file}")
    return matches[0] if matches else None

def check_wiki(strict=False):
    """Varre a wiki em busca de claims sem citação."""
    raw_files = find_raw_sources()
    issues = []
    
    for d in WIKI_DIRS:
        if not d.exists(): continue
        for f in d.rglob("*.md"):
            if "_archive" in str(f) or "lint_report" in str(f) or f.name.startswith("_"): continue
            
            text = f.read_text(encoding="utf-8")
            if f.name in ["README.md", "MASTER_FLOW.md", "RULES.md", "CONTEXT_HEALTH.md", "rebuild_guide.md"]: continue

            # 🛠️ REGRA MANDATÓRIA KARPATHY (v2.5)
            # Se o arquivo está em market/WIKI, ele DEVE seguir o schema Nível 2
            if "market" in str(f) and "WIKI" in str(f):
                if "> Fonte: RAW/" not in text and "> Fonte: market/RAW/" not in text:
                    issues.append(f"[FATAL] [{f.name}] Wiki de Mercado sem citação RAW obrigatória.")
                
                if strict:
                    # Check de Frontmatter Básico
                    if not re.search(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL):
                        issues.append(f"[FATAL] [{f.name}] Frontmatter ausente ou inválido.")
                    
                    # Check de Estrutura
                    if "## Key Takeaways" not in text:
                        issues.append(f"[FATAL] [{f.name}] Seção '## Key Takeaways' ausente.")
                    
                    if "## Related" not in text and "[[" not in text:
                        issues.append(f"[FATAL] [{f.name}] Conectividade ausente (Related ou [[links]]).")

            # Checagem de claims (Geral)
            for match in CLAIM_REGEX.finditer(text):
                claim = match.group(0)
                context_window = text[max(0, match.start() - 150):min(len(text), match.start() + 250)]
                if "> Fonte:" not in context_window and "> Fonte:" not in text and "SSOT" not in text:
                    suggestion = suggest_source(claim, raw_files)
                    error_msg = f"[WARN] [{f.name}] Claim sem fonte: '{claim[:50]}...'"
                    if suggestion: error_msg += f"\n   [DICA] Sugestao: Adicione '> Fonte: {suggestion}'"
                    issues.append(error_msg)

    if issues:
        print("\n[LINT] Wiki Report:")
        print("\n".join(issues))
        # Se houver erro FATAL na WIKI, trava independente do strict-mode
        has_fatal = any("[FATAL]" in i for i in issues)
        status = "FAIL" if (strict or has_fatal) else "WARN"
        
        append_to_wiki_log("LINT", f"Detectados {len(issues)} problemas", "-", status)
        
        if strict or has_fatal:
            print("\n[FATAL] Pipeline bloqueado por integridade epistemológica.")
            sys.exit(1)
        else:
            print("\n[WARN] Verifique as citacoes pendentes.")
            sys.exit(0)
    else:
        print("[OK] Wiki limpa: Epistemologia em dia.")
        append_to_wiki_log("LINT", "Integridade epistemológica validada", "-", "OK")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint de Karpathy Layer")
    parser.add_argument("--strict", action="store_true", help="Bloqueia o pipeline")
    args = parser.parse_args()
    check_wiki(strict=args.strict)

```
CHUNK_END id=ab41b07fb3fb_c001
FILE_END id=file_ab41b07fb3fb

---
<a id="file_d65b48a9d56c"></a>
FILE_START id=file_d65b48a9d56c path=.context/_scripts/migration_registry.py domain=source lang=python lines=44 bytes=1700 mtime=2026-04-12T02:18:47.875961+00:00 sha1=a1e9beb894aba2b44931e9c41522a020b7359ebf
CHUNK_START id=d65b48a9d56c_c001 start_line=1 end_line=44
```python
#!/usr/bin/env python3
"""
🗂️ migration_registry.py — Registro e Auditoria de Esquemas DB-First
Força os agentes a respeitar a ordem incremental de manipulação estrutural de banco.
"""
import re, sys
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
MIG_DIR = CONTEXT_DIR / "maintenance" / "migrations"
SCHEMA = CONTEXT_DIR / "maintenance" / "schema.sql"

def validate():
    print("[RUN] Executando Registro de Migrations...")
    
    if not MIG_DIR.exists():
        print("[WARN] migrations/ ausente. Ignorando (modo snapshot).")
        return
    
    files = sorted(MIG_DIR.glob("*.sql"))
    if not files:
        print("[OK] Nenhuma migration pendente.")
        return

    # 1. Convenção estrita (001_*.sql)
    for i, f in enumerate(files, 1):
        if not re.match(rf"^{i:03d}_.*\.sql$", f.name):
            print(f"[FATAL] Migration fora de ordem ou padrao invalido: {f.name}")
            print(f"💡 Esperado: {i:03d}_nome_da_migration.sql")
            sys.exit(1)

    # 2. Integridade Heurística vs Schema
    if SCHEMA.exists():
        last_mig = files[-1]
        schema_content = SCHEMA.read_text(encoding="utf-8")
        if last_mig.name not in schema_content and "-- Last migration:" not in schema_content:
            print(f"[WARN] schema.sql pode estar desatualizado! Ultima migration: {last_mig.name}")
            print("[DICA] Apos rodar o SQL, rode 'npm run context:sync' com a string da ultima migration no topo do schema.")
            # Nao aborta o pipe, apenas educa a I.A e o Dev.
    
    print(f"[OK] Migrations validas: {len(files)} detectadas. Arquitetura DB-First OK.")

if __name__ == "__main__":
    validate()

```
CHUNK_END id=d65b48a9d56c_c001
FILE_END id=file_d65b48a9d56c

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=82 bytes=2761 mtime=2026-04-12T02:48:42.689091+00:00 sha1=8b12ecb77b7b91c035a2d7c9752910c71064d1e5
CHUNK_START id=024b28a37d29_c001 start_line=1 end_line=82
```python
#!/usr/bin/env python3
"""
🗜️ purge_journal.py
Arquiva 70% das entradas mais antigas do JOURNAL.md.
Mantém 30% mais recentes como semente. Backup automático e escrita atômica.
"""
import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
JOURNAL_FILE = CONTEXT_DIR / "maintenance" / "JOURNAL.md"
ARCHIVE_DIR = CONTEXT_DIR / "maintenance" / "_archive_context" / "journals"
KEEP_RATIO = 0.3  # 30% mais recentes

def parse_entries(content):
    # Divide por headers markdown (## 📅, ##, etc.) mantendo o header na entrada
    parts = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    return [p.strip() for p in parts if p.strip()]

def purge_journal():
    if not JOURNAL_FILE.exists():
        print("[WARN] JOURNAL.md nao encontrado. Nada a fazer.")
        return

    content = JOURNAL_FILE.read_text(encoding="utf-8")
    entries = parse_entries(content)

    if len(entries) <= 1:
        print("[INFO] Poucas entradas para purgar.")
        return

    keep_count = max(1, int(len(entries) * KEEP_RATIO))
    archive_entries = entries[:-keep_count]
    keep_entries = entries[-keep_count:]

    # Garante diretório de arquivo
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    # Backup com timestamp
    timestamp = format_ts(fmt="%Y%m%d_%H%M%S")
    archive_file = ARCHIVE_DIR / f"journal_archive_{timestamp}.md"
    archive_content = f"# Arquivo de Journal - {timestamp}\n\n" + "\n\n".join(archive_entries) + "\n"
    archive_file.write_text(archive_content, encoding="utf-8")

    # Nova semente
    now = format_ts()
    seed = f"""---
Criado em: {now}
Ultima Atualizacao: {now}
Status: Ativo
Nota: Semente pos-purge. {len(archive_entries)} entradas arquivadas em {archive_file.name}.
---

# JOURNAL.md (Memoria Contínua)
> Mantido por purge_journal.py. Limite heuristico de caracteres atingido.

""" + "\n\n".join(keep_entries) + "\n"

    # Escrita atomica (previne corrupcao se interrupcao ocorrer)
    temp_file = JOURNAL_FILE.with_suffix(".tmp")
    temp_file.write_text(seed, encoding="utf-8")
    temp_file.replace(JOURNAL_FILE)

    print(f"[OK] Purge concluido.")
    print(f"[OK] Arquivadas: {len(archive_entries)} entradas -> {archive_file.name}")
    print(f"[OK] Mantidas: {len(keep_entries)} entradas mais recentes.")

if __name__ == "__main__":
    try:
        purge_journal()
    except Exception as e:
        print(f"[ERROR] Erro no purge: {e}")

```
CHUNK_END id=024b28a37d29_c001
FILE_END id=file_024b28a37d29

---
<a id="file_e98b95e5fb6d"></a>
FILE_START id=file_e98b95e5fb6d path=.context/_scripts/secrets_scanner.py domain=source lang=python lines=69 bytes=2622 mtime=2026-04-14T12:47:41.549578+00:00 sha1=f73abf4fe2fa1a6e146de3fefae50c9016b77045
CHUNK_START id=e98b95e5fb6d_c001 start_line=1 end_line=69
```python
#!/usr/bin/env python3
"""
🔐 secrets_scanner.py — Scanner Nativo de Segredos (Inclui JSON com Allowlist)
Usa git ls-files para performance O(N) e filtra falsos positivos.
"""
import re, sys, subprocess, os
from pathlib import Path

CONTEXT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = CONTEXT_DIR.parent
ALLOWLIST_FILE = ROOT_DIR / ".secrets-allowlist"
ALLOWLIST = ALLOWLIST_FILE.read_text(encoding="utf-8").splitlines() if ALLOWLIST_FILE.exists() else []

# Arquivos JSON seguros para ignorar
JSON_ALLOWLIST = {"package.json", "package-lock.json", "tsconfig.json", "vercel.json", "next.config.js"}

SECRET_PATTERNS = [
    re.compile(r"(sk|pk|rk)_(live|test)_[a-zA-Z0-9]{20,}", re.I),
    re.compile(r"whsec_[a-zA-Z0-9]{24,}", re.I),
    re.compile(r"supabase_(key|url)\s*[:=]\s*[\"']?\S{10,}[\"']?", re.I),
    re.compile(r"(AIzaSy|AKIAIOSFODNN7EXAMPLE)\w*", re.I),
    re.compile(r"(NEXT_PUBLIC_|VITE_|REACT_APP_)\w*\s*=\s*[\"']?\S{8,}[\"']?", re.I),
]

def get_files_to_scan():
    try:
        res = subprocess.run(["git", "ls-files"], cwd=ROOT_DIR, capture_output=True, text=True, check=True)
        return [ROOT_DIR / f for f in res.stdout.splitlines()]
    except Exception:
        safe_dirs = ["src", "api", "config", ".context"]
        files = []
        for d in safe_dirs:
            p = ROOT_DIR / d
            if p.exists():
                # Inclui .json agora
                files.extend(p.rglob("*.*"))
        return files

def scan():
    hits = []
    print("[RUN] Executando Scanner de Segredos...")
    for f in get_files_to_scan():
        if not f.is_file(): continue
        # Pula imagens e lockfiles
        if f.suffix in {".lock", ".png", ".jpg", ".md"}: continue
        # Pula JSONs de configuração conhecidos
        if f.suffix == ".json" and f.name in JSON_ALLOWLIST: continue
        
        try:
            content = f.read_text(encoding="utf-8", errors="ignore")
        except Exception: continue

        for pat in SECRET_PATTERNS:
            for m in pat.finditer(content):
                val = m.group(0)
                if any(aw.lower() in val.lower() for aw in ALLOWLIST): continue
                if re.search(r'EXAMPLE|YOUR_|CHANGE_ME|test_', val, re.I): continue
                hits.append(f"🔒 [{f.relative_to(ROOT_DIR)}]: '{val[:15]}...'")
    
    if hits:
        print("\n[FATAL] SECRET SCAN FAILED:")
        print("\n".join(hits))
        print("\n💡 Dica: Use .env e .gitignore. Adicione excecoes legitimas em .secrets-allowlist")
        sys.exit(1)
        
    print("[OK] Secret scan clean.")

if __name__ == "__main__":
    scan()

```
CHUNK_END id=e98b95e5fb6d_c001
FILE_END id=file_e98b95e5fb6d

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=102 bytes=3426 mtime=2026-04-12T02:48:59.755191+00:00 sha1=d2b0f3541ccaab8c75f381f47d539c762618a0b7
CHUNK_START id=f122711ba9e1_c001 start_line=1 end_line=102
```python
#!/usr/bin/env python3
"""
🔄 sync_project.py
Sincroniza TECH_REQUIREMENTS.md com package.json e schema.sql.
Usa marcadores <!-- AUTO-SYNC START/END --> para preservar edicoes humanas.
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from _tz_utils import format_ts
except ImportError:
    format_ts = lambda dt=None, fmt="%Y-%m-%d %H:%M": (dt or datetime.now()).strftime(fmt)
    print("[WARN] _tz_utils inacessivel. Usando timezone local MS-WIN.")

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent
REQ_FILE = CONTEXT_DIR / "maintenance" / "TECHNICAL_REQUIREMENTS.md"
PKG_FILE = CONTEXT_DIR.parent / "package.json"
SCHEMA_FILE = CONTEXT_DIR / "maintenance" / "schema.sql"

AUTO_START = "<!-- AUTO-SYNC START -->"
AUTO_END = "<!-- AUTO-SYNC END -->"

def get_package_deps():
    if not PKG_FILE.exists(): return {"dependencies": {}, "devDependencies": {}}
    try:
        with open(PKG_FILE, 'r', encoding='utf-8') as f:
            pkg = json.load(f)
        return {
            "dependencies": pkg.get("dependencies", {}),
            "devDependencies": pkg.get("devDependencies", {})
        }
    except Exception as e:
        print(f"[WARN] Erro ao ler package.json: {e}")
        return {"dependencies": {}, "devDependencies": {}}

def get_schema_tables():
    if not SCHEMA_FILE.exists(): return []
    content = SCHEMA_FILE.read_text(encoding="utf-8")
    # Regex para extrair nomes de tabelas
    return list(set(re.findall(r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?["\']?(\w+)["\']?', content, re.IGNORECASE)))

def sync_requirements():
    deps = get_package_deps()
    tables = get_schema_tables()
    now = format_ts()

    block = [
        AUTO_START,
        f"*🤖 Atualizado automaticamente em {now}*",
        ""
    ]

    if deps.get("dependencies"):
        block.append("### Dependencias (package.json)")
        for dep, ver in deps["dependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if deps.get("devDependencies"):
        block.append("### DevDependencies")
        for dep, ver in deps["devDependencies"].items():
            block.append(f"- `{dep}`: `{ver}`")
        block.append("")

    if tables:
        block.append("### Tabelas no Schema (schema.sql)")
        for t in sorted(tables):
            block.append(f"- `{t}`")
        block.append("")

    block.append(AUTO_END)
    auto_content = "\n".join(block) + "\n"

    if not REQ_FILE.exists():
        REQ_FILE.write_text(f"# TECHNICAL_REQUIREMENTS.md\n\n{auto_content}", encoding="utf-8")
        print("[OK] TECHNICAL_REQUIREMENTS.md criado.")
        return

    content = REQ_FILE.read_text(encoding="utf-8")
    start_idx = content.find(AUTO_START)
    end_idx = content.find(AUTO_END)

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + auto_content + content[end_idx + len(AUTO_END):]
    else:
        new_content = content.rstrip() + "\n\n" + auto_content

    REQ_FILE.write_text(new_content, encoding="utf-8")
    print("[OK] TECHNICAL_REQUIREMENTS.md sincronizado.")
    print(f"[OK] {len(deps.get('dependencies', {}))} deps | {len(tables)} tabelas detectadas.")

if __name__ == "__main__":
    try:
        sync_requirements()
    except Exception as e:
        print(f"[ERROR] Erro no sync: {e}")

```
CHUNK_END id=f122711ba9e1_c001
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=253 bytes=8091 mtime=2026-04-22T23:17:08.680799+00:00 sha1=c24e8617c984749da6e65e550b43cf786c4c913c
CHUNK_START id=1077e9084ea1_c001 start_line=1 end_line=253
```python
#!/usr/bin/env python3
"""
🔍 validate_context.py
Verifica saude do .context, estima consumo de tokens e valida conformidade.
Retorna exit 1 se houver qualquer alerta ou erro.
"""

import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONTEXT_DIR = SCRIPT_DIR.parent

# Forçar UTF-8 em Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

REQUIRED_FILES = [
    "brain/RULES.md",
    "brain/MASTER_FLOW.md",
    "brain/AGENT_REGISTRY.md",
    "brain/PRD.md",
    "maintenance/JOURNAL.md",
    "maintenance/schema.sql",
    "maintenance/TECHNICAL_REQUIREMENTS.md",
]

OPTIONAL_FILES = ["brain/INCEPTION.md"]


JOURNAL_MAX_LINES = 600
TOKEN_WARN_THRESHOLD_CHARS = 400_000


def check_files():
    return [f for f in REQUIRED_FILES if not (CONTEXT_DIR / f).exists()]


def check_journal_lines():
    journal = CONTEXT_DIR / "maintenance/JOURNAL.md"
    if not journal.exists():
        return 0, True
    lines = journal.read_text(encoding="utf-8").splitlines()
    return len(lines), len(lines) <= JOURNAL_MAX_LINES


def estimate_tokens():
    total_chars = 0
    for f in REQUIRED_FILES:
        path = CONTEXT_DIR / f
        if path.exists():
            total_chars += len(path.read_text(encoding="utf-8", errors="ignore"))
    tokens_raw = total_chars // 4
    return total_chars, tokens_raw, total_chars < TOKEN_WARN_THRESHOLD_CHARS


def check_registry_structure():
    registry = CONTEXT_DIR / "brain/AGENT_REGISTRY.md"
    if not registry.exists():
        return False, "Arquivo ausente"
    content = registry.read_text(encoding="utf-8")
    if "| Role | " not in content and "| Role " not in content:
        return False, "Tabela de roles nao encontrada"
    return True, "OK"


def check_specs_structure():
    specs_dir = CONTEXT_DIR.parent / ".specs"
    if not specs_dir.exists():
        return True, "Workshop inativo (OK)"
    features_dir = specs_dir / "features"
    if not features_dir.exists():
        return False, "Diretorio features ausente no .specs"
    active_specs = [
        d for d in features_dir.iterdir() if d.is_dir() and not d.name.startswith("_")
    ]
    for spec in active_specs:
        if not (spec / "STATE.md").exists():
            return False, f"Falha de integridade: {spec.name}/STATE.md ausente"
    return True, f"OK ({len(active_specs)} specs ativas)"


def get_inception_metadata():
    """Lê metadados do Inception."""
    path = CONTEXT_DIR / "brain" / "INCEPTION.md"
    if not path.exists():
        return None
    try:
        content = path.read_text(encoding="utf-8")
        metadata = {}
        for line in content.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip().split("#")[0].strip()
        return metadata
    except:
        return {}


def check_wiki_integrity():
    """Verifica se a infraestrutura base da WIKI Nível 2 existe."""
    index_file = CONTEXT_DIR / "market/WIKI/_index.md"
    log_file = CONTEXT_DIR / "market/wiki_log.md"
    
    if not index_file.exists():
        return False, "Índice mestre market/WIKI/_index.md ausente."
    if index_file.stat().st_size < 50:
        return False, "Índice mestre market/WIKI/_index.md parece estar vazio ou incompleto."
    if not log_file.exists():
        return False, "Log de transações market/wiki_log.md ausente."
        
    return True, "Estrutura Wiki OK"


def is_non_initial_context():
    """Detecta se o projeto já avançou além do estágio de onboarding."""
    # Critério sugerido pela auditoria: lista de code roots
    code_roots = ["src", "app", "packages", "services", "lib"]
    root_dir = CONTEXT_DIR.parent

    # 1. Verifica pastas de código
    for dr in code_roots:
        path = root_dir / dr
        if path.exists() and any(path.iterdir()):
            return True, f"Pasta de código ativa encontrada: {dr}/"

    # 2. Verifica .specs/features/ ativos
    specs_dir = root_dir / ".specs" / "features"
    if specs_dir.exists():
        active_specs = [d for d in specs_dir.iterdir() if d.is_dir()]
        if active_specs:
            return True, f"Especificações de feature ativas: {len(active_specs)}"

    return False, "Contexto inicial limpo"


def validate():
    print("--- Iniciando validação de contexto (v2.5.0 Hardened + Hybrid) ---")
    issues = []
    exit_code = 0

    missing = check_files()
    if missing:
        issues.append(f"[ERROR] Arquivos ausentes: {', '.join(missing)}")
    else:
        print("[OK] Todos os arquivos obrigatórios presentes.")

    # Inteligência de Onboarding & Inception
    vision_exists = (CONTEXT_DIR / "brain" / "VISION.md").exists()
    metadata = get_inception_metadata()
    inception_status = metadata.get("status") if metadata else None
    is_dirty, dirty_msg = is_non_initial_context()

    if inception_status == "DRAFT":
        if vision_exists:
            print(
                "[WARN] Tradução Pendente: VISION.md detectada. Solicite @spec-enricher."
            )
            exit_code = 2
        elif is_dirty:
            issues.append(
                f"[FATAL] Inception em DRAFT mas projeto possui código ({dirty_msg})."
            )
            exit_code = 1
        else:
            print(f"[INFO] Modo Onboarding: Projeto limpo. Consulte START_HERE.md.")
            exit_code = 0
    elif inception_status == "TRANSLATION_LOCK":
        print(
            "[WARN] Bloqueio de Tradução: INCEPTION.proposed.md aguardando ratificação."
        )
        exit_code = 2
    elif inception_status == "ACTIVE":
        print("[OK] Governança ACTIVE: Limites validados.")
        exit_code = 0
    elif inception_status is not None:
        issues.append(f"[ERROR] Status de Inception inválido: {inception_status}")
        exit_code = 1

    spec_ok, spec_msg = check_specs_structure()
    if not spec_ok:
        issues.append(f"[WARN] .specs/: {spec_msg}")
        if exit_code == 0:
            exit_code = 1
    else:
        print(f"[OK] .specs/: {spec_msg}")

    journal_lines, journal_ok = check_journal_lines()
    if not journal_ok:
        issues.append(
            f"[WARN] JOURNAL.md excede limite: {journal_lines}/{JOURNAL_MAX_LINES}"
        )
        if exit_code == 0:
            exit_code = 1
    else:
        print(f"[OK] JOURNAL.md dentro do limite: {journal_lines}/{JOURNAL_MAX_LINES}")

    total_chars, tokens_raw, token_ok = estimate_tokens()
    tokens_k = tokens_raw / 1000
    if not token_ok:
        issues.append(
            f"[WARN] Contexto estimado alto: tokens_raw={tokens_raw} (~{tokens_k:.1f}k). Execute purge."
        )
        if exit_code == 0:
            exit_code = 1
    else:
        print(
            f"[OK] Estimativa de contexto segura: tokens_raw={tokens_raw} (~{tokens_k:.1f}k)"
        )

    reg_ok, reg_msg = check_registry_structure()
    if not reg_ok:
        issues.append(f"[WARN] AGENT_REGISTRY.md: {reg_msg}")
        if exit_code == 0:
            exit_code = 1
    else:
        print("[OK] AGENT_REGISTRY.md estrutura válida.")

    wiki_ok, wiki_msg = check_wiki_integrity()
    if not wiki_ok:
        issues.append(f"[WARN] WIKI: {wiki_msg}")
        if exit_code == 0:
            exit_code = 1
    else:
        print(f"[OK] WIKI: {wiki_msg}")

    print("\n--- Relatório Final ---")
    if not issues:
        if exit_code == 2:
            print("[PENDING] Pendência estratégica detectada.")
            sys.exit(2)
        print("[SUCCESS] Contexto íntegro. Pronto para execução.")
        sys.exit(0)
    else:
        for issue in issues:
            print(issue)
        print("[FATAL] Erros de governança detectados.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        validate()
    except Exception as e:
        print(f"[ERROR] Erro na execucao: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

```
CHUNK_END id=1077e9084ea1_c001
FILE_END id=file_1077e9084ea1

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=100 bytes=7961 mtime=2026-04-17T14:30:57.702377+00:00 sha1=760dffd6994964389bbcdb387181df2366605a40
CHUNK_START id=e7c17acb71ff_c001 start_line=1 end_line=100
````markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-10 20:50
Status: Ativo
---

# 🤖 AGENT_REGISTRY.md
> Catálogo central de especialidades, permissões e escopo de contexto.  
> **Regra de Ouro:** Se um agente não está registrado aqui, ele não existe. Nenhuma tarefa inicia sem roteamento explícito.

💡 *Insight Humano: Este arquivo é o "DNS cognitivo" do projeto. Ele evita que a IA atue de forma genérica, forçando especialização por tarefa. Isso reduz alucinações, melhora a qualidade do código e economiza tokens ao carregar apenas o contexto necessário.*

---

## 🚨 Regra de Registro Obrigatório
> ⚠️ **Atenção para IAs e Humanos:**  
> Antes de criar ou ativar qualquer nova role/agente, você **DEVE** registrá-lo nesta tabela com:  
> - Nome único (`@nome-da-role`)  
> - Especialidade clara e delimitada  
> - Permissões de escrita explícitas (princípio do menor privilégio)  
> - Contexto prioritário para carregamento  
> - Gatilhos de ativação objetivos  
>  
> *Não registrado = Não executado. Esta regra protege a integridade do contexto.*

---

## 📋 Tabela de Agentes Oficiais

| Role | Especialidade | Permissões de Escrita | Contexto Prioritário (Auto-Load) | Gatilho de Ativação |
|------|--------------|----------------------|----------------------------------|---------------------|
| `@db-architect` | Migrations, índices, normalização, otimização de queries | `maintenance/schema.sql`, `migrations/`, `maintenance/TECHNICAL_REQUIREMENTS.md` (seção DB) | `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md`, `maintenance/JOURNAL.md` (bugs de performance) | "criar tabela", "migration", "otimizar query", "índice", "normalizar", "ERD" |
| `@frontend-specialist` | UI/UX, componentes, estado, acessibilidade, CSS, responsividade | `src/components/`, `src/pages/`, `src/styles/`, `maintenance/rx-anatomy.md` | `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais) | "tela", "componente", "layout", "responsivo", "acessibilidade", "CSS", "estado" |
| `@backend-engineer` | APIs, auth, lógica de negócio, webhooks, cache, filas | `src/api/`, `src/services/`, `src/utils/`, `src/config/` | `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs) | "endpoint", "rota", "validação", "webhook", "auth", "serviço", "cache" |
| `@qa-validator` | Revisão de DoD, assinatura de contrato, validação mecânica de testes | `contract` (frontmatter `qa_signoff`), `tests/`, `maintenance/JOURNAL.md` | `spec.md`, `maintenance/TESTS.md` | `"assine contrato"`, `"valide DoD"`, `"rode testes"`, "testar", "bug" |
| `@devops-guardian` | CI/CD, deploy, env vars, monitoramento, segurança infra | `.github/workflows/`, `Dockerfile`, `maintenance/rebuild_guide.md`, `.env.example` | `maintenance/rebuild_guide.md`, `maintenance/TECHNICAL_REQUIREMENTS.md` (infra), `brain/ROADMAP.md` (deploys) | "deploy", "CI/CD", "docker", "variável de ambiente", "monitoramento", "rollback" |
| `@vision-architect` | Estratégia, validação de market fit, definição de boundaries | `.context/brain/INCEPTION.md`, `.context/market/MARKET_INBOX.md` | `.context/brain/INCEPTION.md`, `.context/market/SSOT_MAP.md` | "definir boundary", "validar gap de mercado", "revisar inception" |
| `@spec-enricher` | Tradução estratégica em PRD, tradução cognitiva VISION -> INCEPTION, validação de gaps de mercado | `.context/brain/PRD.md`, `.context/brain/INCEPTION.proposed.md`, `maintenance/JOURNAL.md` | `.context/brain/INCEPTION.md`, `.context/brain/VISION.md`, `.context/market/SSOT_MAP.md` | "enriquecer spec", "gerar PRD", "traduzir visão", "propor inception", `npm run context:enrich` |
| `@spec-driver` | Criação de specs atômicas, geração de contrato DoD, handoff para execução | `.specs/`, `contract` (frontmatter) | `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30) | `"crie spec"`, `"gere contrato"`, "inicie specify", "modo híbrido" |
| `@context-keeper` | Sync, purge, validação de consistência, saúde do contexto | `.context/` (exceto `_archive/`), `maintenance/JOURNAL.md`, `brain/RULES.md` | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `maintenance/JOURNAL.md`, `monitoring/CONTEXT_HEALTH.md` | "atualize contexto", "purge", "health check", "validar consistência", "sincronizar" |
| `@fullstack-generalist` | Modo fallback para tarefas transversais ou projetos light | Leitura em todo o projeto; Escrita apenas com confirmação explícita | `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30 linhas) + Global | "modo light", "tarefa rápida", "projeto pequeno", "não especificado" |

💡 *Insight Humano: A role `@fullstack-generalist` é sua válvula de escape para projetos simples ou tarefas rápidas. Use com moderação: ela carrega mais contexto e tem menos restrições, o que aumenta o risco de alucinação. Prefira sempre as roles especializadas.*

---

## 🔒 Protocolos de Execução

### 🧭 Roteamento de Tarefas
```text
1. Receber comando → 2. Consultar AGENT_REGISTRY.md → 3. Identificar role(s) adequada(s)
4. Declarar ativação: "🤖 Ativando @[role] | Escopo: [descrição curta]"
5. Carregar APENAS: Global + Role-Specific + Task-Ephemeral
6. Executar dentro das permissões → 7. Registrar handoff no JOURNAL.md se cruzar domínios
```

### 🤝 Handoff Obrigatório (Cruzamento de Domínios)
> Quando uma tarefa exigir atuação de 2+ agentes:
> 1. Agente atual pausa a execução
> 2. Registra no `JOURNAL.md`:  
>    `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo passo: [ação]`
> 3. Aguarda confirmação humana ou prossegue automaticamente (se configurado)
> 4. Próximo agente carrega contexto limpo + estado transferido

💡 *Insight IA: Handoff não é só "passar a bola". É garantir que o próximo agente receba o estado exato da execução, sem ruído. Pense como uma função que retorna um objeto bem tipado: claro, mínimo e autoexplicativo.*

### 🧱 Isolamento de Contexto (Anti-Token-Bloat)
| Camada | Arquivos | Quando Carregar |
|--------|----------|-----------------|
| 🌍 Global | `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md` | Sempre (regras imutáveis do jogo) |
| 🧭 Strategic | `brain/INCEPTION.md`, `market/SSOT_MAP.md` | Durante planejamento estratégico ou via `@vision-architect` |
| 🎯 Role-Specific | Definido na coluna "Contexto Prioritário" da tabela | Só durante a execução daquele agente |
| 📦 Task-Ephemeral | `brain/PRD.md` ativo, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (últimas 30-50 linhas) | Durante a tarefa atual |
| 🗃️ Deep Archive | `_archive_context/` | Nunca por padrão. Só via comando explícito: "consulte o archive de X" |

> **Regra de Ouro:** `Se o agente não precisa do arquivo para completar a tarefa atual, ele não é carregado.`

---

## 🆕 Como Adicionar um Novo Agente (Template)
```markdown
### `@nome-da-nova-role`
- **Especialidade:** [Descreva em 1 linha o foco principal]
- **Permissões de Escrita:** [Liste pastas/arquivos exatos. Seja restritivo.]
- **Contexto Prioritário:** [Quais arquivos este agente carrega por padrão?]
- **Gatilho de Ativação:** [Palavras-chave ou padrões de comando que disparam esta role]
- **💡 Insight:** [Explique em 1 frase por que esta role é útil e quando usá-la]
```

---

## 📊 Health Check Rápido (Para @context-keeper)
```text
✅ Registry está sincronizado com o código? (Novas pastas têm dono?)
✅ Alguma role está com permissões excessivas? (Princípio do menor privilégio)
✅ Gatilhos de ativação ainda fazem sentido com o PRD atual?
✅ Insight humano está ajudando ou poluindo?
```

💡 *Insight Final: Este arquivo é vivo. Revise-o a cada nova fase do ROADMAP.md. Um registry desatualizado é pior que nenhum registry — ele dá falsa sensação de controle.*

````
CHUNK_END id=e7c17acb71ff_c001
FILE_END id=file_e7c17acb71ff

---
<a id="file_4b29e274836e"></a>
FILE_START id=file_4b29e274836e path=.context/brain/HARNESS_REGISTRY.md domain=docs lang=markdown lines=20 bytes=1180 mtime=2026-04-11T23:46:58.142679+00:00 sha1=5a29edb2d353e3117e7e904191ef4dadfd322309
CHUNK_START id=4b29e274836e_c001 start_line=1 end_line=20
```markdown
---
Criado em: 2026-04-11
Status: Ativo
---

# 🛡️ HARNESS_REGISTRY.md
> Superfície de controle para validação de contratos e reação automática.

## 📋 Tabela de Harnesses Ativos
| ID | Tipo | Escopo | Contrato/Schema | Gatilho | Validação | Fallback |
|----|------|--------|-----------------|---------|-----------|----------|
| `H01` | Schema | DB/Queries | `maintenance/schema.sql` | `@db-architect`, `@backend` | Campos existem? Tipos compatíveis? | `@db` cria migration |
| `H02` | AI/LLM | Outputs/Specs | `spec.md` + `PRD.md` | `@spec-driver`, `@frontend` | JSON válido? Critérios cobertos? | `@qa` revalida |
| `H03` | Handoff | Cross-Role | `JOURNAL.md` tags | Troca de domínio | Handoff registrado? Estado limpo? | Pausa + alerta |
| `H04` | Secrets | Segurança | Regex + `.env.example` | Commit/Spec | Zero chaves hardcoded | Rejeita + scrub |

## ⚙️ Regras de Execução
- ✅ `harness_runner.py` deve rodar antes de qualquer merge ou geração de código produtivo.
- ⚠️ Falha consecutiva >2x → pausa automática + log em `JOURNAL.md` com tag `[harness:fail]`.
- 🔒 Nunca sobrescrever `.context/` sem passar por validação de contrato.

```
CHUNK_END id=4b29e274836e_c001
FILE_END id=file_4b29e274836e

---
<a id="file_de9ef20db2be"></a>
FILE_START id=file_de9ef20db2be path=.context/brain/INCEPTION.md domain=docs lang=markdown lines=43 bytes=3455 mtime=2026-04-23T15:10:01.045421+00:00 sha1=1c3639bff80071b9781712b04dfd7edd74ca73bc
CHUNK_START id=de9ef20db2be_c001 start_line=1 end_line=43
```markdown
---
version: 2.5.2
mode: STRATEGIC
status: ACTIVE  # [DRAFT | ACTIVE | TRANSLATION_LOCK]
---

<!-- 🚨 SYSTEM TRIGGER: IA, NÃO PROSSIGA PARA GERAÇÃO DE CÓDIGO SE OS CAMPOS ABAIXO CONTIVEREM "[TODO]" OU PERGUNTAS. INTERROGUE O HUMANO PRIMEIRO. -->
> 🤖 **INSTRUÇÃO DE FLUXO:** Antes de propor specs ou código, preencha os campos estratégicos. Se `[TODO]` persistir, retorne ao humano com: `"⚠️ Contexto incompleto em INCEPTION.md. Preciso de: [lista]"`.

# 🧭 INCEPTION - Fronteiras Estratégicas (SSOT)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita a Estratégia de Negócio e Limites Arquiteturais (O que NUNCA e SEMPRE fazer).
> - **NÃO** insira UUIDs, IDs de nuvem, mapeamento de pastas, nem configurações de ferramentas.
> - Dependências externas devem ir pro `market/SSOT_MAP.md`.
> - Somente a role `@vision-architect` deve alterar significativamente este arquivo.

*Ratificado a partir da tradução cognitiva do `VISION.md`.*

## 🎯 Visão Mestra
O Antigravity Kit (H.O.K Forge v2.5.2) é uma solução de **Harness Engineering** projetada para PMEs e Tech Leads. Seu objetivo é controlar o "AI Slop" e governar as IA geradoras de código através de uma arquitetura determinística implacável, reduzindo confabulações e inchaço de contexto sem depender de infraestruturas MLOps complexas. A equação fundamental é **Agente = Modelo + Harness**.

## 🛑 NUNCA (Boundaries)
> *Limites inegociáveis. Se a IA tentar cruzar estas linhas, o Harness aplicará o fail-fast.*

## 🛡️ Checklist Estratégico (Preenchimento Obrigatório)
- [ ] **Transações DB?** (Sim/Não. Se sim, qual engine?)
- [ ] **APIs Externas?** (Ex: Stripe, Meta, OpenAI)
- [ ] **Compliance Obrigatório?** (Ex: LGPD, HIPAA, PCI)

- **NUNCA** utilizar infraestruturas de MLOps de grande porte ou bancos vetoriais pesados. A indexação deve permanecer leve, rápida e focada na realidade financeira do projeto.
- **NUNCA** confiar apenas na aprovação sintética da IA (Leniency Bias). Nenhuma linha é final sem passar pelo sensor computacional rígido do Harness de Contratos (`harness_runner.py`).
- **NUNCA** introduzir complexidade tecnológica desnecessária no banco de estados; o repositório **deve** usar apenas `.md`, `.json` e `.sql` como SSOT (Single Source of Truth).
- **NUNCA** permitir confabulação de dados. Afirmações técnicas sem citação explícita (`> Fonte: RAW/...`) do Linter Epistemológico (Karpathy rule) serão sumariamente rejeitadas.
- **NUNCA** trabalhar com contexto infinito. As execuções devem usar o *Ralph Wiggum Loop*, quebrando o desenvolvimento em Specs Atômicas com aniquilação periódica de memória.

## 🟢 SEMPRE (Restrições de Processo)
> *Processos que a IA deve invocar obrigatoriamente durante o ciclo de vida.*

- **SEMPRE** utilizar bibliotecas padrão (`stdlib-only`) para os scripts do Oráculo, garantindo execução local independente de contêineres e dependências pesadas.
- **SEMPRE** aplicar a "Divulgação Progressiva". O conhecimento deve ser roteado *just-in-time*, entregando ao modelo apenas o que ele precisa saber para a task efêmera, evitando Context Bloat.
- **SEMPRE** validar os limites técnicos usando o `schema.sql` antes de qualquer ação generativa de UI ou banco.
- **SEMPRE** utilizar a pasta `market/` para populacionar lacunas tecnológicas via "Spec Enricher" antes de compilar Documentos de Requisitos finais (PRDs).

```
CHUNK_END id=de9ef20db2be_c001
FILE_END id=file_de9ef20db2be

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=107 bytes=5912 mtime=2026-04-23T14:41:07.641418+00:00 sha1=e1d7f433195535d0dafdb6ae0a923408328e50fb
CHUNK_START id=d833c436f547_c001 start_line=1 end_line=107
````markdown
---
Criado em: 2026-04-10 23:28
Ultima Atualizacao: 2026-04-23 11:39
Status: Ativo
---

# 🏛️ MASTER_FLOW: Estrutura de Contexto em Camadas

Este documento é a diretriz mestre para a condução de projetos "AI-Ready". Ele define uma arquitetura de memória persistente em camadas para garantir foco, rastreabilidade e performance.

---

## 🕒 1. Metadados Obrigatórios
Todo arquivo dentro de `.context/` (exceto scripts) de conter este cabeçalho:
```markdown
---
Criado em: YYYY-MM-DD HH:MM
Ultima Atualizacao: YYYY-MM-DD HH:MM
Status: [Ativo | Arquivado | Depreciado]
---
```

---

## 📂 2. Estrutura de Governança (Context & Specs)

```text
/ (Root do Projeto)
├── .specs/                 # 🆕 WORKBENCH EFÊMERO (The Workshop - TLC)
│   └── features/           # Specs e tasks atômicas em execução
│
└── .context/               # 🏛️ GOVERNO E MEMÓRIA DE LONGO PRAZO
    ├── 🧠 brain/
    │   ├── ...
    │   ├── INCEPTION.md               # Fronteiras estratégicas (SSOT) [DRAFT|ACTIVE]
    │   ├── INCEPTION.proposed.md      # Proposta gerada pela IA (Aguardando Ratificação)
    │   └── VISION.md                  # Entrada narrativa humana (Input de Visão)
    │
    ├── 🌐 market/                      # CAMADA ESTRATÉGICA (Restrições Externas)
    │   ├── RAW/                       # Minério Bruto (Humano deposita)
    │   ├── WIKI/                      # Conhecimento Destilado (Atômico)
    │   ├── SSOT_MAP.md
    │   ├── wiki_log.md                # Log de Transação (Ingest/Lint)
    │   ├── MARKET_INBOX.md
    │   ├── economics.md
    │   ├── compliance/
    │   └── research/
    │
    ├── 🛠️ maintenance/                 # CAMADA DE MANUTENÇÃO (The Housekeeper)
    │   ├── JOURNAL.md                 # Log vivo (Máx ~50k char - Memória Contínua)
    │   ├── TECHNICAL_REQUIREMENTS.md  # Stack, libs e infra (Inventário)
    │   ├── rebuild_guide.md           # Guia de setup e infra (Pós-Mortem Vivo)
    │   ├── schema.sql                 # Snapshot do Banco de Dados (Verdade Real)
    │   ├── ARCHITECTURE.md            # Blueprint técnico evolutivo (O DNA)
    │   ├── TESTS.md                   # Ledger de padrões e TDDs
    │   ├── rx-anatomy.md              # Raio-X de pastas (Anatomia do Repositório)
    │   ├── rx-biology.md              # Raio-X de fluxos (Biologia do Negócio)
    │   └── _archive_context/          # Histórico imutável (A Biblioteca)
    │
    ├── monitoring/             # CAMADA DE MONITORAMENTO (The Guardian)
    │   └── CONTEXT_HEALTH.md   # Dashboard de saúde técnica e cognitiva
    │
    └── _scripts/               # CAMADA DE AUTOMACAO (The Motor)
        ├── validate_context.py        # Validador de integridade e status
        ├── enrich_context.py          # Tradutor cognitivo e Gap Check
        ├── purge_journal.py           # Gerenciador de memória (Purge)
        ├── cleanup_specs.py           # Gerenciador de efemeridade (.specs)
        └── sync_project.py            # Sincronizador de requisitos

---

## 🔄 2.1 Ciclo de Vida TLC Autobuilder (4 Atos)
| Ato | Gatilho | Ferramenta/Script | Saída Esperada |
|-----|---------|-------------------|----------------|
| **1. [Semente]** | `INCEPTION.md` ativo + gaps | `npm run context:enrich` | `PRD.md` lastreado + `market/` populado |
| **2. [Engenharia]** | Criação de `.specs/features/X/` | `qa_signoff: true` no frontmatter | Contrato assinado; se `type: standard`, validador em contexto distinto |
| **3. [Ingestão]** | `RAW/` novo ou `WIKI/` modificado | `npm run context:ingest-guard` | Artigo validado + `wiki_log.md` |
| **4. [Execução]** | `npm run context:harness` + `lint` | `harness_runner.py` + `lint_wiki.py` | Código validado + `STATE.md: ✅ PASSED` |
| **5. [Rito]** | Merge ou >48h inativo | `npm run context:cleanup` | Spec arquivada + `JOURNAL.md` atualizado |

> 🤖 [SYSTEM HOOK] IA: Este fluxo é imutável. Não pule o Ato 2. Não gere código sem `qa_signoff`. Em `type: standard`, `executor_context_id` e `validator_context_id` devem ser diferentes.

---

## ⚙️ 3. Regras de Manutenção & Ciclo de Vida

### 🔄 Ciclo de Vida de PRD e Schema
1.  **Upgrade:** Antes de alterar o `brain/PRD.md` ou `maintenance/schema.sql`, uma cópia do estado atual deve ser movida para a respectiva subpasta no `_archive_context/`.
2.  **Snapshot:** O arquivo na raiz da camada deve representar sempre o estado "Em Execução" ou "Produção".

### 🧪 Gestão do `.specs/` (The Workshop)
- **Efemeridade:** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/` ou deletar.
- **Validação Leve:** O validador checa apenas a existência e a presença do `STATE.md`, sem fiscalizar o conteúdo interno para manter a agilidade.
- **Sincronia:** Decisões arquiteturais tomadas durante o TLC **devem** ser migradas para o `JOURNAL.md` antes da limpeza da spec.

### 🤖 Roteamento & Isolamento Multi-Agent
1.  **Ativação:** Consultar `brain/AGENT_REGISTRY.md` + template de `brain/PROMPT_LIBRARY.md` e declarar ativação.
2.  **Janela de Contexto:** Global + Role-Specific + Task-Ephemeral. Nunca carregar o `_archive/` sem comando explícito.
3.  **Sync Pós-Execução:** Ao finalizar uma tarefa, valide a consistência entre código, `schema.sql` e `JOURNAL.md` antes de encerrar.

### 📝 Gestão do JOURNAL.md
- **Limite:** Máximo de 600 linhas.
- **O Purge:** Ao atingir o limite, os 70% mais antigos vão para o arquivo e os 30% mais novos ficam como semente.

---

> *Este template transforma um repositório comum em um ecossistema inteligível para IAs de alta performance.*

````
CHUNK_END id=d833c436f547_c001
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=29 bytes=1406 mtime=2026-04-17T01:21:43.543040+00:00 sha1=c75b72944c19fabc58237fb903784cb79ae6b4da
CHUNK_START id=d124f6374cab_c001 start_line=1 end_line=29
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 20:50
Status: Ativo
---

# 📦 Product Requirements Document (PRD)
> **TEMPLATE MESTRE**  
> Todas as funcionalidades descritas aqui SERÃO desmembradas em Specs Atômicas no The Workshop (`.specs/`). Nenhuma instrução contida neste PRD pode violar as restrições estratégicas estabelecidas no `INCEPTION.md`.

## 📌 1. Visão Geral
[Descreva o problema que o produto resolve, o público-alvo e o principal critério de sucesso do projeto. Seja direto.]

## 🚀 2. Requisitos Funcionais (Épicos)
*Descreva as entregas do ponto de vista do usuário final.*
- [ ] **Épico 1:** [Descrição breve].
  - História 1: "Como [ator], eu quero [ação] para que [valor]".

## 🛡️ 3. Critical Dependencies & Limites
> **Obrigatório:** Todas as dependências tecnológicas, de compliance ou integrações devem ter lastro ("Fonte: raw/...") validado na camada `market/`.

- **Integrações Externas:** [Nenhuma Detectada] → Fonte: *market/SSOT_MAP.md*
- **Compliance:** [Normal] → Fonte: *market/SSOT_MAP.md*

## 📓 4. Lógica de Negócio Categórica (Regras)
- [Regra de negócio inegociável]

---
💡 *Nota para Especialistas (Agentes):* Antes de decompor estas premissas usando o `@spec-driver`, ative o `npm run context:validate` para garantir que o projeto cumpriu a fase de **Hybrid Discovery** e está em `status: ACTIVE`.

```
CHUNK_END id=d124f6374cab_c001
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=203 bytes=9794 mtime=2026-04-17T14:31:34.213228+00:00 sha1=002c5f92393fcfd0ce78f0ec85aa8d93af6e377d
CHUNK_START id=9fe16e5591f0_c001 start_line=1 end_line=203
````markdown
---
Criado em: 2026-04-10 21:35
Ultima Atualizacao: 2026-04-10 21:35
Status: Ativo
---

# 📖 PROMPT_LIBRARY.md
> Catalogo de prompts padronizados por role. Use estes templates para garantir consistência, contexto enxuto e execução previsivel.

💡 *Insight Humano: Prompts padronizados reduzem variabilidade, economizam tokens e forcam a IA a seguir o protocolo. Pense neles como "funcoes" bem tipadas: entrada clara, contexto limitado, saida esperada.*

---

## 🧭 Como Usar
1. Escolha a role no `brain/AGENT_REGISTRY.md`
2. Copie o template correspondente
3. Substitua os placeholders `{{...}}`
4. Cole no chat + declare a ativação da role
5. A IA responderá seguindo estritamente o escopo definido

---

## 🤖 Templates por Role

### 🗄️ `@db-architect`
**Gatilho:** Criacao de tabela, migration, otimizacao de query, normalizacao  
**Contexto Obrigatorio:** `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (secao DB), `maintenance/JOURNAL.md` (bugs recentes)
```text
🤖 Ativando @db-architect | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCHEMA_SNAPSHOT: {{tabela(s)_alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser feito no DB}}
🚧 Restricoes: 
- Seguir padrao de nomenclatura do schema atual
- Gerar migration SQL compativel com a stack definida
- Nao quebrar relacoes existentes
- Incluir indices apenas se justificado por query pattern
📤 Saida Esperada: 
1. SQL da migration (CREATE/ALTER)
2. Breve explicacao de impacto
3. Atualizacao sugerida para maintenance/schema.sql
```

### 🖥️ `@frontend-specialist`
**Gatilho:** Telas, componentes, UI/UX, estado, responsividade, acessibilidade  
**Contexto Obrigatorio:** `maintenance/rx-anatomy.md`, `maintenance/ARCHITECTURE.md` (UI Layer), `brain/PRD.md` (fluxos visuais)
```text
🤖 Ativando @frontend-specialist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 UI_CONTEXT: {{pasta/componente alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{o que precisa ser construido/ajustado na UI}}
🚧 Restricoes:
- Usar stack definida em maintenance/TECHNICAL_REQUIREMENTS.md
- Seguir padrao de nomenclatura de maintenance/rx-anatomy.md
- Garantir acessibilidade (WCAG 2.1 AA minimo)
- Nao hardcoded de dados; usar mock/props tipados
📤 Saida Esperada:
1. Codigo do componente/tela
2. Estados gerenciados e interface de props
3. Checklist de responsividade/a11y
```

### ⚙️ `@backend-engineer`
**Gatilho:** Endpoints, logica de negocio, auth, webhooks, cache, filas  
**Contexto Obrigatorio:** `maintenance/rx-biology.md`, `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/TECHNICAL_REQUIREMENTS.md` (APIs)
```text
🤖 Ativando @backend-engineer | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 API_SCOPE: {{rota/servico alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{logica, endpoint ou integracao a ser implementada}}
🚧 Restricoes:
- Validar input contra schema do DB antes de processar
- Retornar erros padronizados (HTTP status + mensagem clara)
- Nenhuma credencial hardcoded; usar variaveis de ambiente
- Seguir arquitetura definida em maintenance/rx-biology.md
📤 Saida Esperada:
1. Codigo do servico/rota
2. Validacoes e tratamento de erro
3. Exemplo de request/response
4. Nota de seguranca/performance se aplicavel
```

### 🧪 `@qa-validator`
**Gatilho:** Testes, validacao, edge cases, cobertura, mocks  
**Contexto Obrigatorio:** `maintenance/TESTS.md`, `maintenance/JOURNAL.md` (bugs recentes), `brain/PRD.md` (criterios de aceite)
```text
🤖 Ativando @qa-validator | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{arquivo/feature a ser testada}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{criar testes, validar edge cases ou aumentar cobertura}}
🚧 Restricoes:
- Seguir framework de testes definido em maintenance/TECHNICAL_REQUIREMENTS.md
- Mockar servicos externos; nao depender de rede real
- Cobrir happy path + 2 edge cases criticos no minimo
- Documentar falhas conhecidas no maintenance/JOURNAL.md se houver
📤 Saida Esperada:
1. Codigo dos testes (unitarios/integracao)
2. Matriz de cenarios cobertos
3. Recomendacoes de refatoracao se aplicavel
4. Se atuando na revisão do Contrato de Sprint: Atualizar a spec mudando `qa_signoff: true` e `signed_by: "@qa-validator"` se a spec.md estiver rigorosa. Se houver desvio, devolva EXIT com o erro para o @spec-driver corrigir.
```

### 🔄 `@fullstack-generalist` (Modo Solo/Light)
**Gatilho:** Projetos pequenos, tarefas rapidas, modo fallback  
**Contexto Obrigatorio:** `brain/PRD.md`, `maintenance/schema.sql`, `maintenance/JOURNAL.md` (ultimas 30 linhas)
```text
🤖 Ativando @fullstack-generalist | Tarefa: {{descrição_curta}}
📌 PRD_REF: {{#ID ou "N/A"}}
📌 SCOPE: {{area do projeto}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{implementar ajuste rapido ou feature simples}}
🚧 Restricoes:
- Manter escopo minimo e atomico
- Atualizar maintenance/JOURNAL.md se houver mudanca de logica
- Validar maintenance/schema.sql antes de criar interfaces
- Evitar over-engineering
📤 Saida Esperada:
1. Codigo necessario
2. Nota de contexto atualizado (se aplicavel)
3. Proximos passos recomendados
```

---

## 🛡️ Regras de Uso
- 🔒 **Context Gate:** Nunca execute um template sem validar a integridade do contexto via `npm run context:validate`.
- 🤝 **Handoff:** Se a tarefa cruzar 2+ roles, interrompa, registre no `maintenance/JOURNAL.md` e ative a proxima role.
- 🧱 **Isolamento:** Carregue APENAS os arquivos listados em "Contexto Obrigatorio". Ignore o restante.

### 🧭 `@vision-architect`
**Gatilho:** Incepção, boundaries estratégicas, validação de mercado, análise de gaps  
**Contexto Obrigatório:** `brain/INCEPTION.md`, `market/SSOT_MAP.md`, `market/MARKET_INBOX.md`
🤖 Ativando @vision-architect | Tarefa: {{descrição_curta}}
📌 PROJECT_VIBE: {{resumo do sentimento}}
📌 MARKET_CONTEXT: {{gaps ou pesquisas alvo}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: {{definir boundaries, validar fit ou resolver gaps}}
🚧 Restrições:
- Respeitar hierarquia do market/SSOT_MAP.md
- Citações explícitas em previsões (Regra Karpathy)
- Boundaries verificáveis apenas (formato: - NUNCA: X)
📤 Saída Esperada:
1. Proposta editada para INCEPTION.md
2. Novos itens para MARKET_INBOX.md se houver gaps
3. Verificação de alinhamento com PRD (se existir)

### 🕵️‍♂️ `@spec-enricher` (Executor de Enriquecimento)
**Gatilho:** `"enriquecer spec"`, `"gerar PRD"`, `"validar market gaps"`  
**Contexto Obrigatório:** `brain/INCEPTION.md`, `market/SSOT_MAP.md`, `market/compliance/`, `market/research/`
```text
🤖 Ativando @spec-enricher | Tarefa: {{descrição_curta}}
📌 CONTEXT_CHECK: ✅ Validado via npm run context:validate
🎯 Objetivo: Traduzir INCEPTION.md em PRD.md lastreado, preenchendo lacunas de mercado antes da execução.

🔒 PROTOCOLO DETERMINÍSTICO (Executar em ordem):
1. ESCANEAR: Extrair todas as entidades externas, compliance e stacks citadas no INCEPTION.md.
2. VALIDAR MARKET: Para cada entidade, verificar existência de arquivo em market/compliance/ ou market/research/.
3. RESOLVER GAPS:
   - Se arquivo existir → Ler e extrair constraints.
   - Se NÃO existir → Inserir linha em market/MARKET_INBOX.md com `[TODO: research]` e **PARAR**. Retornar: `EXIT 2: Pesquisa de mercado obrigatória antes de gerar PRD.`
4. CRISTALIZAR PRD: Se todos os gaps estiverem resolvidos, gerar PRD.md amarrando cada requisito crítico a `> Fonte: market/...`.
5. HANDOFF: Registrar no JOURNAL.md: `🔄 Handoff: @spec-enricher → @spec-driver | PRD lastreado | Próximo: criar .specs/`

⚠️ REGRAS INEGOCIÁVEIS:
- Nunca assumir dados de mercado. Use apenas fontes em `market/` ou pare com EXIT 2.
- Respeitar hierarquia: `market/compliance/` > `INCEPTION.md [Boundaries]` > `PRD.md`
- Se INCEPTION.md conter `TYPE: PATCH` ou `COMPLEXITY: LOW`, pular validação de mercado e gerar PRD direto.

⚙️ ENTREGA OBRIGATÓRIA:
Ao gerar o PRD.md, inclua EXATAMENTE esta seção no final:
## 🚨 Critical Dependencies
- **{Nome_Entidade}** → Fonte: `market/{compliance|research}/{arquivo}.md`
- **{Outra_Entidade}** → Fonte: `market/{compliance|research}/{arquivo}.md`

⚠️ O Harness validará semanticamente (bullet + Fonte: + market/).
```

### 🧬 `@agent-hybrid-tlc` (Spec-Driven + Context Governance)
**Gatilho:** "Inicie SPECIFY", "Crie spec atômica", "Modo Híbrido TLC"  
**Contexto Obrigatório:** `PRD.md`, `schema.sql`, `JOURNAL.md` (tail 30), `RULES.md`

```text
🤖 Ativando @agent-hybrid-tlc | Tarefa: SPECIFY para {{funcionalidade}}
📌 PRD_REF: {{#ID}}
📌 CONTEXT_CHECK: ✅ Validado
🎯 Objetivo: Gerar spec atômica (.specs/) alinhada ao PRD e schema atual
🚧 Restrições:
- Criar pasta .specs/features/{{slug}}/ com spec.md e STATE.md
- Especificar apenas 1 passo atômico por vez
- Validar contrato contra schema.sql antes de definir outputs
- Nunca hardcode; usar [PLACEHOLDER] se depender de env externo
📤 Saída Esperada:
1. Estrutura .specs/ criada com o_template padronizado do bloco YAML definition_of_done.
2. spec.md com passos atômicos, onde o contrato e critérios de verificação residem na root (Frontmatter).
3. STATE.md: draft → aguardando qa_signoff.
```
💡 *Insight IA: Este prompt transforma intenção em plano executável. A spec é o "compilador" entre PRD e código. Mantenha-a enxuta e verificável.*

💡 *Insight IA: Estes templates sao contratos de execucao. Eles reduzem ruido e transformam a IA em um engenheiro previsivel.*

````
CHUNK_END id=9fe16e5591f0_c001
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=15 bytes=719 mtime=2026-04-21T23:32:04.607493+00:00 sha1=55fb929dd00b9a0eff1c9a253ec37e0609445e92
CHUNK_START id=c94f001202db_c001 start_line=1 end_line=15
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-21
Status: Ativo
---

# 🗺️ ROADMAP: Fases do Autobuilder
> 🤖 [SYSTEM HOOK] Siga esta ordem. Não pule fases.

| Fase | Nome | Gatilho de Início | Critério de Saída |
|------|------|-------------------|-------------------|
| **1** | Discovery | `INCEPTION.md` ativo + `npm run context:enrich` | `PRD.md` lastreado + `market/` ok |
| **2** | Contratos/DB | `schema.sql` criado + `qa_signoff` | Harness passa + Migrations 001 applied |
| **3** | Features/WIKI | `.specs/` criadas + `lint_wiki.py --strict` | `STATE.md: ✅ PASSED` em todas specs |
| **4** | Scale/Deploy | CI/CD green + `npm run context:cleanup` | `VERSION.md` bumped + Tag release |

```
CHUNK_END id=c94f001202db_c001
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=121 bytes=8428 mtime=2026-04-23T16:12:49.465411+00:00 sha1=bda18421976aa89e223cbdfbcbe9a931fba8dbc4
CHUNK_START id=cd6526d17218_c001 start_line=1 end_line=121
```markdown
---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-23 11:39
Status: Ativo
---

# 📜 RULES.md — Template Universal de Contexto & Governança
**Projeto:** [NOME DO PROJETO]  
**Arquitetura:** AI-Agent Driven (Layered Context Architecture)  
**PROJECT_MODE:** `[BOOTSTRAP]` *(Fases finitas: BOOTSTRAP, HARDENING, PRODUCTION)*

> **Conceito Central (H.O.K Forge):** A equação moderna do código autônomo é `Agente = Modelo + Harness`. O `.context` atua como Governador Cibernético (SSOT), não apenas como documentação.

---

## 🏗️ 0. Máquina de Estados (`PROJECT_MODE`)
1. `[BOOTSTRAP]`: Criação de infra e docs core.
2. `[HARDENING]`: Segurança, estabilização e redução de dívida técnica.
3. `[PRODUCTION]`: Desenvolvimento maduro de features.
⚠️ Transição de estado deve ser registrada no `JOURNAL.md`.

## 🔄 0.1 Ciclo de Vida do Inception (Hybrid Discovery)
O `INCEPTION.md` (brain/) regula o que a IA pode ou não fazer.
*   `status: DRAFT`: Fase de onboarding ou reset. Permitido apenas leitura e criação de `VISION.md`. Bloqueia escrita em `src/` e `tests/`.
*   `status: TRANSLATION_LOCK`: Ativado pelo `@spec-enricher` ao gerar o `INCEPTION.proposed.md`. **Bloqueio Global**: Nenhuma ferramenta de escrita (exceto o próprio enrich) funciona até a ratificação humana.
*   `status: ACTIVE`: Estado normal de operação. Limites técnicos ratificados.

---

## 🛡️ 1. Checklist de Carga (Obrigatório)
Antes de gerar código de produção ou realizar refatorações, o Agente **DEVE** validar se o contexto necessário está carregado:
1. **[ ] Global Layer:** `brain/RULES.md`, `brain/MASTER_FLOW.md`, `brain/ROADMAP.md`
2. **[ ] Strategic Layer:** `brain/INCEPTION.md` (se existir) + `market/SSOT_MAP.md`
3. **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` para a Role ativa.
4. **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`

> ⚠️ **Bloqueio de Execução:** Se qualquer item estiver ausente ou desatualizado, a IA deve parar e solicitar a carga correta antes de prosseguir.

---

## 🤝 1.1 Regra de Contrato de Sprint (Research-First)
1. `@spec-driver` gera `spec.md` com bloco YAML de `definition_of_done`.
2. `@qa-validator` revisa critérios. Se válidos, seta `qa_signoff: true` e `signed_by: "@qa-validator"`.
3. **Regra v2.5.2:** Se `type: standard`, o `validator_context_id` deve ser diferente do `executor_context_id` para que a assinatura seja valida.
4. **Bloqueio:** Se `qa_signoff == false`, `definition_of_done` estiver vazio, ou (em `type: standard`) os IDs forem iguais/ausentes, o Harness retorna `Exit 1`.
5. Nenhuma geração de código ou merge é permitida antes da assinatura.

## 🔄 1.2 Consistência de Versão (SSOT)
1. `VERSION.md` é a única fonte da verdade para versão do framework.
2. O pipeline `npm run context:all` executa `check_version_consistency.py` antes das demais validações.
3. Drift em `package.json`, `INCEPTION.md` ou `VISION.md` bloqueia o pipeline (`Exit 1`).

---

## 🔢 2. Ansiedade de Contexto & Ralph Wiggum Loop
Para combater o *Context Anxiety* e alucinações por inchaço:
- **Ralph Wiggum Loop:** O foco é absoluto e efêmero. Apenas resolver a Spec atômica atual no `The Workshop` (`.specs/`), persistir os descobrimentos difíceis no `JOURNAL.md`, e encerrar a sessão. A cada ciclo, a memória sintética zera e o sistema de arquivos assume como memória indestrutível.
- **Gatilhos de Alerta:** ~50.000 caracteres ou 15 trocas densas. Se atingido, purgue o Journal ou inicie chat limpo.

---

## 🧠 3. Protocolo de Manutenção do Contexto
A IA atua como bibliotecário chefe. Consistência entre Código e Contexto é obrigatória.
- **`maintenance/JOURNAL.md`:** Apenas decisões de arquitetura, resoluções de bugs complexos e mudanças de lógica. Proibido logar erros triviais. Ao atingir ~600 linhas ou 50k chars → acionar `_scripts/purge_journal.py`.
- **`maintenance/TECHNICAL_REQUIREMENTS.md`:** Atualizar sempre que houver mudança em `package.json`, alteração de Schema ou integração de novas APIs.
- **`maintenance/rebuild_guide.md`:** Atualizar com hacks de ambiente local, CI/CD ou passos manuais de deploy.
- **`.specs/` (Workshop Efêmero):** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/`. Decisões técnicas devem migrar para o `JOURNAL.md` antes da limpeza.

---

## 🗄️ 4. Protocolo Database-First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados.
1. **Verificação Obrigatória:** Antes de criar UI/lógica dependente de dados, validar `maintenance/schema.sql`.
2. **Aviso de Divergência:** Se o código exigir um campo inexistente, parar e avisar: *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro gerar a migration antes de prosseguir."*

---

## 🤖 5. Comportamento do Agente (Transparência & Roteamento)
- **Ativação:** Toda tarefa complexa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`. Ignorar o resto.
- **Handoff:** Cruzar 2+ domínios? Pausar → registrar no `JOURNAL.md`:  
  `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo: [ação]`
- **Context Gate (Pré-Código):** Validar antes de gerar:  
  `[ ] PRD ativo` | `[ ] schema contém estruturas` | `[ ] JOURNAL < 550 linhas` | `[ ] zero secrets hardcoded`

---

## 🔄 6. Gatilhos de Interação (Para o Usuário)
- `"Atualize o contexto"` → IA sintetiza mudanças no `JOURNAL.md` e checa requisitos.
- `"Qual o estado do projeto?"` → Relatório baseado no `JOURNAL.md` + `ROADMAP.md`.
- `"Roteie esta tarefa"` → Consulta `AGENT_REGISTRY.md`, inicia ativação/handoff.
- `"Use o prompt padrão"` → Seleciona template em `brain/PROMPT_LIBRARY.md`, preenche placeholders, solicita confirmação.
- `"Inicie SPECIFY para PRD #[ID]"` → Cria `.specs/features/`, gera `spec.md` alinhado ao PRD, inicia ciclo TLC.

---

## 🚨 7. Segurança e Saúde
- **Segredos:** Variáveis (`API_KEYS`, `TOKENS`) nunca no código. Referenciar como `[VARIABLE_NAME]` e usar `.env`.
- **Depreciação:** Se função/arquivo for removido, marcar como `[DEPRECATED]` ou remover do contexto para evitar sugestão de código morto.
---

## 🔍 8. Protocolo Oracle & Engenharia de Guerrilha
- **Stdlib-only:** Os scripts de Oráculo/Busca devem ser construídos estritamente usando a biblioteca padrão para evitar dependências pesadas. Nada de Kubernetes ou Vector DBs complexos para PMEs.
- **UTF-8 Nativo:** Todos os scripts encarregados da governança em Python (`_scripts/`) devem ser envelopados para forçar I/O em UTF-8 (`sys.stdout = io.TextIOWrapper...`), garantindo blindagem contra quebras de console Windows.
- Se a spec ou PRD contiver ambiguidade técnica, consulte limitando o escopo a Divulgação Progressiva: `npm run context:oracle "sua dúvida"`
- Nunca assuma. Consulte! Se `confidence < 0.5` -> pause.

## 📖 9. Regra Karpathy (Destilação Mandatória v2.5.2)
O H.O.K utiliza a **Estratificação de Densidade** para evitar o *Context Anxiety*.

1.  **Camada RAW (`market/RAW/`)**: Humano deposita dossiês brutos. IA operacional NÃO lê esta pasta.
2.  **Protocolo de Destilação**: IA fatia o RAW em átomos na `market/WIKI/` (máx 500 tokens por arquivo).
3.  **Ciclo de Governança Wiki (Nível 2)**:
    - **INGEST**: Destilação via `@wiki-ingestor`. Requer Frontmatter completo e citação `> Fonte: RAW/...`.
    - **LINT**: `npm run context:lint-strict` bloqueia artigos sem fonte, takeaways ou estrutura.
    - **LOG**: Toda transação de ingestão é registrada em `market/wiki_log.md` para rastreabilidade de linhagem.
4.  **Consulta**: O Oráculo prioriza o `market/WIKI/` via roteamento determinístico (`_index.md`).
## 📊 10. Dashboard Health Sync
- Antes de processar features complexas ou abrir Specs Atômicas, verifique o `.context/monitoring/CONTEXT_HEALTH.md` para assegurar que a janela de tokens e a saúde do Journal não exigem repouso ou manutenção prévia.

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.

```
CHUNK_END id=cd6526d17218_c001
FILE_END id=file_cd6526d17218

---
<a id="file_e11d89201917"></a>
FILE_START id=file_e11d89201917 path=.context/brain/START_HERE.md domain=docs lang=markdown lines=42 bytes=1749 mtime=2026-04-17T00:07:25.637908+00:00 sha1=482d0d056987215305ae88da18b37a59faa64658
CHUNK_START id=e11d89201917_c001 start_line=1 end_line=42
```markdown
# 🚀 START_HERE: Seu Guia de Onboarding

Bem-vindo ao projeto! Este repositório utiliza o framework de governança **Antigravity v2.4.1**. Para começar de forma produtiva e garantir que a IA entenda seus objetivos, siga este fluxo:

## 🧭 O Ciclo de Vida da Descoberta

Para evitar "alucinações" e garantir que o código reflita sua intenção, seguimos o ciclo:

1. **Visão (Humano)**: Você escreve o que quer em linguagem natural.
2. **Inception (IA Proposta)**: A IA traduz sua visão em limites técnicos.
3. **Ativação (Ratificação)**: Você revisa e ativa a governança.

---

## 🛠️ Passo a Passo para Inicializar

### 1. Declare sua Visão
Crie um arquivo chamado `.context/brain/VISION.md`. 
*   **Dica**: Use o template `.context/brain/VISION.md.template` como base.
*   Escreva livremente: O que o projeto faz? Qual o problema resolve?

### 2. Solicite a Tradução Cognitiva
Peça para sua IA:
> "@spec-enricher detecte minha VISION.md e proponha o INCEPTION.md"

A IA gerará um arquivo `INCEPTION.proposed.md`.

### 3. Ratifique os Limites
Revise o arquivo proposto e, se estiver de acordo:
1. Renomeie `INCEPTION.proposed.md` para `INCEPTION.md`.
2. Altere o metadado `status: DRAFT` para `status: ACTIVE`.
3. Rode `npm run context:all` para confirmar a saúde do projeto.

---

## 📈 Comandos Úteis
*   `npm run context:validate`: Verifica se a documentação está íntegra.
*   `npm run context:enrich`: Sincroniza o contexto e detecta mudanças na visão.
*   `npm run context:all`: Executa a pipeline completa de governança.

> [!NOTE]
> Se você tentar escrever código em `src/` sem ter um `status: ACTIVE` no Inception, o sistema de segurança irá bloquear a execução para evitar desvio estratégico.

```
CHUNK_END id=e11d89201917_c001
FILE_END id=file_e11d89201917

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=32 bytes=1739 mtime=2026-04-11T02:29:02.337886+00:00 sha1=35e6506fdaaa427e4d5795b83709f4f9da37fc2d
CHUNK_START id=450d7ec70909_c001 start_line=1 end_line=32
```markdown
---
Criado em: 2026-04-10 23:29
Ultima Atualizacao: 2026-04-10 23:29
Status: Ativo
---

# 🔗 TLC_INTEGRATION.md
> Ponte entre Governança de Longo Prazo (`.context/`) e Execução Atômica (`.specs/`).  
> 💡 *Insight Humano: O PRD diz O QUÊ e POR QUÊ. A SPEC diz COMO e QUANDO. O TLC orquestra a transição.*

## 🔄 Ciclo de Vida Híbrido
1. **INTENT** → `PRD.md` ativo define escopo e critérios de aceite.
2. **SPECIFY** → IA cria `.specs/features/[nome]/spec.md` com passos atômicos, contratos de API/DB e testes.
3. **IMPLEMENT** → Geração de código baseada na spec. Handoffs registrados no `JOURNAL.md`.
4. **VERIFY** → Testes passam → `STATE.md` marcado como `✅ PASSED`.
5. **SYNC** → Decisões arquiteturais e lições → `JOURNAL.md`. Spec arquivada ou deletada.

## 📏 Regras de Ouro
- 🔒 **Soberania do Contexto:** `.specs/` nunca sobrescreve `.context/`. Apenas alimenta a memória de longo prazo.
- 🧹 **Efemeridade:** Spec inativa >48h ou pós-merge → mover para `_archive_context/specs/` ou deletar.
- 🤝 **Handoff:** Handoff obrigatório no `JOURNAL.md` se a spec cruzar domínios (ex: `@backend` → `@qa`).
- ⚠️ **Divergência:** Se `spec.md` divergir de `schema.sql` ou `PRD.md` → parar e solicitar correção de contexto.

## 🤖 Fluxo de Ativação
`"Inicie a fase de SPECIFY para o PRD #[ID]"` → 
1. IA lê `PRD.md` + `schema.sql` + `JOURNAL.md` (últimas 30).
2. Cria `.specs/features/[nome]/` com `spec.md` e `STATE.md: draft`.
3. Executa passos atômicos → atualiza `STATE.md`.
4. Ao concluir: `✅ Spec passed. Deseja arquivar a spec e sincronizar o JOURNAL.md?`

---
> *Este documento garante que o "Cérebro" (Contexto) e o "Músculo" (TLC) operem em harmonia.*

```
CHUNK_END id=450d7ec70909_c001
FILE_END id=file_450d7ec70909

---
<a id="file_d2f31e4696a6"></a>
FILE_START id=file_d2f31e4696a6 path=.context/brain/VISION.md domain=docs lang=markdown lines=44 bytes=7254 mtime=2026-04-23T15:26:57.151891+00:00 sha1=43246ab516dda1697b1efe4e634120aebce63c56
CHUNK_START id=d2f31e4696a6_c001 start_line=1 end_line=44
```markdown
***

Framework Version: v2.5.2

<!-- 🚨 SYSTEM TRIGGER: IA, NÃO PROSSIGA PARA GERAÇÃO DE CÓDIGO SE OS CAMPOS ABAIXO CONTIVEREM "[TODO]" OU PERGUNTAS. INTERROGUE O HUMANO PRIMEIRO. -->
> 🤖 **INSTRUÇÃO DE FLUXO:** Antes de propor specs ou código, preencha os campos estratégicos. Se `[TODO]` persistir, retorne ao humano com: `"⚠️ Contexto incompleto em INCEPTION.md/VISION.md. Preciso de: [lista]"`.

# Do Vibe Coding à Governança Cognitiva:  H.O.K Forge v2.5

Por muito tempo, a indústria de software viveu a lua de mel do *"vibe coding"*. Descrevíamos um problema, dávamos um prompt genérico para uma Inteligência Artificial e cruzávamos os dedos esperando que a mágica acontecesse. Para protótipos de fim de semana, a abordagem era fascinante. Para sistemas em produção, foi catastrófica. O resultado inevitável dessa liberdade irrestrita foi a proliferação do que a literatura passou a chamar de "AI Slop" — códigos que parecem corretos na superfície, mas que acumulam dívida técnica, vulnerabilidades de segurança e uma arquitetura insustentável.

Diante desse cenário, em 2026, presenciamos uma mudança tectônica. O foco deixou de ser a busca cega por modelos com mais parâmetros e passou a ser o design do ambiente onde esses modelos operam. A resposta não é um modelo melhor; é a **Harness Engineering**. Como bem define Martin Fowler, a equação moderna do desenvolvimento autônomo é simples: **Agente = Modelo + Harness** (onde o *Harness* é todo o ecossistema de restrições, guias e sensores que envolvem o LLM).

Foi sob essa premissa rigorosa que o **Antigravity Kit v2.5.2-Hardened** foi forjado. Não somos um megaconglomerado de tecnologia com infraestruturas infinitas; somos uma solução focada no mundo real de pequenas e médias empresas (PMEs), desenvolvedores solo e *Tech Leads*. Nossa missão é fazer mais com menos, transformando a IA de um gerador de textos caótico em um engenheiro disciplinado através de uma arquitetura determinística e implacável.

### A Tríade H.O.K.: O Governador Cibernético

Modelos de linguagem sofrem de patologias documentadas. Eles confabulam com confiança, são péssimos em julgar a qualidade do próprio trabalho, e perdem a coerência quando o contexto se estende demais. O Antigravity Kit atua como uma "clínica de reabilitação estrutural" para essas inteligências através da sua **Tríade H.O.K.**, funcionando como um verdadeiro governador cibernético:

*   **Harness (Sensores Computacionais Ativos):** A literatura da Anthropic provou que IAs sofrem do **Viés de Leniência** (*Leniency Bias*): elas tendem a adular e aprovar o próprio código, mesmo quando ele é medíocre ou falho. Para combater isso, nosso script `harness_runner.py` age como um sensor computacional rígido. Antes de qualquer linha ser consolidada, o agente Gerador e o agente de QA devem formalizar um **Contrato de Sprint**. Se a IA tentar invocar uma tabela que não existe no `schema.sql` ou quebrar uma regra arquitetural, o Harness aplica o *fail-fast* e bloqueia o commit. A IA não julga; o sistema julga.
*   **Oracle (A Biblioteca Sob Demanda):** Injetar todo o conhecimento da empresa de uma vez na IA gera o temido "inchaço de contexto" (*Context Bloat*). Nosso Oráculo utiliza scripts leves usando apenas a biblioteca padrão do Python (`stdlib-only`) para rotear o conhecimento exato na hora exata, adotando o conceito de "Divulgação Progressiva" e evitando o custo proibitivo de bancos vetoriais complexos que não cabem na realidade de uma PME.
*   **Karpathy (O Linter Epistemológico):** A patologia da **Confabulação Sintética** (a tendência da IA de inventar dados e preencher lacunas de forma plausível, porém falsa) é combatida na raiz. Qualquer afirmação técnica ou decisão arquitetural no framework exige uma citação explícita (`> Fonte: raw/...`). Se não há prova criptográfica no sistema de arquivos, a IA é bloqueada de salvar a alteração.

### O Canteiro de Obras Efêmero e o Ralph Wiggum Loop

Uma das descobertas mais fascinantes da engenharia de agentes recente é a **Ansiedade de Contexto** (*Context Anxiety*). Trata-se de uma resposta semelhante à ansiedade humana diante da escassez de recursos: o modelo, percebendo que sua janela de contexto está enchendo, começa a truncar tarefas e apressar conclusões prematuramente. 

O Antigravity Kit resolve isso eliminando o peso do passado. Utilizando a camada `.specs/` e inspirado no **Ralph Wiggum Loop**, o framework quebra o desenvolvimento em tarefas atômicas. A cada nova iteração, a memória do chat é aniquilada. A IA "renasce" com uma janela de contexto 100% limpa, orientando-se apenas pelo arquivo `STATE.md` atualizado autonomamente. O sistema de arquivos torna-se a memória perfeita e indestrutível, enquanto a IA foca toda a sua capacidade cognitiva exclusivamente no problema atual.

### A Nossa Realidade: Engenharia para PMEs

A literatura e os experimentos da OpenAI demonstraram que é possível gerar 1 milhão de linhas de código sem intervenção humana, mas eles o fizeram com recursos quase ilimitados. O Antigravity Kit é a resposta de guerrilha para essa tecnologia. 

Não temos equipes para manter clusters de Kubernetes ou ferramentas complexas de *MLOps*. **Nossa barreira arquitetural é a nossa maior força.** Optamos por uma governança leve: usamos `.md`, `.json` e `.sql` como banco de dados de estado. Nossas verificações (`secrets_scanner`, validação de timezone) rodam via *pre-commit* local, sem dependências externas. O *Harness* protege o orçamento financeiro das operações da mesma forma que protege a integridade do código.

### O Horizonte: A Engenharia de Concepção

Olhando para o futuro, o desafio não é mais gerar código, mas sim garantir que estamos gerando o produto certo. É aqui que entra o nosso módulo **INCEPTION.md**. Ele é o útero criativo — o lugar onde o humano despeja sua visão literária, suas incertezas e a sua "Vibe" de negócio.

O futuro do framework reside na consolidação do **Spec Enricher**, um agente de Nível 0 que atua como um caçador de lacunas. Ao ler o *Inception*, esse agente identificará programaticamente os buracos na estratégia (por exemplo, "O usuário quer integração META, mas não temos os custos de API"). Inspirados pelas redes de **Grafos de Conhecimento (Knowledge Graphs)**, especulamos que, em breve, essas lacunas serão mapeadas de forma matemática através do Oráculo. O agente não apenas apontará o que falta, mas direcionará pesquisas profundas (via *Deep Research*) para ferramentas como o NotebookLM, populando autonomamente nossa pasta `market/` antes que o primeiro Documento de Requisitos (PRD) seja sequer rascunhado. 

### Conclusão

O H.O.K Forge v2.5.2 framework não é apenas um *template* de software; é a materialização de uma nova filosofia de trabalho. Aceitamos que IAs são motores estocásticos e falíveis, e ao aceitarmos isso, construímos o chassi de aço que as torna seguras, autônomas e brilhantes. Deixamos de ser digitadores de sintaxe para nos tornarmos arquitetos de intenção e de governança. O código do futuro não será apenas gerado; ele será governado.

```
CHUNK_END id=d2f31e4696a6_c001
FILE_END id=file_d2f31e4696a6

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=17 bytes=827 mtime=2026-04-21T23:31:39.053793+00:00 sha1=e56f0939f55e5a0897bf89642150226cb048abd1
CHUNK_START id=9b6470da8849_c001 start_line=1 end_line=17
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-21
Status: Ativo
---

# 🏗️ ARCHITECTURE: Pipeline de Classes & Fluxos
> 🤖 [SYSTEM HOOK] NÃO preencha antes de `schema.sql` existir. Siga DB-First.
> 📐 Formato: [Componente] → [Responsabilidade] → [Dependência] → [Endpoint/Route]
> ⚠️ REGRA DE MOCK: Se DB não estiver disponível, mockar em `src/__mocks__/` com o EXATO formato do `schema.sql`. Proibido inventar campos não declarados.

## 📦 Estrutura Atual (Exemplo)
| Camada | Arquivo/Dir | Função | SSOT Vinculado |
|--------|-------------|--------|----------------|
| DB | `maintenance/schema.sql` | Verdade estrutural | `run_context.py sync` |
| API | `src/api/` | Rotas, validação, auth | `schema.sql` + `PRD.md` |
| UI | `src/components/` | Interface, estado | `rx-anatomy.md` |

```
CHUNK_END id=9b6470da8849_c001
FILE_END id=file_9b6470da8849

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=484 bytes=23416 mtime=2026-04-23T18:31:41.954752+00:00 sha1=bd90ab9ecbe4fffe87df6802cc68e0159123010b
CHUNK_START id=019509328844_c001 start_line=1 end_line=300
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-23 12:06
Status: Ativo
---

# JOURNAL.md
> Log vivo de decisoes e bugs. (Max 600 linhas)

## 📅 2026-04-23 15:31
**Decisão/Bug:** 🛡️ Hardening do Script de Captura (Anti-Bloat & Privacy).
**Solução:** 
1. Atualizado `captura_projeto.py` (v2.5.2) para ignorar globalmente as pastas `_archive_context`, `planos` e `RAW`.
2. Implementado isolamento cirúrgico para a camada `market/RAW`, impedindo que dossiês de pesquisa pesados contaminem o contexto de codificação da IA.
3. Sincronizada a versão interna do script com o baseline do projeto.
**Implicação:** Blindagem definitiva contra "Context Anxiety". A IA agora recebe apenas conhecimento destilado, ignorando o lixo histórico e os planos de rascunho.
**Evidência Operacional:** `npm run context:capture` gerou `contexto_v2.5.2.md` com sucesso, respeitando as novas exclusões.
**Handoff:** @antigravity-agent -> @user | Estado: Captura Hardened | Próximo: Encerrar ciclo.

## 📅 2026-04-23 13:14
**Decisão/Bug:** ✅ Hardening de Consistência de Versão (v2.5.2 Alignment).
**Solução:** 
1. Sincronização dos arquivos `README.md` e `README_CONTEXT.md` para refletir o baseline **v2.5.2**.
2. Atualização das referências de versão no `RULES.md` para precisão técnica.
3. Validação via pipeline `context:all` garantindo zero drift entre `VERSION.md` e o ecossistema documental.
**Implicação:** Erradicação de drift narrativo. Futuros agentes operando no framework agora herdam as travas de segurança e regras corretas da v2.5.2 sem ambiguidade.
**Evidência Operacional:** Execução de `npm run context:all` resultou em `Exit 0`.
**Handoff:** @antigravity-agent -> @user | Estado: Versão Sincronizada | Próximo: Avaliação Git.

## 📅 2026-04-23 12:06
**Decisão/Bug:** ✅ v2.5.2 aplicado para segregação de validação em specs `standard`.
**Solução:**
1. Criado o template oficial `.specs/_template.md` com os campos `type`, `executor_context_id`, `validator_context_id`, `definition_of_done`, `qa_signoff` e `signed_by`.
2. Atualizados `brain/MASTER_FLOW.md` e `brain/RULES.md` para formalizar que `type: standard` exige `executor_context_id != validator_context_id` antes de assinatura QA.
3. Atualizado `.context/_scripts/harness_runner.py` para bloquear (`Exit 1`) specs `standard` com IDs ausentes/nulos/iguais, preservando compatibilidade das specs legadas sem `type`.
**Implicação:** A assinatura de QA em sprint `standard` passa a exigir proveniência independente de contexto, reduzindo validação auto-referente.
**Evidência Operacional:** Execução local validada com três cenários (IDs iguais = FAIL; IDs distintos = PASS; spec legado sem `type` = PASS).
**Handoff:** @qa-validator -> @user | Estado: v2.5.2 aplicado | Próximo: Commit das mudanças.

## 📅 2026-04-22 21:10
**Decisão/Bug:** 🧠 Salto Evolutivo: Governança por Evidência e Honestidade Técnica (Skills Upgrade).
**Solução:** 
1. `hok-governor` (v1.2.0): Injetada a **Lei 8 (Espelhamento de Metadados)** para erradicar drifts narrativos de versão.
2. `flash-harness` (v1.1.0): Injetado o **Gate de Evidência Operacional** e a **Regra Anti-Leniência**.
**Implicação:** O framework agora proíbe retórica inflada ("atômico", "seguro") sem prova mecânica e exige visualização de logs/saídas para fechamento de tasks. O Antigravity Kit aprendeu com os erros de drift da release v2.5.1 e codificou a solução no seu "córtex central" (skills).
**Handoff:** @vision-architect -> @user | Estado: Skills Hardened (v2.5.1 Ready) | Próximo: Novo Ciclo.

**Decisão/Bug:** 🚨 Reforço Estrutural: Correção da Vulnerabilidade de Bypass do Linter (Fail-Closed).
**Solução:** Alteramos o `harness_runner.py` de "Fail-Open" para "Fail-Closed". Antes, se não houvesse *spec*, o script dava 'skip' e liberava o commit. Agora, a ausência de uma Spec ativada na pasta `.specs/` aciona imediatamente `Exit 1` (BLOQUEIO). A física do projeto tornou-se inflexível quanto ao Contrato de Sprint.
**Implicação:** Nenhum Agente (nem mesmo o Master) e nenhum Dev pode empurrar código à força bruta para o repositório sem assinar uma spec e colocar o YAML com `definition_of_done` e `qa_signoff: true`.
**Handoff:** @vision-architect -> @user | Estado: Zero Trust. | Próximo: Aguardar novos rumos.

## 📅 2026-04-21 19:00
**Decisão/Bug:** 👑 Declaração Oficial de Release: Antigravity v2.5 (Karpathy Hardened).
**Solução:** O agente @spec-driver (Flash) concluiu com sucesso o plano de infraestrutura Fase 3. O Oráculo agora opera com privilégio mínimo (`WIKI/` e `compliance/`) e indexação densa. O Workhop (`.specs/`) foi limpo. O agente @vision-architect (Pro) realizou o C-Level Audit (`npm run context:all`), selando a integridade epistemológica do projeto.
**Implicação:** A governança atingiu o nível onde as alucinações táticas de IAs terceiras estão mitigadas tanto pela política de destilação de contexto quanto pela exigência do "Protocolo Anti-Atropelo".
**Handoff:** @vision-architect -> @user | Estado: PRODUÇÃO (v2.5) | Próximo: Encerrar ciclo de hardening.

## 📅 2026-04-21 15:25
**Decisão/Bug:** 🛡️ Hardening v2.5: Implementação do Protocolo Anti-Atropelo.
**Solução:** Atualizada a skill `flash-harness` incorporando a "Cláusula de Inteligência Nativa" (Pro=Opcional, Flash=Obrigatório) e o "Bypass TRIVIAL".
**Implicação:** Otimização de tokens no Gemini Pro e eliminação de edições por presunção no Gemini Flash. O modelo Flash agora opera sob o "Cerco ao Objetivo" (Proposta -> GO -> Execução).
**Handoff:** @spec-enricher -> @user | Estado: Governança Refinada | Próximo: Aguardar GO.

## 📅 2026-04-21 14:53
**Decisão/Bug:** 📁 Arquivamento do Plano Fase 3 (Karpathy Wiki).
**Solução:** Finalizada a rodada de avaliação crítica (The Fool / Pros / Consiglieri). Planos gerados por agentes de execução foram deletados e o plano de arquitetura refinado ("Veredito Qwen") foi salvo em `.context/planos/`.
**Implicação:** O projeto não sofreu alterações de código, mas possui agora o blueprint oficial para escalabilidade "Zero RAG".
**Handoff:** @vision-architect -> @user | Estado: Plano Arquivado | Próximo: Aguardar execução.

## 📅 2026-04-21 13:20
**Decisão/Bug:** 🛡️ Implementação da Skill `flash-harness` (Governança Flash).
**Solução:** Criada e ativada a skill global `flash-harness`. Ela impõe o protocolo de Desaceleração Cognitiva via `<thought_process>` para compensar o viés de pressa do modelo Gemini Flash.
**Implicação:** Drástica redução de alucinações táticas. O modelo agora é forçado a realizar Auditoria Epistêmica e Ancoragem no Framework antes de gerar qualquer output técnico.
**Handoff:** @vision-architect -> @governance-agent | Estado: Flash Hardened | Próximo: Produção.

## 📅 2026-04-21 00:23
**Decisão/Bug:** 🛑 Implementação da Regra 6 (Protocolo de Estudo Tectônico) no Governor.
**Solução:** Injetada a trava anti-entropia na skill global `hok-governor`, obrigando a IA a realizar um estudo de natureza funcional do arquivo antes de propor mudanças e proibindo redundâncias no `.context`.
**Implicação:** Blindagem definitiva contra "gambiarras" arquiteturais e fragmentação de contexto por criação de arquivos desnecessários.
**Handoff:** @antigravity-agent -> @user | Estado: Governança Fortalecida (v2.4.1+) | Próximo: Encerrar dia.

## 📅 2026-04-20 12:15
**Decisão/Bug:** 🛡️ Hardening de Governança & Roteamento do Oráculo.
**Solução:** 
1. Implementado o `market/SSOT_MAP.md` como roteador central para o NotebookLM (Oracle Baseline).
2. Injetados **Harnesses Preventivos** (Sticky Instructions) no topo de `INCEPTION.md`, `rx-anatomy.md` e `rx-biology.md` para blindar o contexto contra poluição de IAs.
3. Atualizada a skill global `hok-governor` com a Regra 5 (Bússola Cognitiva).
**Implicação:** O sistema agora possui auto-defesa documental e uma ponte clara e desacoplada para a base de conhecimento externa na nuvem (NotebookLM).
**Handoff:** @antigravity-agent -> @user | Estado: Template Hardened e Blindado | Próximo: Implementação de novas features.

## 📅 2026-04-16 23:58
**Decisão/Bug:** 🚩 [SAVEPOINT] Hardening v2.4.1 Concluído (Dogfooding Total).
**Estado Atual:** O sistema está em modo `ACTIVE`, com o motor Python (`run_context.py`) consolidado como SSOT de execução. O "Execution Drift" foi erradicado: `Makefile`, `run_context.sh` e `init_ai_project.sh` são agora wrappers seguros.
**Pendências:** 
  1. Iniciar ciclo de desenvolvimento de novas features seguindo o fluxo `VISION -> INCEPTION -> SPECIFY`.
  2. Monitorar o `CONTEXT_HEALTH.md` conforme o volume de código crescer.
**Handoff:** @antigravity-agent -> @user | Estado: Sistema Blindado e Sincronizado | Próximo: Novas Features.

## 📅 2026-04-16 22:20
**Decisão/Bug:** 🧭 [MODE: HYBRID_DISCOVERY] Implementação The Fool's Cut e Eng. de Guerrilha Concluída.
**Solução:** Atualização cirúrgica na governança documental (PRD, RULES, TECHNICAL_REQUIREMENTS). O PRD oficializado como template livre do framework, e a equação 'Agente = Modelo + Harness' formalizada nas RULES.
**Implicação:** A documentação mestre do framework está totalmente alinhada ao paradigma do Ralph Wiggum Loop e da Tríade H.O.K., prevenindo que IAs injetem filosofia do framework nas features do produto do usuário.

## 📅 2026-04-15 14:50
**Decisão/Bug:** 🛡️ Antigravity Kit v2.4.1-Hardened CONCLUÍDO.
**Solução:** Patches cirúrgicos nos scripts core, ativação da camada Inception/Market e isolamento de path no bundle. Pipeline Fail-Fast validado.
**Implicação:** O template oficial agora opera no modo v2.4.1-Hardened, com governança estratégica blindada e redução drástica de alucinações via Market layer.


## 📅 2026-04-14 10:35
**Decisão/Bug:** 🔄 Handoff: @governance-agent → @vision-architect | Estado: Patches v2.3.1 Resolvidos | Próximo: Ativar camada Inception
**Solução:** H.O.K Hardening integrado (fail-fast, rx-biology, project_mode).
**Implicação:** A partir de agora, o desenvolvimento da camada Inception/Market utilizará 100% da própria governança (Dogfooding).

## 📅 2026-04-14 12:00
**Decisão/Bug:** ✅ Camada Inception + Market (v2.4.0) Ativada
**Solução:** Implementada estrutura de Market/, templates Inception e logic de STRATEGIC_ALIGNMENT no Harness. Dogfooding concluído.
**Implicação:** O pipeline H.O.K. agora protege contra drift estratégico, falhando se o PRD violar boundaries definidos no Inception. 🔄 Handoff: @vision-architect -> @dev-ops | Estado: Validado | Próximo: Teste.

## 📅 2026-04-14 13:10
**Decisão/Bug:** 🛡️ Hardening do Prompt @vision-architect (v2.4.1)
**Solução:** Injetada hierarquia explícita de SSOT, instrução de sintaxe para Harness e limite de 3 parágrafos para o VIBE.
**Implicação:** Redução de alucinações estratégicas e garantia de que boundaries escritos serão capturados pelo pipeline.

## 📅 2026-04-11 01:25
**Decisão/Bug:** 🔄 Handoff: @frontend-specialist → @backend-engineer | Estado: UI Completa | Próximo: Setup DB
**Solução:** Implementada UI do CheckoutForm v1 usando Stripe Elements. Estado local gerenciado; aguardando API `/api/checkout/session`.
**Implicação:** Próximo agente deve configurar a rota backend e garantir o retorno do `clientSecret`.

## 📅 2026-04-11 01:35
**Decisão/Bug:** 🔄 Handoff: @backend-engineer → @qa-validator | Estado: API webhook pronta | Próximo: Testar hooks
**Solução:** Endpoint Stripe Session operacional. Webhook configurado para escutar `payment_intent.succeeded` e atualizar tabela `orders`.
**Implicação:** QA deve validar fluxos de falha e idempotência do webhook.

## 📅 2026-04-11 01:45
**Decisão/Bug:** ✅ Ciclo Checkout Stripe Concluído
**Solução:** Cobertura de testes em 92%. Validado happy path e 'card declined'. Injetado retry pattern no webhook.
**Implicação:** PRD #15 concluído. Tecnologias Stripe adicionadas ao env.

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## Teste Epistemológico
> Fonte: raw/stripe_docs.md
O sistema garante a idempotencia de eventos cruzado com as webhooks da Stripe.

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:hok-advanced-modules
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:manual
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** strategy: PRD viola boundaries estrategicas: ['usar mongoDB']

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** strategy: PRD viola boundaries estratégicas: ['mongoDB']

## [SESSION-COMPLETE] Antigravity Kit v2.4.1 Hardened
- **Meta-Ação:** Re-Baseline completo da infraestrutura e camada estratégica.
- **Destaques:** 
  - Scripts Hardened (Unicode, JSON Allowlist, Surgical Isolation).
  - Camada Market operacional com indexação dinâmica no Oracle.
  - Fail-fast estratégico validado via Harness Runner.
- **Status:** [PRODUCTION READY]
- **Próximo:** Iniciar ciclo de desenvolvimento de features na Versão 2.4.1.

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** enrichment: Seção Critical Dependencies obrigatória para PRDs com integrações/compliance

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** enrichment: Dependencies sem lastro em market/: ['- LGPD (faltando fonte)']

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid


## [2026-04-15 16:17] release: Spec Enricher v2.4.1-Hardened
- **Status:** Ativado e validado via H.O.K.
- **Ritual:** @vision-architect ⮕ @spec-enricher (Exit 2) ⮕ @spec-driver.
- **Harness:** Adicionada validação de contract de Critical Dependencies.

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid


```
CHUNK_END id=019509328844_c001
CHUNK_START id=019509328844_c002 start_line=301 end_line=484
```markdown
## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** enrichment: Seção Critical Dependencies obrigatória para PRDs com integrações/compliance

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: @governance-agent → @vision-ar', 'Handoff incompleto: @vision-architect -> @dev-ops.', 'Handoff incompleto: @frontend-specialist → @backen', 'Handoff incompleto: @backend-engineer → @qa-valida']

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: @governance-agent → @vision-ar', 'Handoff incompleto: @vision-architect -> @dev-ops.', 'Handoff incompleto: @frontend-specialist → @backen', 'Handoff incompleto: @backend-engineer → @qa-valida', "Handoff incompleto: Handoffs malformados: ['Handof"]

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** handoff: Handoffs malformados: ["Handoff incompleto: Handoffs malformados: ['Handof", "Handoff incompleto: Handoffs malformados: ['Handof"]

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:_template
- **Detalhe:** sprint_contract: Contrato não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-FAIL] Report | spec:_template
- **Detalhe:** sprint_contract: Contrato não assinado pelo @qa-validator (qa_signoff: false)

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** @spec-enricher -> @user | E']

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:meta-inception
- **Detalhe:** handoff: Handoffs malformados: ['Handoff incompleto: ** @vision-architect -> @user ']

## [HARNESS-PASS] Report | spec:meta-inception
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [2026-04-22 09:50] release: Antigravity Kit v2.5.0 'Hardened Matrix'
- **Meta-Ação:** Implementação de SSOT de Versão e Endurecimento de Onboarding (Arquiteto).
- **Destaques:** 
  - `version_targets.json` ⮕ Matriz declarativa de sincronia de versão.
  - `check_version_consistency.py` ⮕ Linter de drift integrado ao pipeline `all`.
  - `harness_runner.py` ⮕ Poda real de arquivos e fail-closed para `DRAFT` quando há atividade.
- **Status:** [CONSISTENT & HARDENED]
- **Próximo:** Iniciar ciclo de desenvolvimento de features sobre fundação v2.5.0.

---

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:harness_fail_closed
- **Detalhe:** All contracts valid

## [HARNESS-FAIL] Report | spec:wiki_level2
- **Detalhe:** sprint_contract: Bloco de contrato (---) ausente no topo da spec

## [HARNESS-FAIL] Report | spec:wiki_level2
- **Detalhe:** sprint_contract: Campo definition_of_done obrigatório

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

## [HARNESS-PASS] Report | spec:wiki_level2
- **Detalhe:** All contracts valid

```
CHUNK_END id=019509328844_c002
FILE_END id=file_019509328844

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=128 bytes=989 mtime=2026-04-23T16:13:09.768560+00:00 sha1=d37f5068cfdd73f955c65746e68629891162e2a9
CHUNK_START id=d069d4f2ebef_c001 start_line=1 end_line=128
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-10 20:50
Status: Ativo
---

## 🚫 Restrições de Infraestrutura (Guerrilha)
> O Antigravity Kit (H.O.K Forge) atua como um sistema para PMEs. Fica expressamente **proibida** a introdução das seguintes tecnologias no core, limitando o AI Slop e a dívida técnica:
- **Kubernetes (K8s)** ou Orquestradores Complexos.
- **Bancos Vetoriais (Vector DBs)** para busca de contexto (usar stdlib-only).
- **Infraestruturas MLOps Pesadas**.

## 🔧 Requisitos Mínimos (Motor)
Para execução segura dos scripts de governança (Harness e Oracle):
- **Python:** `>= 3.10`
- **Node.js:** `>= 18.x` (para pacotes de pre-commits automáticos)

<!-- AUTO-SYNC START -->
*🤖 Atualizado automaticamente em 2026-04-23 13:13*

### DevDependencies
- `husky`: `^9.1.7`

### Tabelas no Schema (schema.sql)
- `orders`

<!-- AUTO-SYNC END -->






































































































```
CHUNK_END id=d069d4f2ebef_c001
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=14 bytes=487 mtime=2026-04-21T23:31:41.224778+00:00 sha1=41caf1bd5e6bf513c1924db0b4dca9fb6f92322b
CHUNK_START id=0858a02cf53f_c001 start_line=1 end_line=14
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-21
Status: Ativo
---

# 🧪 TESTS: Cobertura & Framework
> 🤖 [SYSTEM HOOK] Nenhum caso de negócio opera sem cobertura declarada aqui.
> 🔧 Declare o stack: `[TODO] Jest/Pytest/Vitest? Cobertura alvo?`

## 📋 Matriz de Casos Críticos
| Módulo | Happy Path | Edge Case 1 | Edge Case 2 | Status |
|--------|------------|-------------|-------------|--------|
| `[TODO]` | `[TODO]` | `[TODO]` | `[TODO]` | ❌ Pendente |

```
CHUNK_END id=0858a02cf53f_c001
FILE_END id=file_0858a02cf53f

---
<a id="file_3707c3aa3239"></a>
FILE_START id=file_3707c3aa3239 path=.context/maintenance/migrations/001_init.sql domain=db lang=sql lines=12 bytes=450 mtime=2026-04-12T02:14:15.429255+00:00 sha1=a4e5465634cd084041656f59f9093be09f5a8fc9
CHUNK_START id=3707c3aa3239_c001 start_line=1 end_line=12
```sql
-- 🗄️ Migration 001: Estrutura base (DB-First)
-- Este arquivo foi detectado pela governança H.O.K.
-- As regras definem que todo novo campo deve nascer em uma nova migration (002_*.sql) etc.

-- Exemplo:
-- CREATE TABLE IF NOT EXISTS users (
--     id SERIAL PRIMARY KEY,
--     email VARCHAR(255) UNIQUE
-- );

-- Apos popular este arquivo inicial, execute "npm run context:sync"
-- para que os agentes de IA saibam da existencia dos campos.

```
CHUNK_END id=3707c3aa3239_c001
FILE_END id=file_3707c3aa3239

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CHUNK_START id=a5c71962029a_c001 start_line=1 end_line=63
````markdown
---
Criado em: 2026-04-10 21:44
Ultima Atualizacao: 2026-04-10 21:44
Status: Ativo
---

# 🛠️ Manual de Reconstrução & Automação

Este guia contém as instruções para subir o ambiente do zero e operar as ferramentas de governança de contexto.

---

## 🏗️ 1. Setup do Ambiente

### Requisitos Mínimos:
- **Python ≥ 3.8** (Para os scripts de automação)
- **Node.js** (Para os wrappers NPM)
- **Make** (Opcional, para orquestração Unix)
- **Bash** (Para Git Bash, WSL, Linux ou macOS)

---

## ⚙️ 2. Ferramentas de Automação

O projeto oferece três formas de gerenciar a saúde do contexto. Escolha a que melhor se adapta ao seu terminal:

### Opção A: Via NPM (Recomendado para Devs Web)
```bash
npm run context:validate  # Checa integridade e tokens
npm run context:sync      # Sincroniza deps e schema
npm run context:purge     # Limpa e arquiva o log vivo
```

### Opção B: Via Make (Recomendado para CI/CD e Unix)
```bash
make validate
make sync
make purge
make all       # Executa o pipeline completo: Valida -> Sync -> Purge
```

### Opção C: Via Bash (Resiliência Universal)
```bash
./run_context.sh validate
./run_context.sh all
```

---

## 🗃️ 3. Recuperação de Contexto (Archive)

Se precisar restaurar um Journal ou PRD antigo que foi arquivado:
1. Vá até `.context/maintenance/_archive_context/`.
2. Localize o arquivo pelo timestamp `YYYYMMDD_HHMMSS`.
3. Copie o conteúdo necessário de volta para a raiz da camada correspondente (`maintenance/` ou `brain/`).

---

## 🚨 4. Troubleshooting
- **Erro de Encoding (Windows):** Todos os scripts são forçados para UTF-8. Se vir caracteres estranhos, verifique se o seu terminal suporta Unicode.
- **Python não encontrado:** No Windows, o script tenta `python3` e faz fallback para `python`. Se falhar, certifique-se que o executável está no seu PATH.

> *Lembrete: Sem automação, a documentação morre. Use as ferramentas a cada nova funcionalidade iniciada no ROADMAP.md.*

````
CHUNK_END id=a5c71962029a_c001
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=36 bytes=2178 mtime=2026-04-20T14:46:26.673206+00:00 sha1=34ca91d2500a5683e58506f31c7ebad4abc34939
CHUNK_START id=54a6a553d34b_c001 start_line=1 end_line=36
```markdown
---
Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-10 23:27
Status: Ativo
---

# 🧬 rx-anatomy.md (Raio-X de Anatomia)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita EXCLUSIVAMENTE a Estrutura de Pastas Físicas do repositório.
> - **NÃO** insira regras de negócio, fluxos lógicos ou contratos de base de dados aqui.
> - **NÃO** adicione dependências de infraestrutura de pacote (use `TECHNICAL_REQUIREMENTS.md`).
> - Se você está editando as linhas abaixo, você deve estar criando ou justificando uma PASTA FÍSICA no disco.

> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # 🏛️ CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Regras, PRD e Fronteiras (VISION/INCEPTION)
│   ├── market/             # Camada Estratégica (SSOT, Limits, Compliance)
│   ├── maintenance/        # Logs (JOURNAL), Schema e Inventários
│   ├── monitoring/         # Dashboard de Saúde (CONTEXT_HEALTH.md)
│   └── _scripts/           # Motor de Validação em Python (Oráculo, Harness)
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.py          # ⚙️ Orquestrador Universal Python (SSOT de Execução)
├── init_ai_project.sh      # Bootstrapper Supremo (injeta python no NPM)
└── package.json            # Gerenciamento de libs e rotas context:* (Npm scripts)

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `.context/maintenance/_archive_context/specs/`
- **Isolamento:** Não é fonte da verdade. O `.context/` permanece como SSOT. As specs são submetidas à validação do Harness (`run_context.py harness`).

```
CHUNK_END id=54a6a553d34b_c001
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=31 bytes=2068 mtime=2026-04-20T14:46:28.695155+00:00 sha1=b9830614be78ced5077a6accd008a9bb41f5fe2a
CHUNK_START id=ca8da4f87431_c001 start_line=1 end_line=31
```markdown
---
Criado em: 2026-04-14
Ultima Atualizacao: 2026-04-16
Status: Ativo (v2.4.1-Hardened)
---

# 🧬 rx-biology.md (Raio-X de Comportamento AI)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita como as IAs interagem com a máquina de estados (O MODO DE PENSAR e HANDOFF).
> - **NÃO** descreva arquiteturas de banco de dados ou diagramas de componentes de software aqui.
> - **NÃO** adicione regras de compilação ou deploy (use os scripts raiz ou `.github/`).
> - Foco 100% no Ralph Wiggum Loop e regras comportamentais entre Agentes.

> Documenta as biológicas de interação, limites cognitivos e padrões de resposta esperados da IA orbitando a Tríade H.O.K Forge.

## 🧠 Modus Operandi (O Ralph Wiggum Loop)
As IAs devem atuar de forma **efêmera e cirúrgica**:
1. **Foco Atômico:** Ignorar abstrações além do estritamente necessário para resolver a Spec atual. 
2. **Ciclo de Amnésia:** Uma vez que a tarefa ou conjunto de specs termina, os resultados difíceis ("lições ganhas") são transferidos para o `JOURNAL.md` e o loop "esquece" o resto. A memória reside no `FileSystem (.context/)`.

## 🛡️ Handoff & Cruzamento de Domínio
A integridade da continuidade é garantida pelas transferências no _JOURNAL.md_. O Formato Oficial cobrado pelo `harness_runner.py`:
- `🔄 Handoff: @[role-atual] -> @[role-próxima] | Estado: [Status técnico] | Próximo: [O que precisa ser feito]`

## 🔍 Comportamento Epistemológico (Regra Karpathy)
A IA não tem permissão para assumir dogmas técnicos (claims) sem citar a fonte da documentação original:
- Todo conselho ou decisão estrutural no `.context/` deve vir acompanhado de `> Fonte: raw/nome-do-arquivo.md`.
- **Tratamento de Erro:** Em caso de dúvida técnica ou ausência de documentação de referência cruzada, acione o `npm run context:oracle`. Nunca adivinhe requisitos.

> 🛠️ **Diretriz de Segurança:** Todo o roteamento é impulsionado por `run_context.py`. Evite invocar scripts bash de baixo nível se houver comandos npm (`context:*`) mapeados.

```
CHUNK_END id=ca8da4f87431_c001
FILE_END id=file_ca8da4f87431

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CHUNK_START id=91d5627a725e_c001 start_line=1 end_line=9
```sql
-- Snapshot Real da Tabela de Pedidos
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    stripe_session_id VARCHAR(255),
    status VARCHAR(50) DEFAULT 'pending', -- pending, succeeded, failed
    total_amount DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

```
CHUNK_END id=91d5627a725e_c001
FILE_END id=file_91d5627a725e

---
<a id="file_51ed93c9d8ab"></a>
FILE_START id=file_51ed93c9d8ab path=.context/maintenance/version_targets.json domain=config lang=json lines=22 bytes=538 mtime=2026-04-22T12:37:34.654694+00:00 sha1=c2279f3056490c43cd112154c87f7b6b97e852ac
CHUNK_START id=51ed93c9d8ab_c001 start_line=1 end_line=22
```json
{
  "ssot": "VERSION.md",
  "targets": [
    {
      "path": "package.json",
      "pattern": "\"version\"\\s*:\\s*\"([^\"]+)\"",
      "mode": "must_match"
    },
    {
      "path": ".context/brain/INCEPTION.md",
      "pattern": "^version:\\s*([0-9]+\\.[0-9]+(?:\\.[0-9]+)?)\\s*$",
      "mode": "must_match",
      "multiline": true
    },
    {
      "path": ".context/brain/VISION.md",
      "pattern": "^Framework Version:\\s*v?([0-9]+\\.[0-9]+(?:\\.[0-9]+)?)\\s*$",
      "mode": "must_match",
      "multiline": true
    }
  ]
}

```
CHUNK_END id=51ed93c9d8ab_c001
FILE_END id=file_51ed93c9d8ab

---
<a id="file_81ef387da7b7"></a>
FILE_START id=file_81ef387da7b7 path=.context/market/MARKET_INBOX.md domain=docs lang=markdown lines=11 bytes=341 mtime=2026-04-15T19:15:21.935146+00:00 sha1=66adcca82c5eae73d386371aef29795c87e283b3
CHUNK_START id=81ef387da7b7_c001 start_line=1 end_line=11
```markdown
---
version: 2.4.1
type: INBOX
---

# 📥 MARKET_INBOX

| Data | Gap/Gap de Pesquisa | Status | Fonte Relacionada |
|------|--------------------|--------|-------------------|
| [Data] | [Descrição do Gap] | `[TODO: research]` | [Referência] |
| Integração LGPD | `> Fonte: raw/docs_oficiais.md` | Crítica | 🔍 Pesquisa | 2026-04-15

```
CHUNK_END id=81ef387da7b7_c001
FILE_END id=file_81ef387da7b7

---
<a id="file_65a089176b85"></a>
FILE_START id=file_65a089176b85 path=.context/market/SSOT_MAP.md domain=docs lang=markdown lines=26 bytes=1842 mtime=2026-04-20T14:12:07.881449+00:00 sha1=817fcdf3b98f82a751294e12763163f975e890db
CHUNK_START id=65a089176b85_c001 start_line=1 end_line=26
```markdown
---
version: 2.4.1
type: GOVERNANCE
---

# 🗺️ SSOT_MAP: Roteador do Oráculo & Hierarquia da Verdade

> **💡 TEMPLATE CLONE - INSTRUÇÃO OBRIGATÓRIA (Para Humanos & IAs)**
> Como este é um template (`template_inicío_de_projeto`), o ID do Oráculo abaixo aponta para a base de conhecimento estrutural do próprio template (sobre como usar o H.O.K). **Logo após clonar este repositório para iniciar um novo negócio, o humano DEVE criar um novo Notebook no NotebookLM e a IA DEVE vir aqui atualizar o ID abaixo.**

## 🔮 Oracle Baseline (Memória Externa)
O NotebookLM armazena o "Contexto Massivo" contínuo (PDFs, pesquisas, históricos detalhados) que saturaria nosso limite local de tokens. Agentes como `@vision-architect` e `@spec-enricher` o utilizam como extensão cerebral primária.

- **`oracle_mcp_id`:** `8979de2f-a111-4856-8a71-197d6b9ec876` *(ID do Oráculo - Altere no pós-clone!)*
- **Comportamento da IA:** Consulte usando ferramentas do MCP (`mcp_notebooklm_chat_with_notebook`) sempre que a informação transcender a raiz do código.

## 🏗️ Hierarquia da Verdade Local (SSOT)
Ordem de precedência (o nível superior sempre anula o inferior):

1. `🔮 Oráculo Externo (NotebookLM)`: Literatura de mercado, manuais extensos e macro-histórico.
2. `market/compliance/*.md`: Regras imutáveis de negócio locais (Leis, Controles).
3. `brain/INCEPTION.md`: Visão estratégica, regras comportamentais (NUNCA/SEMPRE).
4. `brain/PRD.md`: Regras do produto e fluxo transacional atual.
5. `maintenance/schema.sql`: O contrato final implementado tecnicamente.

⚠️ **Conflito Nuvem vs Local:** Em caso de divergência entre o Oráculo (Mercado/Visão) e os arquivos locais, a IA deve disparar um alerta e o Humano deve arbitrar quem detém a verdade correta no momento (Paradigma da Lei 3 - Hok Governor).

```
CHUNK_END id=65a089176b85_c001
FILE_END id=file_65a089176b85

---
<a id="file_578d56cac1a4"></a>
FILE_START id=file_578d56cac1a4 path=.context/market/WIKI/_index.md domain=docs lang=markdown lines=5 bytes=100 mtime=2026-04-22T23:08:43.528195+00:00 sha1=49feb4c64bb2f3a2838a667b4e78b5afb009b2e4
CHUNK_START id=578d56cac1a4_c001 start_line=1 end_line=5
```markdown
# WIKI Index Raiz
> Fonte: SSOT_MAP.md

## Topicos
- [[conceito_teste]] | tags: ecommerce, checkout

```
CHUNK_END id=578d56cac1a4_c001
FILE_END id=file_578d56cac1a4

---
<a id="file_491684f3a96e"></a>
FILE_START id=file_491684f3a96e path=.context/market/WIKI/_template.md domain=docs lang=markdown lines=26 bytes=451 mtime=2026-04-21T21:52:58.658989+00:00 sha1=cff3271c1a095ae525f40835ebdcf49adc208d3a
CHUNK_START id=491684f3a96e_c001 start_line=1 end_line=26
````markdown
---
entity: [Entidade Principal, ex: LGPD]
concept: [Conceito Específico, ex: Checkout]
tags: [tag1, tag2]
aliases: [sinonimo1, sinonimo2]
last_updated: 2026-04-21
source: RAW/[arquivo_origem].md
---

# [Título Descritivo]

> Fonte: RAW/[arquivo_origem].md

## Resumo
[Breve explicação do conceito]

## Regras / Fluxo
- [Regra 1]

## Exemplo Mínimo
```python
# Código de referência rápida
```

## Links Relacionados
- [[conceito_relacionado]]

````
CHUNK_END id=491684f3a96e_c001
FILE_END id=file_491684f3a96e

---
<a id="file_b5d38697335e"></a>
FILE_START id=file_b5d38697335e path=.context/market/economics.md domain=docs lang=markdown lines=7 bytes=109 mtime=2026-04-15T17:50:11.975520+00:00 sha1=17852efa34dbaea46351dcabac87aa67286e2e93
CHUNK_START id=b5d38697335e_c001 start_line=1 end_line=7
```markdown
---
version: 2.4.1
type: FINANCIAL
---

# 💰 Economics & Financials
- [Budget, custos de API, projeções]

```
CHUNK_END id=b5d38697335e_c001
FILE_END id=file_b5d38697335e

---
<a id="file_c255058b56fe"></a>
FILE_START id=file_c255058b56fe path=.context/market/wiki_log.md domain=docs lang=markdown lines=24 bytes=1756 mtime=2026-04-23T16:13:10.596559+00:00 sha1=b7c18915dc39c03f69bce97b65f9eff45eb05193
CHUNK_START id=c255058b56fe_c001 start_line=1 end_line=24
```markdown
# Wiki Log (Append-only)

| Timestamp | Mode | Description | Files | Status |
|-----------|------|-------------|-------|--------|
| [2026-04-22 20:08] | INIT | INITIALIZED WIKI LEVEL 2 FOUNDATION | _index.md, wiki_log.md | OK |
| [2026-04-22 20:35] | INGEST | Falha de conformidade Karpathy | market/WIKI/fail_log_test.md | FAIL |
| [2026-04-22 20:36] | INGEST | Ingestão de 1 artigos | fail_log_test.md | OK |
| [2026-04-22 20:36] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-22 20:37] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-22 20:37] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-22 20:37] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-22 20:37] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-22 20:47] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-22 20:47] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-22 20:47] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-22 20:48] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-23 11:30] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-23 11:30] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-23 11:44] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-23 11:44] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-23 11:45] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-23 11:45] | LINT | Integridade epistemológica validada | - | OK |
| [2026-04-23 13:13] | SKIP | Nenhum artigo detectado para ingestão | - | OK |
| [2026-04-23 13:13] | LINT | Integridade epistemológica validada | - | OK |

```
CHUNK_END id=c255058b56fe_c001
FILE_END id=file_c255058b56fe

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1506 mtime=2026-04-23T16:13:10.880297+00:00 sha1=81c613e83d0d6f6a61cd5b1158fcf5173268a56c
CHUNK_START id=068a21d64bec_c001 start_line=1 end_line=38
```markdown
---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-04-23 13:13
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Manutencao** | | | | |
| Linhas do Journal | 464 | 600 | Tracker | [OK] |
| Carga do Journal | 21k chars | 50k chars | Tracker | [OK] |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~41k | 128k (Max) | Eficiencia | [OK] |
| **Consistencia** | | | | |
| Tabelas no Schema | 1 | N/A | DB-First | [OK] |
| Migrations Pendentes | 1 file(s) | N/A | DB-First | [OK] |
| Ultimo Harness | Role Check | Pass/Fail | Integridade | [PASS] |
| Ultima Sincronia | 2026-04-23 13:13 | Real-Time | Automacao | [OK] |
<!-- HEALTH_TABLE_END -->

---

## 🚨 Regras de Degradação & Ações
- **Se Journal > 550 linhas ou > 45k char:** Ativar `@context-keeper` para rodar `_scripts/purge_journal.py`.
- **Se Schema vs PRD divergir:** Bloquear geração de UI até que a migration seja documentada.
- **Se Turns > 18:** Propor Snapshot ou Reset de Sessão antes de iniciar próxima tarefa grande.

---

## 📅 Histórico de Saúde (Log de Purges)
| Data | Ação | Agente | Resultado |
| :--- | :--- | :--- | :--- |
| 2026-04-10 | Purge Completo | @context-keeper | Journal resetado para seed de 30 linhas. |

```
CHUNK_END id=068a21d64bec_c001
FILE_END id=file_068a21d64bec

---
<a id="file_c6d44cc7da35"></a>
FILE_START id=file_c6d44cc7da35 path=.context/monitoring/EXECUTION_BUFFER.md domain=docs lang=markdown lines=10 bytes=327 mtime=2026-04-18T14:24:14.955191+00:00 sha1=d7989e55f1d5b4c9c8c2fa6057d6c8407b80e134
CHUNK_START id=c6d44cc7da35_c001 start_line=1 end_line=10
```markdown
---
status: ACTIVE
last_reset: 2026-04-18
---
# Odômetro de Execução (KBuM)

Este arquivo é a "memória de curto prazo" do H.O.K Governor. Toda ferramenta executiva da IA consome um "tick". Ao atingir 5 ticks, a execução entra em Checkpoint para atualizar a sanidade do projeto.

## Buffer Atual (Ticks Ocupados)
*vazio*

```
CHUNK_END id=c6d44cc7da35_c001
FILE_END id=file_c6d44cc7da35

---
<a id="file_37fb63b0fac5"></a>
FILE_START id=file_37fb63b0fac5 path=.context/specs/DIRECTIVA_V2.4.1_HARDENED.md domain=docs lang=markdown lines=174 bytes=8421 mtime=2026-04-15T17:41:55.756194+00:00 sha1=7b18093a0456bf1be767656576630ad229da9324
CHUNK_START id=37fb63b0fac5_c001 start_line=1 end_line=174
````markdown
# Plano de Implementação: Antigravity Kit v2.4.1-Hardened

Este plano detalha a aplicação da **Diretiva de Implementação v2.4.1-Hardened**, focando em patches cirúrgicos, segurança fail-fast e ativação da governança estratégica (Inception/Market).

## 🗺️ Mapa Visual da Arquitetura

Para garantir o entendimento determinístico da ordem temporal e lógica, os diagramas abaixo regem o comportamento dos agentes.

### 1. Fluxo de Execução Fail-Fast (`run_context.py`)
*O pipeline é uma esteira crítica. Qualquer falha em segurança, sincronia ou contrato interrompe o fluxo imediatamente.*

```mermaid
graph TD
    Start([npm run context:all]) --> Validate[1. validate_context.py]
    Validate -->|FAIL| Error([❌ EXIT 1: Build Quebrado])
    Validate -->|Integrity OK| Secrets[2. secrets_scanner.py]
    Secrets -->|FAIL: Hits Found| Error
    Secrets -->|Clean| Sync[3. sync_project.py]
    Sync -->|FAIL| Error
    Sync -->|Updated| Migrations[4. migration_registry.py]
    Migrations -->|FAIL: Order Broken| Error
    Migrations -->|Order OK| Harness{5. harness_runner.py}
    
    Harness -->|FAIL: Strategy/Schema| Error
    Harness -->|PASS: All Contracts| Lint[6. lint_wiki.py --strict]
    
    Lint -->|FAIL: Missing Source| Error
    Lint -->|Citations OK| Health[7. health_sync.py]
    Health -->|Updated| Done([✅ DONE: Pipeline Sucesso])
```

### 2. A Máquina de Estados do Projeto (`RULES.md`)
*Define o modo operacional e os critérios de transição de maturidade.*

```mermaid
stateDiagram-v2
    [*] --> BOOTSTRAP
    
    BOOTSTRAP: [BOOTSTRAP]
    note right of BOOTSTRAP
      Foco: Estrutura, Scripts, 
      Inception e Market Setup.
      Regras: Validação de diretórios.
    end note
    
    BOOTSTRAP --> HARDENING: JOURNAL Entry + Context Pass + Harness Validated
    HARDENING: [HARDENING]
    note right of HARDENING
      Foco: Segurança, CI/CD, 
      Scanners e Estabilidade.
      Regras: Zero falhas no Harness Pipeline.
    end note
    
    HARDENING --> PRODUCTION: Zero falhas em N sessões + Baseline v2.4.1
    PRODUCTION: [PRODUCTION]
    note right of PRODUCTION
      Foco: Features Reais.
      Market/ vira fonte estratégica prioritária (SSOT_MAP).
    end note
```

### 3. O Rito do Spec Enricher (Concepção → Execução)
*Inclui o estado Exit 2 para pesquisa pendente e o fluxo de incepção estratégica.*

```mermaid
sequenceDiagram
    participant Human
    participant Vision as @vision-architect
    participant Inception as INCEPTION.md
    participant Market as MARKET/ Folders
    participant Enricher as @spec-enricher
    participant PRD as PRD.md

    Human->>Vision: "Tenho uma ideia para X"
    Vision->>Inception: Escreve [Boundaries] (- NUNCA: X)
    Enricher->>Inception: Lê INCEPTION.md e escaneia Entidades
    Enricher->>Market: Verifica compliance/ e research/
    
    alt Exit 2: Research Needed
        Market-->>Enricher: Incerteza técnica ou Gaps
        Enricher->>Market: Registra em MARKET_INBOX.md [TODO]
        Enricher->>Human: ❌ EXIT 2: Pesquisa necessária. Popule market/
        Human->>Market: Insere fontes (Karpathy Rule)
        Note over Enricher, Market: Reinicia ciclo Enrich
    else Fontes Presentes
        Market-->>Enricher: Documentos encontrados
        Enricher->>Enricher: Valida viabilidade vs Boundaries
        Enricher->>PRD: Gera PRD.md lastreado (> Fonte: market/...)
        Note right of PRD: Pronto para Handoff TLC
    end
```

## User Review Required

> [!IMPORTANT]
> **Regra de Patch Rígida:** Não substituiremos arquivos inteiros. Faremos edições apenas nos blocos indicados para preservar a integridade das funções auxiliares.
> **Estado Atual:** Muitos componentes já possuem a lógica da v2.4.1 instalada. Este plano irá **formalizar, corrigir discrepâncias de string (acentuação, logs) e garantir a presença dos novos arquivos** da camada Market.

## Proposed Changes

### 📂 FASE 1: Scripts Core (Hardening)

#### [MODIFY] [run_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/run_context.py)
- Sincronizar o bloco `elif cmd == "all":` para incluir o print de sincronização e a string final com acentuação correta conforme a diretiva.

#### [MODIFY] [validate_context.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/validate_context.py)
- Garantir a verificação da camada opcional `INCEPTION.md`.
- Assegurar que `sys.exit(1)` seja chamado se houver `issues`.

#### [MODIFY] [context_oracle.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/context_oracle.py)
- Revisar regex Unicode para garantir compatibilidade PT-BR (`\b\w{3,}\b`).
- Confirmar indexação de `brain/INCEPTION.md` e `market/SSOT_MAP.md`.

#### [MODIFY] [harness_runner.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/harness_runner.py)
- Sincronizar a função `check_strategic_alignment()` e o dicionário de `checks` no `main()`.

#### [MODIFY] [secrets_scanner.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/_scripts/secrets_scanner.py)
- Validar `JSON_ALLOWLIST` e a lógica de scan que ignora MDs e imagens, mas escaneia JSONs fora da allowlist.

---

### 📂 FASE 2: Governança & Registry

#### [MODIFY] [RULES.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/RULES.md)
- Inserir/Sincronizar a seção `## 🏗️ 0. Máquina de Estados (PROJECT_MODE)` com o texto exato da diretiva.

#### [MODIFY] [AGENT_REGISTRY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/AGENT_REGISTRY.md)
- Adicionar/Sincronizar a role `@vision-architect` e a camada `Strategic` na tabela de isolamento.

#### [MODIFY] [MASTER_FLOW.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/MASTER_FLOW.md)
- Atualizar árvore de diretórios para incluir explicitamente a camada `🌐 market/`.

#### [MODIFY] [PROMPT_LIBRARY.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/PROMPT_LIBRARY.md)
- Sincronizar o prompt do `@vision-architect` com os gatilhos e restrições H.O.K.

---

### 📂 FASE 3: Camada Inception + Market

#### [NEW] [INCEPTION.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/brain/INCEPTION.md)
- Criar template mestre com boundaries `- NUNCA:`.

#### [NEW] [SSOT_MAP.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/SSOT_MAP.md)
- Definir hierarquia da verdade.

#### [NEW] [MARKET_INBOX.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/MARKET_INBOX.md) e [economics.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/market/economics.md)
- Criar arquivos com frontmatter padrão.

#### [NEW] .gitkeeps
- Criar em `market/compliance/` e `market/research/`.

---

### 📂 FASE 4: Isolamento & Bundle

#### [MODIFY] [captura_projeto.py](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/captura_projeto.py)
- Aplicar o filtro **path-scoped** para ignorar `compliance/` e `research/` no bundle.

#### [MODIFY] [JOURNAL.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/.context/maintenance/JOURNAL.md)
- Registrar a entrada de conclusão do hardening.

---

## Verification Plan

### Automated Tests
1. **Pipeline Completo:** `npm run context:all` (Saída esperada: `[DONE] ... concluído com sucesso.`)
2. **Isolamento Market:** Comando python para verificar se `market/compliance` e `market/research` NÃO estão no bundle.
3. **Oracle Unicode:** Consultar termos com acento e verificar confidence.
4. **Harness Fail-Fast:** Inserir boundary proibida no `INCEPTION.md` e violar no `PRD.md`, verificando se o Harness bloqueia com exit 1.

### Manual Verification
- Revisão visual dos arquivos `.md` gerados na camada `market/`.
- Verificação do frontmatter YAML em todos os novos arquivos.

````
CHUNK_END id=37fb63b0fac5_c001
FILE_END id=file_37fb63b0fac5

---
<a id="file_0511c79bd7d2"></a>
FILE_START id=file_0511c79bd7d2 path=.context/specs/PLAN_SPEC_ENRICHER_V2.4.1.md domain=docs lang=markdown lines=58 bytes=2572 mtime=2026-04-15T19:09:36.074497+00:00 sha1=9069fe10243396ca96cc0b1e8b76b29a7084307e
CHUNK_START id=0511c79bd7d2_c001 start_line=1 end_line=58
```markdown
# 📜 PLANO DE IMPLEMENTAÇÃO: Spec Enricher (v2.4.1-Hardened)
*(Documento mestre para instalação do Módulo de Enriquecimento de Especificações)*

---

## 🎯 Objetivo & Visão
Instalar o **@spec-enricher** como role e ritual oficial, criando a ponte cognitiva entre a incepção estratégica e as especificações funcionais. O sistema deve impedir a geração de PRDs se houver gaps de mercado, forçando o ciclo **Research -> Valid -> Execute**.

---

## 🛠️ Arquitetura de Patches (Auditada)

### 🐍 scripts/enrich_context.py (Gap-Checker)
- **Logica:** Scan `INCEPTION.md` -> Busca restrita em `market/compliance` e `market/research` -> Validação de conteúdo (1000 chars) -> Update `MARKET_INBOX.md` (uma linha por entidade).
- **Exit Codes:** `0` (Ready), `2` (Research Needed), `1` (Error).

### 🛡️ scripts/harness_runner.py (Integrity Check)
- **Nova Funcionalidade:** `check_enrichment_integrity(prd_path)`.
- **Gatilhos Semânticos:** Monitora menções a integrações/compliance (integracao, compliance, integration, external api, etc.).
- **Contrato:** Exige seção `## 🚨 Critical Dependencies` com formato exato `- **{Entidade}** → Fonte: market/...`.

### 🐍 run_context.py (Dispatcher)
- **Integração:** Novo comando `enrich`.
- **Tratamento:** `subprocess.run(..., check=False)` + print do `[STRATEGIC BLOCK]`.
- **Help:** Atualizado para refletir o novo rito.

---

## 📋 Matriz de Roles & Prompts

| Role | Especialidade | Escrita | Leitura (Market) | Gátilho |
|------|---------------|---------|------------------|---------|
| `@spec-enricher` | Tradução estratégica, validação de gaps, PRDs lastreados | `PRD.md`, `MARKET_INBOX.md` | `compliance/`, `research/`, `INCEPTION.md` | `npm run context:enrich` |

---

## ✅ Plano de Verificação (H.O.K.)

### 1. Teste de Bloqueio (Exit 2)
1. Inserir entidade (ex: `LGPD`) no `INCEPTION.md`.
2. Certificar ausência do arquivo fonte em `market/`.
3. Rodar `npm run context:enrich`.
4. **Esperado:** Exit 2 + Mensagem de Strategic Block.

### 2. Teste de Sucesso (Exit 0)
1. Criar arquivo fonte `market/research/LGPD.md`.
2. Rodar `npm run context:enrich`.
3. **Esperado:** Exit 0 + Mensagem de Sucesso.

### 3. Teste de Validação (Harness)
1. Criar `PRD.md` com menção a integrações mas sem a seção de dependências.
2. Rodar `npm run context:harness`.
3. **Esperado:** Exit 1 + Erro de contrato de enriquecimento.

---

## 🔒 Handoff Final (Estado Pronto)
`@vision-architect` (Incepção) ⮕ `@spec-enricher` (Research & PRD) ⮕ `@spec-driver` (Specs)

```
CHUNK_END id=0511c79bd7d2_c001
FILE_END id=file_0511c79bd7d2

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=25 bytes=569 mtime=2026-04-14T12:47:48.321567+00:00 sha1=7c7488139d3c3c4327aa9889700f683ee1f47be1
CHUNK_START id=e477c4c5a96c_c001 start_line=1 end_line=25
```yaml
name: Context Health Check

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate-context:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Context Validation (Exit Code Check)
        run: python3 .context/_scripts/validate_context.py

      - name: Run Secrets Scan
        run: python3 .context/_scripts/secrets_scanner.py

```
CHUNK_END id=e477c4c5a96c_c001
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CHUNK_START id=3adfd36c1559_c001 start_line=1 end_line=9
```bash
echo "husky - DEPRECATED

Please remove the following two lines from $0:

#!/usr/bin/env sh
. \"\$(dirname -- \"\$0\")/_/husky.sh\"

They WILL FAIL in v10.0.0
"
```
CHUNK_END id=3adfd36c1559_c001
FILE_END id=file_3adfd36c1559

---
<a id="file_b838611f038c"></a>
FILE_START id=file_b838611f038c path=.specs/_template.md domain=docs lang=markdown lines=25 bytes=671 mtime=2026-04-23T15:03:29.252894+00:00 sha1=2a614c9cd5347bb1019dff4d36733eb19cc91f7d
CHUNK_START id=b838611f038c_c001 start_line=1 end_line=25
```markdown
---
contract_version: 2.5.2
parties: ["@spec-driver", "@qa-validator"]
type: standard
executor_context_id: "ctx-dev-YYYYMMDD-HHMM"
validator_context_id: "ctx-qa-YYYYMMDD-HHMM"
definition_of_done:
  - [ ] Requisito 1
  - [ ] Requisito 2
qa_signoff: false
signed_by: null
---

# 📄 Spec: [Nome da Feature]

## 🎯 Objetivo
[Descreva o que sera construido.]

## ✅ Criterios de aceite
- [ ] O requisito principal foi implementado.
- [ ] Testes e/ou validacoes manuais executadas.
- [ ] Resultado registrado no STATE.md.

## 🔎 Regra de segregacao
- Se `type: standard`, o `validator_context_id` deve ser diferente do `executor_context_id` antes de `qa_signoff: true`.

```
CHUNK_END id=b838611f038c_c001
FILE_END id=file_b838611f038c

---
<a id="file_d4f64fc3b549"></a>
FILE_START id=file_d4f64fc3b549 path=.specs/features/harness_fail_closed/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-22T23:02:55.455444+00:00 sha1=a627e9b0e39cebcd966bff38fff2869fb72544c9
CHUNK_START id=d4f64fc3b549_c001 start_line=1 end_line=5
```markdown
---
status: ✅ PASSED
updated: 2026-04-22 20:02
detail: All checks passed
---

```
CHUNK_END id=d4f64fc3b549_c001
FILE_END id=file_d4f64fc3b549

---
<a id="file_a32e3bf74e3d"></a>
FILE_START id=file_a32e3bf74e3d path=.specs/features/harness_fail_closed/spec.md domain=docs lang=markdown lines=14 bytes=630 mtime=2026-04-21T22:16:15.283651+00:00 sha1=32ea04febe6e93d0fa8959cc525575f3bd2bb3eb
CHUNK_START id=a32e3bf74e3d_c001 start_line=1 end_line=14
```markdown
---
status: ATIVO
definition_of_done: O script 'harness_runner.py' deve travar o commit (Exit 1) se não localizar um spec.md ativo.
qa_signoff: true
signed_by: "@qa-validator"
---

# Spec: Reparo de Vulnerabilidade do Linter (Fail-Closed)

Esta spec é exigida pela nova física do repositório. Para conseguir submeter a própria alteração que tranca o repositório, o agente é obrigado a instanciar uma spec atômica que cumpra os mesmos critérios.

## Tarefas:
- [x] Mudar 'return True' para 'return False' em spec_path.exists().
- [x] Validar que o commit prossegue apenas devido à existência deste documento assinado.

```
CHUNK_END id=a32e3bf74e3d_c001
FILE_END id=file_a32e3bf74e3d

---
<a id="file_238a0e1da225"></a>
FILE_START id=file_238a0e1da225 path=.specs/features/meta-inception/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-21T22:01:44.285888+00:00 sha1=4647d09b6cba8ee228ab2e51d8c647537a9c41a5
CHUNK_START id=238a0e1da225_c001 start_line=1 end_line=5
```markdown
---
status: ✅ PASSED
updated: 2026-04-21 19:01
detail: All checks passed
---

```
CHUNK_END id=238a0e1da225_c001
FILE_END id=file_238a0e1da225

---
<a id="file_9801af51c558"></a>
FILE_START id=file_9801af51c558 path=.specs/features/meta-inception/spec.md domain=docs lang=markdown lines=30 bytes=1389 mtime=2026-04-17T14:33:18.003175+00:00 sha1=0cd48f6f6251020721a35d1efcec750576473d60
CHUNK_START id=9801af51c558_c001 start_line=1 end_line=30
```markdown
---
contract_version: 1.0
parties: ["@spec-driver", "@qa-validator"]
definition_of_done:
  - [x] Criar templates-base para INCEPTION.md e market/.
  - [x] Registrar Role @vision-architect.
  - [x] Inserir bloqueamento estratégico no Pipeline do Harness.
qa_signoff: true
signed_by: "@qa-validator"
Epic: Governança do Template
Feature: Camada Inception e Market (v2.4.0)
Status: Active
Context Dependencies: 
  - .context/brain/RULES.md
  - .context/brain/MASTER_FLOW.md
---

# 🎯 Spec: Meta-Inception Layer

## 1. Visão Geral
Implementar a fundação estrutural e de governança para injetar as restrições e objetivos "Soft e Hard" (Estratégia e Mercado) sem vazar ambiguidade para a camada executiva (PRD e Código).

## 2. Requisitos Principais
- Criar templates-base para `INCEPTION.md`, `SSOT_MAP.md` e diretório `market/`.
- Atualizar a rede de Agentes (Registrar `@vision-architect`).
- Inserir um bloqueamento estratégico no Pipeline do `Harness` (se o código quebra uma restrição do Inception, o CI deve falhar).

## 3. Restrições & Premissas
- Retro-compatibilidade: O arquivo `INCEPTION.md` deve ser **opcional** no `validate_context.py` para não causar quebras em outras instâncias desse template em uso por aí.
- Acesso explícito: O agente `@vision-architect` deve ter seus privilégios formatados aplicando Mínimo Privilégio (apenas Inception e Market).

```
CHUNK_END id=9801af51c558_c001
FILE_END id=file_9801af51c558

---
<a id="file_638d6695a3f1"></a>
FILE_START id=file_638d6695a3f1 path=.specs/features/wiki_level2/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-23T16:13:10.105855+00:00 sha1=148beb1b31b7c84b24afa16b4a71d25cf71264bb
CHUNK_START id=638d6695a3f1_c001 start_line=1 end_line=5
```markdown
---
status: ✅ PASSED
updated: 2026-04-23 13:13
detail: All checks passed
---

```
CHUNK_END id=638d6695a3f1_c001
FILE_END id=file_638d6695a3f1

---
<a id="file_86778e912e18"></a>
FILE_START id=file_86778e912e18 path=.specs/features/wiki_level2/spec.md domain=docs lang=markdown lines=43 bytes=1834 mtime=2026-04-22T23:11:15.675831+00:00 sha1=71be78a7b5b40a5dd98bb2d0f899312d14766a6d
CHUNK_START id=86778e912e18_c001 start_line=1 end_line=43
```markdown
---
id: wiki_level2
status: DRAFT
qa_signoff: true
signed_by: "@qa-validator"
version: 1.0.0
definition_of_done:
  - "npm run context:all verde"
  - "fallback lexical funcional"
  - "artigos sem fonte bloqueados"
---

# Spec: Nível 2 Karpathy Wiki (Market Layer)

## 🎯 Objetivo
Implantar o Nível 2 da Wiki de Mercado (Karpathy Paradigm) focado em roteamento determinístico, guardrails de ingestão e lint incremental sem regressão no pipeline v2.5.0.

## 📋 Requisitos (Rastreabilidade)

### 1. Camada de Roteamento (ORACLE)
- **ORACLE-01**: Implementar cascata de busca: `SSOT_MAP.md` -> `WIKI/_index.md` -> Fallback Lexical.
- **ORACLE-02**: Retorno integral de arquivos MD para evitar truncamento cognitivo.
- **ORACLE-03**: Fallback seguro (exit 2) com warning explícito em caso de baixa confiança.

### 2. Contrato de Ingestão (GUARD)
- **GUARD-01**: Criar `ingest_wiki_guard.py` para validar schema MD (Frontmatter + Fonte + Takeaways).
- **GUARD-02**: Registro obrigatório de toda transação em `market/wiki_log.md`.
- **GUARD-03**: Fast-path (exit 0) se a pasta estiver vazia (pre-onboarding).

### 3. Governança e Qualidade (LINT)
- **LINT-01**: Atualizar `lint_wiki.py` com flag `--strict` bloqueante para diretrizes Karpathy.
- **LINT-02**: Integração no `npm run context:all` como gate obrigatório.
- **LINT-03**: Health check estrutural em `validate_context.py` (check de existência do índice).

## 📐 Design
- **Localização**: `.context/market/WIKI/`
- **Índice Mestre**: `.context/market/WIKI/_index.md`
- **Scripting**: Python 3 (No external dependencies)

## ✅ Critérios de Aceitação
1. `npm run context:all` deve passar com 100% de sucesso.
2. `npm run context:oracle` com termo inexistente deve disparar fallback e aviso.
3. Artigo sem `> Fonte: RAW/...` deve ser bloqueado pelo lint.

```
CHUNK_END id=86778e912e18_c001
FILE_END id=file_86778e912e18

---
<a id="file_fafce66dc671"></a>
FILE_START id=file_fafce66dc671 path=.specs/features/wiki_level2/tasks.md domain=docs lang=markdown lines=55 bytes=2460 mtime=2026-04-22T23:32:40.379948+00:00 sha1=161c580635c9ecd7ba0d68aa9fab0db1d788b1af
CHUNK_START id=fafce66dc671_c001 start_line=1 end_line=55
```markdown
# Tasks: Wiki Level 2

Rifa de tarefas atômicas para implementação do paradigma Karpathy Wiki.

---

## [Phase 1] Foundation & Logs
- [x] **TASK-01**: Criar arquivos base da Wiki.
  - Criar `.context/market/WIKI/_index.md` (root index).
  - Criar `.context/market/wiki_log.md` (append-only log).
  - *Verify*: `ls .context/market/WIKI/_index.md`
- [x] **TASK-02**: Atualizar documentação de governança.
  - Injetar fluxo INGEST -> LINT -> LOG em `RULES.md` e `MASTER_FLOW.md`.
  - *Verify*: Check manual dos arquivos.

## [Phase 2] Oracle Cascade
- [x] **TASK-03**: Patch cirúrgico em `context_oracle.py`.
  - Injetar lógica de busca SSOT -> Index -> Lexical.
  - *Verify*: `python .context/_scripts/context_oracle.py "test"` deve retornar fallback (exit 2).

## [Phase 3] Guard & Lint
- [x] **TASK-04**: Implementar `ingest_wiki_guard.py`.
  - Validação de schema (Frontmatter, Fonte, Takeaways).
  - *Verify*: Rodar contra um mock inválido e esperar falha.
- [x] **TASK-05**: Atualizar `lint_wiki.py` para modo `--strict`.
  - Bloqueio de artigos sem meta-dados Karpathy.
  - *Verify*: `python .context/_scripts/lint_wiki.py --strict`
- [x] **TASK-06**: Integrar no pipeline Central.
  - Atualizar `run_context.py` e `package.json` com novos comandos.
  - *Verify*: `npm run context:all` verde.

## [Phase 4] Health Check
- [x] **TASK-07**: Patch em `validate_context.py`.
  - Injetar `check_wiki_integrity()`.
  - *Verify*: `npm run context:wiki-health`

## [Phase 5] Traceability & Hotfix v2.5.1
- [ ] **TASK-08**: Criar utilitário de log robusto.
  - Criar `.context/_scripts/_wiki_log_utils.py` (atomic append + escape).
  - *Verify*: Script manual de teste de escrita.
- [ ] **TASK-09**: Instrumentar Ingestão e Lint.
  - Patches em `ingest_wiki_guard.py` e `lint_wiki.py`.
  - *Verify*: Validar entradas `OK/FAIL/SKIP` no log.
- [ ] **TASK-10**: Instrumentar Oráculo (Resumo de Query).
  - Patch em `context_oracle.py`.
  - *Verify*: `npm run context:oracle` gera log.
- [ ] **TASK-11**: Validação Operacional (Stress Test).
  - Testar fluxo de erro e correção real.
  - *Verify*: `wiki_log.md` preenchido corretamente.
- [ ] **TASK-12**: Release Bump v2.5.1 (Global SSOT).
  - Atualizar VERSION.md, package.json, Inception e Vision.
  - *Verify*: `npm run context:check-version`.
- [ ] **TASK-13**: Refatoração Factual do Walkthrough.
  - Sincronizar narrativa com a realidade operacional.
  - *Verify*: Leitura final do artefato.

```
CHUNK_END id=fafce66dc671_c001
FILE_END id=file_fafce66dc671

---
<a id="file_95dabcdf3543"></a>
FILE_START id=file_95dabcdf3543 path=GUIA_ESTABILIZACAO_NOTEBOOKLM.md domain=docs lang=markdown lines=56 bytes=2342 mtime=2026-04-16T01:24:16.342106+00:00 sha1=42fda535b309349df1a8c83c959f0cc2e534875a
CHUNK_START id=95dabcdf3543_c001 start_line=1 end_line=56
````markdown
# 🛠️ Guia de Estabilização: NotebookLM + Antigravity

Este guia contém a "receita do bolo" para resolver falhas de autenticação e conexão no servidor MCP do NotebookLM. Siga estes passos se a IA perder o acesso ao seu Save Point.

---

## 🚀 1. Preparação do Ambiente (Obrigatório)
Sempre que for rodar comandos de diagnóstico no PowerShell, rode este comando primeiro para evitar erros de caracteres especiais:

```powershell
$env:PYTHONUTF8=1
```

---

## 🛠️ 2. Correção de Dependências (O "Soro")
O Google detecta robôs facilmente. Para o login **persistir no disco**, o Python precisa destes três componentes:

1. **undetected-chromedriver**: Faz o navegador parecer humano.
2. **setuptools**: Necessário para versões modernas do Python (3.12+).

**Comando para reinstalar tudo se parar de funcionar:**
```powershell
uv pip install --python C:\Users\User\AppData\Roaming\uv\tools\notebooklm-mcp\Scripts\python.exe undetected-chromedriver setuptools
```

---

## 🔑 3. O Fluxo de Login Definitivo
Se a IA disser "Not Authenticated", siga este ritual:

1. Abra o arquivo `C:\Users\User\.gemini\antigravity\notebooklm-config.json`.
2. Mude `"headless": true` para **`false`**.
3. No terminal, rode: 
   `uv tool run notebooklm-mcp chat -n 8979de2f-a111-4856-8a71-197d6b9ec876`
4. **Logue manualmente** na janela que abrir.
5. Quando o notebook carregar, feche a janela e mude o config de volta para **`true`**.

---

## 🧠 4. Como o MCP funciona na prática?
Você **não** precisa dizer qual pasta eu devo ler. O sistema funciona por **ID de Notebook**:

*   **Vínculo:** O seu projeto local está vinculado ao Notebook **"Template-framework-HOK"** via ID.
*   **Ação:** Quando você me pede algo, eu uso o MCP para pesquisar nas **32 fontes** (PDFs, Docs, Planilhas) que você subiu lá no Google.
*   **Vantagem:** Você pode subir 1000 PDFs no NotebookLM e eu terei acesso a todo esse conhecimento sem "estourar" o limite de memória do nosso chat aqui.

---

> [!IMPORTANT]
> **Caminho do Perfil:** Suas senhas ficam salvas localmente em:
> `C:\Users\User\.gemini\antigravity\chrome_profile_notebooklm`
> **NUNCA** delete esta pasta, ou terá que logar novamente.

> [!TIP]
> **Notebook Errado?** Se quiser trocar de notebook, basta mudar o `default_notebook_id` no arquivo `notebooklm-config.json`.

````
CHUNK_END id=95dabcdf3543_c001
FILE_END id=file_95dabcdf3543

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=97 bytes=4687 mtime=2026-04-23T16:12:13.144613+00:00 sha1=23e3abb6e9ba9b868808626442bbec6112a64a74
CHUNK_START id=8ec9a00bfd09_c001 start_line=1 end_line=97
````markdown
# 🛸 Antigravity Kit v2.5.2 Hardened (H.O.K. Enabled)
> **O ecossistema definitivo para engenharia AI-Ready: Governança Macro + Execução Atômica + Controle Ativo.**

Este repositório é um **Template Semente** desenhado para projetos que utilizam IA como parceira de codificação. Ele unifica o **Antigravity Kit** com o **TLC Spec-Driven** e eleva a governança ao **Nível 3 (H.O.K.)**, garantindo que Propósito → Execução → Validação operem em loop fechado e autônomo.

---

## 🛡️ A Tríade H.O.K. (Governança Nível 3)
O kit evoluiu de validação passiva para **controle ativo e reativo**:
| Pilar | Função | Script | Gatilho |
|-------|--------|--------|---------|
| 🛡️ **Harness** | Bloqueia specs que violam contratos (Schema vs PRD, Handoffs incompletos) | `harness_runner.py` | `npm run context:all` / `pre-commit` |
| 🔍 **Oracle**  | RAG local `stdlib` que resolve ambiguidades antes da geração de código | `context_oracle.py` | `npm run context:oracle "dúvida"` |
| 📖 **Karpathy**| Linter epistemológico: exige `> Fonte: raw/...` em claims técnicos | `lint_wiki.py` | `npm run context:lint` (Strict no commit) |

> 💡 **Regra de Ouro:** `Se não está no .context, não existe. Se não tem fonte, é alucinação. Se não passa no Harness, não vai pro repositório.`

---

## 🚀 Instalação e Onboarding

### Cenário 1: Repositório Novo (Template)
Se você apenas clonou este repositório base, você já possui todo o ecossistema Antigravity. Apenas execute:
```bash
npm install
npm run prepare # ativa os hooks do Husky
```

### Cenário 2: Aplicando a projetos existentes (Bootstrapper)
Se você quer governar um projeto pré-existente, copie os arquivos `.context/_scripts/`, `run_context.py` e execute o integrador via Bash:
```bash
# O ambiente precisa de um bash real compatível (Linux/Mac/WSL/Git Bash)
bash init_ai_project.sh
```
> ⚠️ **Aviso Operacional:** O `init_ai_project.sh` cria as pastas estruturais de regras e injeta NPM Scripts cross-platform. Ele **não** gera os motores internos e aborta se a pasta `.context/` estruturada já existir. Certifique-se de copiar os `.py` desta raiz se estiver instalando manualmente!

---

## 📂 Anatomia do Repositório

### 1. `.context/` - A Camada de Governança
- **`brain/`**: Onde mora a inteligência. Regras, Fronteiras (VISION/INCEPTON) e PRD-Template.
- **`market/`**: Camada Estratégica. Restrições do mundo real, dependências externas e compliance.
- **`maintenance/`**: Onde mora a "verdade real". Log vivo (`JOURNAL.md`), Schema e Inventário Técnico.
- **`monitoring/`**: Dashboard de saúde técnica e cognitiva.
- **`_scripts/`**: Validação ativa (Harness e Oracle) escrita na biblioteca Padrão do Python (Seguro Cross-Platform).

### 2. `.specs/` - A Camada de Execução (TLC)
- **`features/`**: Workshop efêmero para desenvolvimento Spec-Driven. Máximo de 3 specs ativas. Regra de limpeza automática pós-merge ou 48h de inatividade.

---

## 🚀 Comandos de Operação (v2.5.2)
| Comando | Descrição |
|---------|-----------|
| `npm run context:validate` | Checa integridade, estrutura e estimativa de tokens |
| `npm run context:harness`  | Valida contratos ativos e handoffs (`harness_runner.py`) |
| `npm run context:oracle`   | Roteia consulta proativa ao Oráculo local (com confidence) |
| `npm run context:lint`     | Fiscaliza citações epistemológicas e claims sem fonte |
| `npm run context:all`      | 🟢 Pipeline C-Level: Validate → Sync → Cleanup → Harness → Lint(Strict) |

---

## 🤝 Protocolo de Ativação Híbrida

Para iniciar uma tarefa com poder total, use o prompt mestre:
> *"Inicie a fase de SPECIFY para o PRD #[ID] usando o modo Híbrido TLC."*

Isso ativará a role `@spec-driver` e iniciará o ciclo atômico no `.specs/` alinhado à governança do `.context/`.

---

## 🕐 Configuração de Fuso Horário
Por padrão, o kit usa **America/Sao_Paulo (Brasília)** (-3h fixo). Para alterar globalmente:

```bash
# No terminal (temporário)
export CONTEXT_TIMEZONE="America/New_York"
npm run context:all

# Ou no .env do projeto (permanente)
echo "CONTEXT_TIMEZONE=Europe/London" >> .env
```

*Nota: Usa apenas Python stdlib (sem dependência do módulo 'pytz') para máxima compatibilidade cruzada.*

---

## 📖 Documentação de Operação
Para ritos de Sunrise/Sunset e gerenciamento de memória, consulte:
👉 **[README_CONTEXT.md](./README_CONTEXT.md)**
👉 **[TLC_INTEGRATION.md](./.context/brain/TLC_INTEGRATION.md)**

---

> **Desenvolvido com 🤖 por Tales Avancini / Antigravity Kit.**  
> *"Governança não é burocracia, é a fundação da inteligência escalável."*

````
CHUNK_END id=8ec9a00bfd09_c001
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=124 bytes=6147 mtime=2026-04-23T16:12:19.354400+00:00 sha1=1d7fc538fa85b139c3882b3f40c7525e7ed5429f
CHUNK_START id=4efb6293109d_c001 start_line=1 end_line=124
````markdown
---
Criado em: 2026-04-10 22:45
Ultima Atualizacao: 2026-04-11 23:30
Status: Ativo (v2.5.2)
---

# 📖 README_CONTEXT.md — Guia de Operação do Framework
> Diretriz oficial para humanos e agentes de IA operarem o diretório `.context/` no dia a dia.

## 🎯 1. Visão Geral
O diretório `.context/` é a **Fonte Unica da Verdade (SSOT)** do projeto. Ele existe para:
- 🧠 Manter a IA alinhada, previsivel e livre de alucinacoes.
- 📐 Garantir rastreabilidade tecnica, de negocio e de decisoes.
- ⚙️ Automatizar validacao, sincronizacao e limpeza de contexto.
- 🛡️ Impedir que codigo e documentacao divirjam ao longo do tempo.

**Regra de Ouro:** `Se nao esta no .context, nao existe. O codigo deve ser o reflexo fiel do contexto.`

## 🧩 Novos Pilares de Operação (v2.5.2+)
- **🛡️ Harness:** O pipeline aborta automaticamente se uma Spec referenciar tabelas/campos inexistentes no `schema.sql` ou se handoffs estiverem incompletos.
- **🔍 Oracle:** Ao detectar ambiguidade, execute `npm run context:oracle "sua pergunta"`. Retorno com `confidence < 0.5` pausa o fluxo e exige `[oracle:uncertain]` no `JOURNAL.md`.
- **📖 Karpathy:** Todo claim técnico adicionado ao `.context/` deve conter `> Fonte: raw/nome-arquivo.md`. O `pre-commit` roda em modo `--strict` e rejeita commits sem citação.

---

## 📂 2. Estrutura em Camadas
| Camada | Arquivos Principais | Função |
|--------|---------------------|--------|
| 🧠 **Cognitiva** | `brain/` (`RULES`, `MASTER_FLOW`, `AGENT_REGISTRY`, `PROMPT_LIBRARY`, `PRD`) | Governanca, roteamento, execucao e requisitos. |
| 💼 **Mercado** | `market/` | Camada Estratégica, limites operacionais e compliance financeiro. |
| 🛠️ **Manutencao** | `maintenance/` (`JOURNAL`, `TECH_REQ`, `rebuild_guide`, `schema.sql`) | Memoria viva, inventario tecnico e recovery. |
| 📊 **Monitoramento** | `monitoring/` (`CONTEXT_HEALTH.md`) | Dashboard de integridade e limites de sessao. |
| ⚙️ **Automacao** | `_scripts/*.py`, `run_context.py` | Validacao, purge, sync, harness e orquestracao. (SSOT de Execucao). |
| 🛡️ **Qualidade** | `tests/test_context.py`, `.husky/` | Testes automaticos e gate de commit. |

---

## 🔄 3. Fluxo de Trabalho Diário (Day-to-Day)

### 🌅 Inicio da Sessao (Sunrise)
1. Verifique a saude do contexto: `npm run context:validate`
2. Leia `brain/RULES.md` + `brain/PRD.md` ativo + ultimas 30 linhas do `maintenance/JOURNAL.md`.
3. Declare a role no chat: `🤖 Ativando @[role] | Escopo: [descricao]`

### 💻 Durante o Desenvolvimento
- Siga estritamente os templates do `brain/PROMPT_LIBRARY.md`.
- Respeite o `Context Gate` antes de gerar codigo.
- Em cruzamentos de dominio, registre handoff no `maintenance/JOURNAL.md`.
- Nunca hardcode segredos; use `[VAR_NAME]` + `.env`.

### 🌙 Fim da Sessao / Pre-Commit (Sunset)
1. Execute `npm run context:sync` se adicionou libs ou mudou schema.
2. Responda ao prompt da IA: `"Deseja que eu atualize o contexto agora?"`
3. Commit normal -> Husky roda `npm run context:all` automaticamente.
4. Se passar: ✅ merge seguro. Se falhar: 🔍 corrija o contexto antes de forcar (Harness, Lint e Oráculo barrarão desvios).

---

## 🤖 4. Operando com Agentes de IA

| Situacao | Acao Recomendada |
|----------|------------------|
| **Ativacao** | Sempre comece com `🤖 Ativando @[role] | Tarefa: [...]` |
| **Isolamento** | A IA so carrega `Global + Role-Specific + Task-Ephemeral`. |
| **Handoff** | Se cruzar 2+ dominios -> pausa -> registra no `maintenance/JOURNAL.md` -> proxima role assume. |
| **Prompt Padronizado** | Use `brain/PROMPT_LIBRARY.md`. Substitua `{{...}}` e cole no chat. |
| **Alucinacao Suspeita** | Execute `npm run context:validate` e peca: `"Valide o contexto antes de prosseguir."` |

---

## ⚙️ 5. Comandos Rápidos (Cheat Sheet v2.5.2)
```bash
# Validar integridade + estimar tokens
npm run context:validate

# Consultar Oráculo antes de assumir ambiguidades
npm run context:oracle "qual regex de validação?"

# Checar citações epistemológicas (modo manual: WARN-ONLY)
npm run context:lint

# Pipeline completo (orquestrado por run_context.py, lint vira STRICT-MODE aqui)
npm run context:all

# Limpar specs inativas / Sincronizar deps / Purge Journal
npm run context:cleanup
npm run context:sync
npm run context:purge
```
**🌎 Fuso Horário:** Por padrão, todos os artefatos temporais usam **Brasília (-3h)**. Exporte `CONTEXT_TIMEZONE="..."` para sobrescrever nativamente.

> 💡 *Nota:* Todos os comandos são roteados pelo `run_context.py`. Isso garante compatibilidade nativa Windows/WSL/Linux no `pre-commit`, sem dependências de shell.

---

## 🛡️ 6. Gate de Qualidade (Husky & CI)
- **Pre-commit:** Bloqueia commits se o `npm run context:all` falhar (Harness aborta, ou Lint em modo Strict acusa falta de fonte crua).
- **CI/CD:** O GitHub Actions roda o pipeline completo (`python run_context.py all`) em cada Pull Request para garantir consistencia remota.

---

## ✅ 7. Checklist de Operacao & Implantacao

### 🆕 Novo Projeto / Onboarding (The Fool's Cut)
- [ ] **Visão Humana:** Crie o arquivo `brain/VISION.md` (veja template).
- [ ] **Enriquecimento:** Execute `npm run context:enrich`. A IA gerará o `INCEPTION.proposed.md`.
- [ ] **Ratificação:** Revise a proposta. Se aprovado, renomeie para `INCEPTION.md` e mude `status` para `ACTIVE`.
- [ ] **Consistência:** Execute `npm run context:validate` para garantir que o projeto está operando em modo governado.

### 🚀 Feature / Desenvolvimento Normal
- [ ] `brain/PRD.md` preenchido com objetivos e criterios de aceite.
- [ ] `Context Gate` validado.
- [ ] Roles mapeadas na tabela de roteamento do PRD.

### ✅ Antes do Commit / PR
- [ ] `npm run context:validate` retorna `[SUCCESS]`.
- [ ] Secrets nao estao no codigo (usar `.env`).
- [ ] Husky pre-commit passou sem bloqueios.

---

> 💡 **Nota para a Equipe:** Este framework e vivo. Revise este guia a cada nova fase do `ROADMAP.md`. Um contexto desatualizado gera falsa sensacao de controle.

🚀 **Pronto para operar.** Mantenha o `.context/` enxuto, valido e atualizado. A IA fara o resto.

````
CHUNK_END id=4efb6293109d_c001
FILE_END id=file_4efb6293109d

---
<a id="file_19e76e009f38"></a>
FILE_START id=file_19e76e009f38 path=TEMPLATE_MIGRATION.md domain=docs lang=markdown lines=59 bytes=1930 mtime=2026-04-15T13:55:12.936320+00:00 sha1=a3590439f4c18d976ff928504760f8f35a29d25c
CHUNK_START id=19e76e009f38_c001 start_line=1 end_line=59
````markdown
# 🚀 Guia de Migração: Do Template para o Projeto Real

Este guia descreve como "descolar" este template do repositório de origem e iniciar seu novo projeto com a Governança Antigravity Kit v2.4.1.

---

## 🛠️ Passo a Passo via CLI

### 1. Clonar o Template
Escolha um nome para a pasta do seu novo projeto (Ex: `meu-novo-projeto`).
```powershell
git clone https://github.com/TalesAvancini/template-ai-context-governance.git meu-novo-projeto
cd meu-novo-projeto
```

### 2. Romper o vínculo com o Antigravity (Reset do Git)
Delete o histórico de commits do template para começar sua própria história do zero.
```powershell
# No Windows (PowerShell)
Remove-Item -Recurse -Force .git

# No Linux/Mac/WSL
rm -rf .git
```

### 3. Iniciar seu novo Repositório
```powershell
git init
git add .
git commit -m "chore: initial commit from Antigravity Kit v2.4.1"
```

### 4. Conectar ao seu NOVO repositório no GitHub
Crie um repositório vazio no seu GitHub e utilize a URL dele abaixo:
```powershell
git remote add origin https://github.com/SEU_USUARIO/SEU_NOVO_REPOSICTORIO.git
git branch -M main
git push -u origin main
```

### 5. Ativar o Motor de Governança
Garanta que os Hooks e dependências estejam prontos no novo ambiente.
```powershell
# Instalar dependências (Husky, etc)
npm install

# Rodar a validação completa pela primeira vez
npm run context:all
```

---

## 💡 Dicas de Manutenção
*   **package.json**: Edite os campos `name`, `version`, `author` e `description` para refletir a sua nova aplicação.
*   **README.md**: Atualize o título e a descrição principal do projeto, mantendo as seções de Operação de Contexto.
*   **Timezone**: Verifique se o arquivo `.env` do novo projeto possui a variável `CONTEXT_TIMEZONE` se você não estiver operando no fuso de Brasília.

---
> 🛸 **Antigravity Kit** | Governança não é burocracia, é a fundação da inteligência escalável.

````
CHUNK_END id=19e76e009f38_c001
FILE_END id=file_19e76e009f38

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=10 bytes=537 mtime=2026-04-23T15:08:13.037173+00:00 sha1=8f9a8ce10e35a27487d66c85490f535adcdb2d5a
CHUNK_START id=f6f7100f063b_c001 start_line=1 end_line=10
```markdown
# 🛸 Antigravity Kit Versioning
v2.5.2
Dash: [Antigravity Kit v2.5.2 - Independent QA Segregation]
Audit Status: ✅ PASSED
Release Date: 2026-04-23

📜 Changelog:
- **[Segregação QA]** Specs `type: standard` exigem `executor_context_id != validator_context_id` no harness.
- **[Contrato de Sprint]** Template oficial `.specs/_template.md` atualizado com campos de proveniência e assinatura.
- **[Hook Estável]** Pre-commit em modo read-only (`check-version`, `validate`, `scan-secrets`) para evitar drift automático em cadeia.

```
CHUNK_END id=f6f7100f063b_c001
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CHUNK_START id=1f98938d3cd9_c001 start_line=1 end_line=140
````markdown
### 🔍 Por que um único arquivo não basta?
A IA não lê apenas um arquivo para definir comportamento. Ela avalia:
- 📁 Estrutura de pastas (`brain/`, `maintenance/`, `monitoring/`, `.specs/`)
- 🤖 `AGENT_REGISTRY.md` (ainda carregará 7 roles se existir)
- 🐍 Scripts Python e hooks do Husky (continuam ativos)
- 📜 Regras de carregamento (`Checklist de Carga` ainda exige camadas)
- 🧠 Memória de sessão (a IA tentará carregar tudo o que encontrar)

Se você só trocar o `RULES.md`, a IA ficará em **estado híbrido confuso**: regras dizem "modo leve", mas a estrutura exige validações pesadas, registry complexo e scripts de automação. Isso gera `token bloat`, alucinação e falhas de contexto gate.

---
### 🛠️ 3 Caminhos Técnicos Viáveis

| Abordagem | Como funciona | Prós | Contras |
|-----------|--------------|------|---------|
| `MODE.md` (Flag) | Arquivo simples: `MODE: LIGHT`. A IA lê primeiro e ajusta comportamento. | Zero destruição, reversível, explícito. | Exige atualização no `RULES_LIGHT.md` para ler a flag. |
| `init_ai_project_light.sh` | Bootstrap que cria estrutura mínima do zero (sem camadas, sem scripts, sem Husky). | Limpo, seguro, ideal para novos MVPs. | Não converte projetos robustos existentes. |
| `downgrade_to_light.sh` | Remove camadas, desativa Husky, arquiva scripts, substitui `RULES.md`. | Converte projeto existente sem perder histórico. | Irreversível sem backup manual. |

---
### ✅ Recomendação: `MODE.md` + `init_ai_project_light.sh`
É a combinação mais segura. Você mantém o robusto como padrão, mas pode ativar o modo leve em qualquer repositório novo ou existente com **um arquivo de flag** ou **um comando de init**.

---
### 📄 1. `MODE.md` (A Chave de Conversão)
Coloque na raiz de `.context/`. A IA **DEVE** ler este arquivo antes de qualquer checklist.

```markdown
---
Criado em: YYYY-MM-DD HH:MM
Última Atualização: YYYY-MM-DD HH:MM
Status: Ativo
---

# 🪶 MODE.md
> Define o perfil operacional do framework. A IA ajusta carregamento, roles e automação conforme este valor.

**MODE:** LIGHT  
**Reason:** MVP < 2 semanas | Time 1-2 devs | Velocidade > Governança  

💡 *Insight IA: Se MODE = LIGHT, ignore camadas, scripts, registry multi-agent e .specs/. Carregue apenas: RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql. Use @fullstack-generalist por padrão.*
```

---
### 📜 2. Patch Obrigatório no `RULES_LIGHT.md`
Adicione este bloco no **topo** do arquivo, antes de qualquer regra:

```markdown
📜 RULES_LIGHT.md — Modo Minimalista (MVP/POC)
Projeto: [NOME DO PROJETO] | Arquitetura: Single-Agent + Database-First
> 🪶 **MODO ATIVO:** Leia `MODE.md`. Se `MODE: LIGHT`, siga estritamente este protocolo enxuto. Ignore `.specs/`, scripts Python, Husky e `AGENT_REGISTRY.md`.

🛡️ Checklist de Carga (Light)
1. [ ] RULES_LIGHT.md (este arquivo)
2. [ ] PRD.md ativo
3. [ ] schema.sql atualizado
4. [ ] JOURNAL.md < 300 linhas
⚠️ Se faltar 1 item → pare e solicite correção.

🔄 Comportamento do Agente (Light)
- Role padrão: `@fullstack-generalist` (única ativa)
- Sem handoff obrigatório. Registre decisões críticas direto no JOURNAL.md
- Database-First mantido. Nunca assuma schema.
- Sem automação. Validação manual: `grep -q "schema.sql" PRD.md && echo "✅ OK"`
- Fim de sessão: `"Contexto atualizado? [S/N]"`
```

---
### 🐚 3. `init_ai_project_light.sh` (Bootstrap Seguro)
Cria uma estrutura flat, sem camadas, sem scripts, sem Husky. Ideal para `git init` de MVPs.

```bash
#!/usr/bin/env bash
set -euo pipefail

GREEN='\033[0;32m'
NC='\033[0m'

[ -d ".context" ] && { echo "❌ .context/ já existe. Abortando."; exit 1; }

echo -e "\n${GREEN}🪶 Inicializando Modo LIGHT...${NC}"
mkdir -p .context

NOW=$(date +%Y-%m-%d\ %H:%M)

# MODE Flag
cat > .context/MODE.md << EOF
---
Criado em: $NOW
Status: Ativo
---
MODE: LIGHT
Reason: MVP rápido | Velocidade > Governança
💡 IA: Ignore camadas, scripts, registry e .specs/. Use apenas RULES_LIGHT.md, PRD.md, JOURNAL.md, schema.sql.
EOF

# RULES_LIGHT (minimalista)
cat > .context/RULES_LIGHT.md << 'EOF'
📜 RULES_LIGHT.md — Modo Minimalista
> 🪶 MODE: LIGHT ativo. Role única: @fullstack-generalist. Sem scripts, sem Husky, sem handoff complexo.
🛡️ Carga: [ ] RULES_LIGHT.md [ ] PRD.md [ ] schema.sql [ ] JOURNAL.md <300lin
🗄️ DB-First: Valide schema antes de UI. Se faltar campo → pare e avise.
🔄 Fim de sessão: Pergunte "Atualizo contexto?" e registre no JOURNAL.md apenas mudanças de lógica/bug.
⚠️ Sem automação. Sem registry. Sem .specs/. Mantenha enxuto.
EOF

# Arquivos base
for f in PRD.md JOURNAL.md schema.sql; do
  cat > ".context/$f" << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📄 $f
EOF
done

echo -e "${GREEN}✅ Modo LIGHT pronto. Estrutura plana, sem overhead.${NC}"
echo "📖 Próximo: Preencha PRD.md e comece. A IA usará @fullstack por padrão."
```

---
### 🧠 Como a IA Interpreta Isso na Prática
1. **Início de sessão:** A IA lê `MODE.md` primeiro.
2. **Se `MODE: LIGHT`:** 
   - Ignora `brain/`, `maintenance/`, `monitoring/`, `_scripts/`, `.specs/`
   - Carrega apenas os 4 arquivos essenciais
   - Ativa `@fullstack-generalist` implicitamente
   - Desativa validações Python/Husky automaticamente
   - Usa heurística simplificada de tokens (limite ~20k chars)
3. **Se quiser voltar ao robusto:** Troque `MODE: ROBUST` e rode `npm run context:all` para restaurar camadas/scripts.

---
### 🚀 Próximo Passo
Quer que eu:
1. **Gere o `downgrade_to_light.sh`** para converter um projeto robusto existente sem perder histórico?
2. **Ajuste o `init_ai_project.sh` principal** para incluir uma flag `--light` que alterna entre os dois modos automaticamente?
3. **Entregue o `RULES_LIGHT.md` completo** (versão pronta para copiar/colar, com todos os protocolos simplificados)?

Escolha o fechamento. O framework agora tem conversão explícita, segura e reversível. 🏁
````
CHUNK_END id=1f98938d3cd9_c001
FILE_END id=file_1f98938d3cd9

---
<a id="file_c3916196f58f"></a>
FILE_START id=file_c3916196f58f path=captura_projeto.py domain=source lang=python lines=429 bytes=17844 mtime=2026-04-23T18:31:18.210183+00:00 sha1=6108c27d0315281c1f40bec72da49685422fdcc9
CHUNK_START id=c3916196f58f_c001 start_line=1 end_line=300
```python
#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

VERSION = "2.5.2"

# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
    "_archive_context", "planos", "RAW",
}

ARQUIVOS_IGNORAR = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "composer.lock",
    "contexto.md", "contexto_*.md", ".*.lock"
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False
    include_lockfiles: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        # 🛡️ Isolamento Cirúrgico (v2.4.1): Ignora pastas densas específicas
        rel_dir = current.relative_to(root).as_posix()
        if rel_dir == ".context/market":
            dirnames[:] = [d for d in dirnames if d not in {"compliance", "research", "RAW"}]

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            
            # 🛡️ Blindagem contra Self-Capture e Locks
            is_output_file = (filename == config.output or filename == get_dynamic_filename(config))
            is_ignored_file = any(fnmatch(filename.lower(), pat.lower()) for pat in ARQUIVOS_IGNORAR)
            is_lockfile = ("lock" in filename.lower() and path.suffix in {".json", ".yaml", ".yml", ".lock"})

            # Filtro path-scoped para Market (v2.4.1 Hardened)
            # Ignora pastas de documentos brutos para evitar token bloat no bundle
            if "market/compliance" in rel_path.lower() or "market/research" in rel_path.lower():
                continue

            if is_output_file: 
                continue
            if is_ignored_file and not (is_lockfile and config.include_lockfiles):
                continue

            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    parts = []
    if config.only_core: parts.append("only-core")
    elif config.exclude_core: parts.append("exclude-core")
    else: parts.append("full")
    if config.toc_only: parts.append("TOC")
    return " | ".join(parts)

def get_dynamic_filename(config: BundleConfig) -> str:
    # Se o usuário não mudou o default, geramos um nome inteligente
    if config.output != DEFAULT_OUTPUT:
        return config.output
    
    base = "contexto"

```
CHUNK_END id=c3916196f58f_c001
CHUNK_START id=c3916196f58f_c002 start_line=301 end_line=429
````python
    ver = f"_v{VERSION}"
    suffix = ""
    if config.toc_only: suffix += "_toc"
    if config.only_core: suffix += "_core"
    
    return f"{base}{ver}{suffix}.md"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)

def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"

def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    target_name = get_dynamic_filename(config)
    output_path = config.diretorio / target_name
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")
    return output_path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    parser.add_argument("--include-lockfiles", action="store_true", help="Força a inclusão de package-lock.json e similares")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets,
        include_lockfiles=args.include_lockfiles
    )
    out = write_output(config)
    print(f"\n[OK] Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()
````
CHUNK_END id=c3916196f58f_c002
FILE_END id=file_c3916196f58f

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=127 bytes=4447 mtime=2026-04-17T02:44:14.961287+00:00 sha1=f14d70f06e7349803e99a3d2521a4f54ff1a669d
CHUNK_START id=c59135753d26_c001 start_line=1 end_line=127
```bash
#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# 🚀 init_ai_project.sh - Antigravity Kit Bootstrapper (v2.4.1 Hardened)
# -----------------------------------------------------------------------------
# Versão Suprema: Fusão Antigravity + TLC Spec-Driven.
# Com detecção automática de gerenciador e motores de manutenção completos.
# -----------------------------------------------------------------------------
set -euo pipefail

# 🎨 Cores & Estética
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log() { echo -e "\n${CYAN}🔹 $1${NC}"; }
success() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️ $1${NC}"; }
error() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# 🛡️ Pre-flight Checks
check_deps() {
  command -v git >/dev/null 2>&1 || error "git e obrigatorio."
  if command -v python3 >/dev/null 2>&1; then PYTHON="python3"
  elif command -v python >/dev/null 2>&1; then PYTHON="python"
  else error "python3 ou python e obrigatorio."
  fi
}

# 🔍 Detecção de Gerenciador de Pacotes
detect_pkg_mgr() {
  if command -v pnpm >/dev/null 2>&1; then echo "pnpm"
  elif command -v yarn >/dev/null 2>&1; then echo "yarn"
  elif command -v npm >/dev/null 2>&1; then echo "npm"
  else error "Nenhum gerenciador de pacotes encontrado (npm, yarn ou pnpm)."
  fi
}

# 🔒 Segurança
if [ -d ".context" ]; then
    error ".context/ ja existe. Abortando para proteger dados."
fi

check_deps
PKG_MGR=$(detect_pkg_mgr)
log "Gerenciador detectado: $PKG_MGR"
log "Inicializando Antigravity AI-Ready Framework v2.4.1 Hardened..."

# 📂 Estrutura de Diretorios
log "Criando estrutura de camadas e workshop TLC..."
mkdir -p .context/{brain,maintenance,monitoring,_scripts}
mkdir -p .context/maintenance/_archive_context/{prds,schemas,journals,specs}
mkdir -p .specs/features
mkdir -p tests .husky

NOW=$(date +%Y-%m-%d\ %H:%M)

# 📄 Geração de Documentos de Governança
log "Gerando documentos de governança e integração TLC..."

cat > .context/brain/RULES.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 📜 RULES.md — Template Universal de Contexto & Governança
Projeto: [NOME DO PROJETO]
Arquitetura: AI-Agent Driven (Antigravity Kit + TLC Fusion)

Conceito Central: A pasta \`.context\` e a fonte da verdade (SSOT). O workshop \`.specs\` e o espaco de execucao efemera.

🧠 1. Protocolo de Manutencao
- JOURNAL.md: Memoria de longo prazo e handoffs.
- .specs/: Workbench atômico (Regra de 48h/Max 3).

🔄 4. Gatilhos Operacionais
- "Inicie a fase de SPECIFY para o PRD #[ID]": IA cria spec atômica no .specs/.
- "Atualize contexto": Sincronizacao proativa via sync_project.py.
EOF

cat > .context/brain/TLC_INTEGRATION.md << EOF
---
Criado em: $NOW
Status: Ativo
---
# 🔗 TLC_INTEGRATION.md
Ponte entre Governança (.context/) e Execução Atômica (.specs/).

## 🔄 Ciclo de Vida Híbrido
1. INTENT -> PRD.md ativo define escopo.
2. SPECIFY -> IA cria .specs/features/[nome]/spec.md.
3. IMPLEMENT -> Geração de código baseada na spec.
4. VERIFY -> STATE.md marcado como ✅ PASSED.
5. SYNC -> Lições para o JOURNAL.md e limpeza da spec.
EOF

# Os Motores Reais v2.4.1 Hardened já residem na pasta .context/_scripts do template.
# Diferente de versões anteriores, este bootstrapper NÃO sobrescreve os motores Python nativos com cat.

# Injeta scripts no package.json via Node
[ -f package.json ] || npm init -y > /dev/null 2>&1
node -e "
const fs = require('fs');
const pkg = JSON.parse(fs.readFileSync('package.json','utf8'));
pkg.scripts = pkg.scripts || {};
Object.assign(pkg.scripts, {
  'context:validate': 'python run_context.py validate',
  'context:cleanup': 'python run_context.py cleanup',
  'context:purge': 'python run_context.py purge',
  'context:sync': 'python run_context.py sync',
  'context:oracle': 'python run_context.py oracle',
  'context:lint': 'python run_context.py lint',
  'context:harness': 'python run_context.py harness',
  'context:all': 'python run_context.py all',
  'prepare': 'husky'
});
fs.writeFileSync('package.json', JSON.stringify(pkg, null, 2));
"

log "Instalando Husky e configurando Hooks..."
npx husky init > /dev/null 2>&1
echo "$PKG_MGR run context:all" > .husky/pre-commit
chmod +x .context/_scripts/*.py .husky/pre-commit

success "Antigravity + TLC Fusion inicializado com sucesso!"
warn "Acesse README_CONTEXT.md para o manual de operacao."

```
CHUNK_END id=c59135753d26_c001
FILE_END id=file_c59135753d26

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=38 bytes=1494 mtime=2026-04-23T15:08:31.764449+00:00 sha1=d790fbee1062be196684ab2ca82037ffc394e56a
CHUNK_START id=7030d0b2f71b_c001 start_line=1 end_line=38
```json
{
  "name": "ai-context-governance-template",
  "version": "2.5.2",
  "description": "AI-Ready Template with Layered Context Governance & Spec-Driven Execution",
  "scripts": {
    "context:validate": "python run_context.py validate",
    "context:sync": "python run_context.py sync",
    "context:cleanup": "python run_context.py cleanup",
    "context:purge": "python run_context.py purge",
    "context:harness": "python run_context.py harness",
    "context:lint": "python run_context.py lint",
    "context:lint-strict": "python run_context.py lint-strict",
    "context:oracle": "python run_context.py oracle",
    "context:health": "python run_context.py health",
    "context:scan-secrets": "python run_context.py scan-secrets",
    "context:check-migrations": "python run_context.py check-migrations",
    "context:check-version": "python run_context.py check-version",
    "context:enrich": "python run_context.py enrich",
    "context:ingest-guard": "python run_context.py ingest-guard",
    "context:wiki-health": "python run_context.py wiki-health",
    "context:capture": "python captura_projeto.py --emit-symbol-index --emit-import-map",
    "context:all": "python run_context.py all",
    "context:test": "python tests/test_context.py",
    "prepare": "husky"
  },
  "keywords": [
    "ai",
    "context-governance",
    "spec-driven",
    "multi-agent",
    "automation"
  ],
  "author": "Tales Avancini",
  "license": "MIT",
  "devDependencies": {
    "husky": "^9.1.7"
  }
}

```
CHUNK_END id=7030d0b2f71b_c001
FILE_END id=file_7030d0b2f71b

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=144 bytes=5190 mtime=2026-04-22T23:16:30.370440+00:00 sha1=d888ea6eb9ffb21318a8abcb892c99af10ca6374
CHUNK_START id=350a79f8b829_c001 start_line=1 end_line=144
```python
#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto v2.5.0 (Hardened Pipeline)
Sequencia otimizada: validate → scan-secrets → sync → migrations → harness → lint(strict) → health
"""

import sys
import subprocess
from pathlib import Path

stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
stderr_reconfigure = getattr(sys.stderr, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")
if callable(stderr_reconfigure):
    stderr_reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"


def run_script(name, args=None, capture=False):
    if args is None:
        args = []
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)

    print(f"[RUN] Executando {name}...")
    try:
        # Refatoração sugerida pela auditoria: Remover check=True para tratar códigos semânticos
        res = subprocess.run([sys.executable, str(script_path)] + args, check=False)

        if res.returncode == 0:
            print(f"[OK] Concluido: {name}\n")
            return 0
        elif res.returncode == 2:
            print(f"[STRATEGIC BLOCK] Pendência em {name}. Pipeline local TRAVADO.\n")
            sys.exit(2)
        else:
            print(
                f"[FATAL] Falha estrutural em {name}. Exit: {res.returncode}. Pipeline abortado."
            )
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Erro na execução de {name}: {e}\n")
        sys.exit(1)


def get_inception_status():
    """Lê o status do Inception mestre."""
    path = BASE_DIR / ".context" / "brain" / "INCEPTION.md"
    if not path.exists():
        return "MISSING"
    try:
        content = path.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"


def main():
    if len(sys.argv) < 2:
        print(
            "[USAGE] python run_context.py [validate|purge|sync|cleanup|harness|lint|lint-strict|oracle|health|scan-secrets|check-migrations|check-version|enrich|all|help]"
        )
        sys.exit(1)

    cmd = sys.argv[1]
    extra_args = sys.argv[2:]

    # Bloqueio global preventivo (Auditoria: TRANSLATION_LOCK uniforme)
    status = get_inception_status()
    if status == "TRANSLATION_LOCK" and cmd != "enrich" and cmd != "help":
        print(
            "[LOCKED] O projeto está em TRANSLATION_LOCK. Aceite ou rejeite o INCEPTION.proposed.md primeiro."
        )
        sys.exit(2)

    if cmd == "validate":
        run_script("validate_context.py", extra_args)
    elif cmd == "purge":
        run_script("purge_journal.py", extra_args)
    elif cmd == "sync":
        run_script("sync_project.py", extra_args)
    elif cmd == "cleanup":
        run_script("cleanup_specs.py", extra_args)
    elif cmd == "harness":
        run_script("harness_runner.py", extra_args)
    elif cmd == "lint":
        run_script("lint_wiki.py", extra_args)
    elif cmd == "lint-strict":
        run_script("lint_wiki.py", ["--strict"] + extra_args)
    elif cmd == "oracle":
        run_script("context_oracle.py", extra_args)
    elif cmd == "health":
        run_script("health_sync.py", extra_args)
    elif cmd == "scan-secrets":
        run_script("secrets_scanner.py", extra_args)
    elif cmd == "check-migrations":
        run_script("migration_registry.py", extra_args)
    elif cmd == "check-version":
        run_script("check_version_consistency.py", extra_args)

    elif cmd == "enrich":
        run_script("enrich_context.py", extra_args)
    elif cmd == "ingest-guard":
        run_script("ingest_wiki_guard.py", extra_args)
    elif cmd == "wiki-health":
        run_script("validate_context.py", ["check_wiki_integrity"] + extra_args)

    elif cmd == "all":
        # Pipeline Fail-Fast (Hardened v2.5.0 + Hybrid Discovery)
        run_script("check_version_consistency.py")
        run_script("validate_context.py")
        run_script("secrets_scanner.py")
        run_script("sync_project.py")
        run_script("migration_registry.py")
        run_script("harness_runner.py")
        run_script("ingest_wiki_guard.py")
        print("[RUN] Executando lint_wiki.py (Strict)...")
        run_script("lint_wiki.py", ["--strict"])
        print("[RUN] Sincronizando Health Dashboard...")
        run_script("health_sync.py")
        print(
            "[DONE] Pipeline H.O.K. + Security + Migrations + Health concluído com sucesso."
        )

    elif cmd in ["help", "--help", "-h"]:
        print(
            "Comandos: validate | purge | sync | cleanup | harness | lint | lint-strict | oracle | health | scan-secrets | check-migrations | check-version | enrich | all"
        )
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()

```
CHUNK_END id=350a79f8b829_c001
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=17 bytes=798 mtime=2026-04-17T02:31:37.204327+00:00 sha1=a6c29d302d9d9c3f99917dd1da64da3d07f635ac
CHUNK_START id=86bac54f32d7_c001 start_line=1 end_line=17
```bash
#!/usr/bin/env bash
# ---------------------------------------------------------
# 🐚 run_context.sh - [DEPRECATED] Módulo Retido por Compatibilidade (v2.4.1)
# ---------------------------------------------------------
set -euo pipefail

echo -e "\033[1;33m[DEPRECATED]\033[0m O uso de 'run_context.sh' e desencorajado na v2.4.1+. Redirecionando para 'run_context.py'..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 🔍 Detecção robusta de Python na máquina host (para Linux/macOS)
if command -v python3 &>/dev/null; then PYTHON="python3"
elif command -v python &>/dev/null; then PYTHON="python"
else echo "❌ Erro: Python não encontrado no PATH."; exit 1; fi

# Delega argumentos diretamente para a engine unificada Python
exec $PYTHON "$SCRIPT_DIR/run_context.py" "$@"

```
CHUNK_END id=86bac54f32d7_c001
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=135 bytes=6249 mtime=2026-04-17T00:13:58.569614+00:00 sha1=9d17651da9da5326350654941d201d72c37c42c4
CHUNK_START id=4c6bbd05056e_c001 start_line=1 end_line=135
```python
import unittest
import os
import shutil
import tempfile
import subprocess
import sys
from pathlib import Path

class TestContextGovernance(unittest.TestCase):
    def setUp(self):
        # Cria diretório temporário para sandbox
        self.test_dir = Path(tempfile.mkdtemp())
        self.project_root = self.test_dir
        self.context_dir = self.project_root / ".context"
        self.scripts_dir = self.context_dir / "_scripts"
        
        # Caminho real dos scripts
        self.repo_root = Path(__file__).parent.parent
        self.real_scripts_dir = self.repo_root / ".context" / "_scripts"
        
        # Cria estrutura de camadas
        for layer in ["brain", "maintenance", "monitoring", "_scripts"]:
            (self.context_dir / layer).mkdir(parents=True, exist_ok=True)
        (self.context_dir / "maintenance" / "_archive_context" / "journals").mkdir(parents=True, exist_ok=True)

        # Copia scripts reais para o sandbox
        scripts_to_copy = ["validate_context.py", "purge_journal.py", "sync_project.py", "enrich_context.py", "harness_runner.py"]
        for script in scripts_to_copy:
            shutil.copy(self.real_scripts_dir / script, self.scripts_dir / script)

        # Cria arquivos base vazios
        for f in ["brain/RULES.md", "brain/MASTER_FLOW.md", "brain/AGENT_REGISTRY.md", "brain/PRD.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")
        
        for f in ["maintenance/schema.sql", "maintenance/TECHNICAL_REQUIREMENTS.md", "maintenance/JOURNAL.md"]:
            (self.context_dir / f).write_text("# Test", encoding="utf-8")

        # Configura Inception padrão
        (self.context_dir / "brain/INCEPTION.md").write_text("status: ACTIVE\nversion: 2.4.1", encoding="utf-8")

        self.python_cmd = sys.executable

    def tearDown(self):
        # Limpa sandbox
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def run_script(self, name):
        script_path = self.scripts_dir / name
        result = subprocess.run(
            [self.python_cmd, str(script_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=self.project_root
        )
        return result

    def test_onboarding_draft(self):
        """DRAFT + No Vision + Clean Context -> Exit 0"""
        (self.context_dir / "brain/INCEPTION.md").write_text("status: DRAFT", encoding="utf-8")
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        res = self.run_script("validate_context.py")
        self.assertEqual(res.returncode, 0)
        self.assertIn("[INFO] Modo Onboarding", res.stdout)

    def test_translation_pending(self):
        """DRAFT + VISION.md -> Exit 2"""
        (self.context_dir / "brain/INCEPTION.md").write_text("status: DRAFT", encoding="utf-8")
        (self.context_dir / "brain/VISION.md").write_text("Minha visão", encoding="utf-8")
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertEqual(res.returncode, 2)
        self.assertIn("[WARN] Tradução Pendente", res.stdout)
        
        res_enrich = self.run_script("enrich_context.py")
        self.assertEqual(res_enrich.returncode, 2)
        self.assertIn("[TRANSLATION_PENDING]", res_enrich.stdout)

    def test_translation_lock(self):
        """TRANSLATION_LOCK -> Exit 2"""
        (self.context_dir / "brain/INCEPTION.md").write_text("status: TRANSLATION_LOCK", encoding="utf-8")
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertEqual(res.returncode, 2)
        self.assertIn("[WARN] Bloqueio de Tradução", res.stdout)

    def test_dirty_draft(self):
        """DRAFT + Existing Code -> Exit 1 (Strategic Breach)"""
        (self.context_dir / "brain/INCEPTION.md").write_text("status: DRAFT", encoding="utf-8")
        (self.project_root / "src").mkdir()
        (self.project_root / "src/main.py").write_text("print()", encoding="utf-8")
        
        res = self.run_script("validate_context.py")
        self.assertEqual(res.returncode, 1)
        self.assertIn("[FATAL] Inception em DRAFT mas projeto possui código", res.stdout)

    def test_validate_integrity(self):
        """ACTIVE + Valid Context -> Exit 0"""
        (self.context_dir / "brain/AGENT_REGISTRY.md").write_text("| Role | Permissao |\n|---|---|", encoding="utf-8")
        res = self.run_script("validate_context.py")
        self.assertEqual(res.returncode, 0)
        self.assertIn("[SUCCESS]", res.stdout)

    def test_validate_missing_file(self):
        (self.context_dir / "brain/AGENT_REGISTRY.md").unlink()
        res = self.run_script("validate_context.py")
        self.assertIn("Arquivos ausentes", res.stdout)

    def test_purge_journal(self):
        journal = self.context_dir / "maintenance/JOURNAL.md"
        journal.write_text("## 📅 2024\nEntry 1\n\n## 📅 2024\nEntry 2", encoding="utf-8")
        res = self.run_script("purge_journal.py")
        self.assertIn("[OK] Purge concluido", res.stdout)
        
        # Verifica se arquivo foi criado no archive
        archive_files = list((self.context_dir / "maintenance/_archive_context/journals").glob("*.md"))
        self.assertGreaterEqual(len(archive_files), 1)

    def test_sync_project(self):
        # Simula package.json e schema.sql
        (self.project_root / "package.json").write_text('{"dependencies":{"test":"1.0"}}', encoding="utf-8")
        (self.context_dir / "maintenance/schema.sql").write_text("CREATE TABLE users (id INT);", encoding="utf-8")
        
        res = self.run_script("sync_project.py")
        self.assertIn("[OK] TECHNICAL_REQUIREMENTS.md sincronizado", res.stdout)
        
        req_content = (self.context_dir / "maintenance/TECHNICAL_REQUIREMENTS.md").read_text(encoding="utf-8")
        self.assertIn("users", req_content)
        self.assertIn("test", req_content)

if __name__ == "__main__":
    unittest.main()

```
CHUNK_END id=4c6bbd05056e_c001
FILE_END id=file_4c6bbd05056e
