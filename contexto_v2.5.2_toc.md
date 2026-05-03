# Project Context Bundle

---
schema_version: 1
generated_at: 2026-05-02T21:40:47.192881+00:00
root: template_inicío_de_projeto
mode: full | TOC
profile: ai-default
file_count: 111
byte_count: 445538
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
  - _flash_report
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
  - `.agent/subagents/qa-validator.md` -> [file_5a0c0f1b1bd0](#file_5a0c0f1b1bd0)
  - `.agent/subagents/spec-driver.md` -> [file_a412f1bb7017](#file_a412f1bb7017)
  - `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
  - `.context/brain/FILE_GLOSSARY.md` -> [file_14666768162a](#file_14666768162a)
  - `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
  - `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
  - `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
  - `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
  - `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
  - `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
  - `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
  - `.context/brain/SCRIPT_GLOSSARY.md` -> [file_aa59d3515582](#file_aa59d3515582)
  - `.context/brain/START_HERE.md` -> [file_e11d89201917](#file_e11d89201917)
  - `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
  - `.context/brain/VISION.md` -> [file_d2f31e4696a6](#file_d2f31e4696a6)
  - `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
  - `.context/maintenance/HARNESS_LOG.md` -> [file_41c3d3da4381](#file_41c3d3da4381)
  - `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
  - `.context/maintenance/JOURNAL_SYNAPSE.md` -> [file_cc20d1370d98](#file_cc20d1370d98)
  - `.context/maintenance/RX_REPOSITORIO.md` -> [file_ef714e7c8162](#file_ef714e7c8162)
  - `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
  - `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
  - `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
  - `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
  - `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
  - `.context/maintenance/rx-communications.md` -> [file_4f9504df2efc](#file_4f9504df2efc)
  - `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
  - `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
  - `.context/market/WIKI/_index.md` -> [file_578d56cac1a4](#file_578d56cac1a4)
  - `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
  - `.context/market/WIKI/concepts/harness_architecture.md` -> [file_d3053a37c321](#file_d3053a37c321)
  - `.context/market/WIKI/concepts/harness_behavior.md` -> [file_377d3d8e4da4](#file_377d3d8e4da4)
  - `.context/market/WIKI/concepts/harness_maintainability.md` -> [file_2589e52b2eed](#file_2589e52b2eed)
  - `.context/market/WIKI/concepts/ralph_wiggum_loop.md` -> [file_a19b6a994237](#file_a19b6a994237)
  - `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
  - `.context/market/wiki_log.md` -> [file_c255058b56fe](#file_c255058b56fe)
  - `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
  - `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
  - `.context/monitoring/PROJECT_INDEX.md` -> [file_3667001850eb](#file_3667001850eb)
  - `.specs/_template.md` -> [file_b838611f038c](#file_b838611f038c)
  - `.specs/features/SDD_ERRORS_LEDGER.md` -> [file_cec7fa80a0cf](#file_cec7fa80a0cf)
  - `.specs/features/SDD_PLAYBOOK.md` -> [file_b33d2a2116cd](#file_b33d2a2116cd)
  - `.specs/features/_arquive_features/harness_fail_closed/STATE.md` -> [file_5353fbc27cc1](#file_5353fbc27cc1)
  - `.specs/features/_arquive_features/harness_fail_closed/spec.md` -> [file_e56f737897cf](#file_e56f737897cf)
  - `.specs/features/_arquive_features/log_old_features.md` -> [file_f7b3adad01fe](#file_f7b3adad01fe)
  - `.specs/features/_arquive_features/meta-inception/STATE.md` -> [file_0fa0b6b078a5](#file_0fa0b6b078a5)
  - `.specs/features/_arquive_features/meta-inception/spec.md` -> [file_b544f5358fb0](#file_b544f5358fb0)
  - `.specs/features/_arquive_features/multi_agent_choreography/STATE.md` -> [file_976dca62e5de](#file_976dca62e5de)
  - `.specs/features/_arquive_features/multi_agent_choreography/spec.md` -> [file_dcdf7269aabc](#file_dcdf7269aabc)
  - `.specs/features/_arquive_features/oracle_v3/STATE.md` -> [file_3377cfe00b2d](#file_3377cfe00b2d)
  - `.specs/features/_arquive_features/oracle_v3/spec.md` -> [file_96f9097dbbd2](#file_96f9097dbbd2)
  - `.specs/features/_arquive_features/qa_subagent/STATE.md` -> [file_96a2bcfd8479](#file_96a2bcfd8479)
  - `.specs/features/_arquive_features/qa_subagent/spec.md` -> [file_07e43f982f2d](#file_07e43f982f2d)
  - `.specs/features/_arquive_features/sam_chronology_fix/STATE.md` -> [file_2bad8249610a](#file_2bad8249610a)
  - `.specs/features/_arquive_features/sam_chronology_fix/spec.md` -> [file_a969b2604ea8](#file_a969b2604ea8)
  - `.specs/features/_arquive_features/synapse_workflow/STATE.md` -> [file_a47ad3f11faa](#file_a47ad3f11faa)
  - `.specs/features/_arquive_features/synapse_workflow/spec.md` -> [file_08d15183b50c](#file_08d15183b50c)
  - `.specs/features/_arquive_features/wiki_level2/STATE.md` -> [file_26b5471905f2](#file_26b5471905f2)
  - `.specs/features/_arquive_features/wiki_level2/spec.md` -> [file_25a85d147e2a](#file_25a85d147e2a)
  - `.specs/features/_arquive_features/wiki_level2/tasks.md` -> [file_df9a30cacfaa](#file_df9a30cacfaa)
  - `.specs/features/_template_operacional/STATE.md` -> [file_1a22b8bd3423](#file_1a22b8bd3423)
  - `.specs/features/_template_operacional/design.md` -> [file_c26edabf0ec4](#file_c26edabf0ec4)
  - `.specs/features/_template_operacional/spec.md` -> [file_b3ffa4b3b701](#file_b3ffa4b3b701)
  - `.specs/features/_template_operacional/tasks.md` -> [file_7cde61057f28](#file_7cde61057f28)
  - `.specs/features/_template_operacional_sprint/CHECKLIST.md` -> [file_df91d6111d17](#file_df91d6111d17)
  - `.specs/features/_template_operacional_sprint/STATE.md` -> [file_dea2c04e539b](#file_dea2c04e539b)
  - `.specs/features/_template_operacional_sprint/design.md` -> [file_e8d353f63af3](#file_e8d353f63af3)
  - `.specs/features/_template_operacional_sprint/spec.md` -> [file_6c7ec05b2f9e](#file_6c7ec05b2f9e)
  - `.specs/features/_template_operacional_sprint/tasks.md` -> [file_f623b71a536c](#file_f623b71a536c)
  - `.specs/features/contract_sprints_v2_safe/STATE.md` -> [file_c6539441c702](#file_c6539441c702)
  - `.specs/features/contract_sprints_v2_safe/spec.md` -> [file_f26b9f244534](#file_f26b9f244534)
  - `.specs/features/contract_sprints_v2_safe/tasks.md` -> [file_4f8d9b00b4a4](#file_4f8d9b00b4a4)
  - `.specs/features/governance_rules_hardening/STATE.md` -> [file_c1d55217ac2a](#file_c1d55217ac2a)
  - `.specs/features/governance_rules_hardening/design.md` -> [file_99c81edef6ff](#file_99c81edef6ff)
  - `.specs/features/governance_rules_hardening/spec.md` -> [file_58b215a340da](#file_58b215a340da)
  - `.specs/features/governance_rules_hardening/tasks.md` -> [file_4f9bb146f536](#file_4f9bb146f536)
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
  - `.context/_scripts/oracle_analytics.py` -> [file_6e825c0bd6ad](#file_6e825c0bd6ad)
  - `.context/_scripts/project_bundler.py` -> [file_02d732116d93](#file_02d732116d93)
  - `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
  - `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
  - `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
  - `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
  - `.context/_scripts/workflow_journal_auditor.py` -> [file_8f42e61c8a29](#file_8f42e61c8a29)
  - `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
  - `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
  - `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
  - `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
  - `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
  - `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)
  - `tests/test_oracle.py` -> [file_357f74cc7014](#file_357f74cc7014)

## INDEX_BY_PATH
- `.agent/subagents/qa-validator.md` -> [file_5a0c0f1b1bd0](#file_5a0c0f1b1bd0)
- `.agent/subagents/spec-driver.md` -> [file_a412f1bb7017](#file_a412f1bb7017)
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
- `.context/_scripts/oracle_analytics.py` -> [file_6e825c0bd6ad](#file_6e825c0bd6ad)
- `.context/_scripts/project_bundler.py` -> [file_02d732116d93](#file_02d732116d93)
- `.context/_scripts/purge_journal.py` -> [file_024b28a37d29](#file_024b28a37d29)
- `.context/_scripts/secrets_scanner.py` -> [file_e98b95e5fb6d](#file_e98b95e5fb6d)
- `.context/_scripts/sync_project.py` -> [file_f122711ba9e1](#file_f122711ba9e1)
- `.context/_scripts/validate_context.py` -> [file_1077e9084ea1](#file_1077e9084ea1)
- `.context/_scripts/workflow_journal_auditor.py` -> [file_8f42e61c8a29](#file_8f42e61c8a29)
- `.context/brain/AGENT_REGISTRY.md` -> [file_e7c17acb71ff](#file_e7c17acb71ff)
- `.context/brain/FILE_GLOSSARY.md` -> [file_14666768162a](#file_14666768162a)
- `.context/brain/HARNESS_REGISTRY.md` -> [file_4b29e274836e](#file_4b29e274836e)
- `.context/brain/INCEPTION.md` -> [file_de9ef20db2be](#file_de9ef20db2be)
- `.context/brain/MASTER_FLOW.md` -> [file_d833c436f547](#file_d833c436f547)
- `.context/brain/PRD.md` -> [file_d124f6374cab](#file_d124f6374cab)
- `.context/brain/PROMPT_LIBRARY.md` -> [file_9fe16e5591f0](#file_9fe16e5591f0)
- `.context/brain/ROADMAP.md` -> [file_c94f001202db](#file_c94f001202db)
- `.context/brain/RULES.md` -> [file_cd6526d17218](#file_cd6526d17218)
- `.context/brain/SCRIPT_GLOSSARY.md` -> [file_aa59d3515582](#file_aa59d3515582)
- `.context/brain/START_HERE.md` -> [file_e11d89201917](#file_e11d89201917)
- `.context/brain/TLC_INTEGRATION.md` -> [file_450d7ec70909](#file_450d7ec70909)
- `.context/brain/VISION.md` -> [file_d2f31e4696a6](#file_d2f31e4696a6)
- `.context/maintenance/ARCHITECTURE.md` -> [file_9b6470da8849](#file_9b6470da8849)
- `.context/maintenance/HARNESS_LOG.md` -> [file_41c3d3da4381](#file_41c3d3da4381)
- `.context/maintenance/JOURNAL.md` -> [file_019509328844](#file_019509328844)
- `.context/maintenance/JOURNAL_SYNAPSE.md` -> [file_cc20d1370d98](#file_cc20d1370d98)
- `.context/maintenance/RX_REPOSITORIO.md` -> [file_ef714e7c8162](#file_ef714e7c8162)
- `.context/maintenance/TECHNICAL_REQUIREMENTS.md` -> [file_d069d4f2ebef](#file_d069d4f2ebef)
- `.context/maintenance/TESTS.md` -> [file_0858a02cf53f](#file_0858a02cf53f)
- `.context/maintenance/migrations/001_init.sql` -> [file_3707c3aa3239](#file_3707c3aa3239)
- `.context/maintenance/rebuild_guide.md` -> [file_a5c71962029a](#file_a5c71962029a)
- `.context/maintenance/rx-anatomy.md` -> [file_54a6a553d34b](#file_54a6a553d34b)
- `.context/maintenance/rx-biology.md` -> [file_ca8da4f87431](#file_ca8da4f87431)
- `.context/maintenance/rx-communications.md` -> [file_4f9504df2efc](#file_4f9504df2efc)
- `.context/maintenance/schema.sql` -> [file_91d5627a725e](#file_91d5627a725e)
- `.context/maintenance/version_targets.json` -> [file_51ed93c9d8ab](#file_51ed93c9d8ab)
- `.context/market/MARKET_INBOX.md` -> [file_81ef387da7b7](#file_81ef387da7b7)
- `.context/market/SSOT_MAP.md` -> [file_65a089176b85](#file_65a089176b85)
- `.context/market/WIKI/_index.md` -> [file_578d56cac1a4](#file_578d56cac1a4)
- `.context/market/WIKI/_template.md` -> [file_491684f3a96e](#file_491684f3a96e)
- `.context/market/WIKI/concepts/harness_architecture.md` -> [file_d3053a37c321](#file_d3053a37c321)
- `.context/market/WIKI/concepts/harness_behavior.md` -> [file_377d3d8e4da4](#file_377d3d8e4da4)
- `.context/market/WIKI/concepts/harness_maintainability.md` -> [file_2589e52b2eed](#file_2589e52b2eed)
- `.context/market/WIKI/concepts/ralph_wiggum_loop.md` -> [file_a19b6a994237](#file_a19b6a994237)
- `.context/market/economics.md` -> [file_b5d38697335e](#file_b5d38697335e)
- `.context/market/wiki_log.md` -> [file_c255058b56fe](#file_c255058b56fe)
- `.context/monitoring/CONTEXT_HEALTH.md` -> [file_068a21d64bec](#file_068a21d64bec)
- `.context/monitoring/EXECUTION_BUFFER.md` -> [file_c6d44cc7da35](#file_c6d44cc7da35)
- `.context/monitoring/PROJECT_INDEX.md` -> [file_3667001850eb](#file_3667001850eb)
- `.github/workflows/context-health.yml` -> [file_e477c4c5a96c](#file_e477c4c5a96c)
- `.husky/_/husky.sh` -> [file_3adfd36c1559](#file_3adfd36c1559)
- `.specs/_template.md` -> [file_b838611f038c](#file_b838611f038c)
- `.specs/features/SDD_ERRORS_LEDGER.md` -> [file_cec7fa80a0cf](#file_cec7fa80a0cf)
- `.specs/features/SDD_PLAYBOOK.md` -> [file_b33d2a2116cd](#file_b33d2a2116cd)
- `.specs/features/_arquive_features/harness_fail_closed/STATE.md` -> [file_5353fbc27cc1](#file_5353fbc27cc1)
- `.specs/features/_arquive_features/harness_fail_closed/spec.md` -> [file_e56f737897cf](#file_e56f737897cf)
- `.specs/features/_arquive_features/log_old_features.md` -> [file_f7b3adad01fe](#file_f7b3adad01fe)
- `.specs/features/_arquive_features/meta-inception/STATE.md` -> [file_0fa0b6b078a5](#file_0fa0b6b078a5)
- `.specs/features/_arquive_features/meta-inception/spec.md` -> [file_b544f5358fb0](#file_b544f5358fb0)
- `.specs/features/_arquive_features/multi_agent_choreography/STATE.md` -> [file_976dca62e5de](#file_976dca62e5de)
- `.specs/features/_arquive_features/multi_agent_choreography/spec.md` -> [file_dcdf7269aabc](#file_dcdf7269aabc)
- `.specs/features/_arquive_features/oracle_v3/STATE.md` -> [file_3377cfe00b2d](#file_3377cfe00b2d)
- `.specs/features/_arquive_features/oracle_v3/spec.md` -> [file_96f9097dbbd2](#file_96f9097dbbd2)
- `.specs/features/_arquive_features/qa_subagent/STATE.md` -> [file_96a2bcfd8479](#file_96a2bcfd8479)
- `.specs/features/_arquive_features/qa_subagent/spec.md` -> [file_07e43f982f2d](#file_07e43f982f2d)
- `.specs/features/_arquive_features/sam_chronology_fix/STATE.md` -> [file_2bad8249610a](#file_2bad8249610a)
- `.specs/features/_arquive_features/sam_chronology_fix/spec.md` -> [file_a969b2604ea8](#file_a969b2604ea8)
- `.specs/features/_arquive_features/synapse_workflow/STATE.md` -> [file_a47ad3f11faa](#file_a47ad3f11faa)
- `.specs/features/_arquive_features/synapse_workflow/spec.md` -> [file_08d15183b50c](#file_08d15183b50c)
- `.specs/features/_arquive_features/wiki_level2/STATE.md` -> [file_26b5471905f2](#file_26b5471905f2)
- `.specs/features/_arquive_features/wiki_level2/spec.md` -> [file_25a85d147e2a](#file_25a85d147e2a)
- `.specs/features/_arquive_features/wiki_level2/tasks.md` -> [file_df9a30cacfaa](#file_df9a30cacfaa)
- `.specs/features/_template_operacional/STATE.md` -> [file_1a22b8bd3423](#file_1a22b8bd3423)
- `.specs/features/_template_operacional/design.md` -> [file_c26edabf0ec4](#file_c26edabf0ec4)
- `.specs/features/_template_operacional/spec.md` -> [file_b3ffa4b3b701](#file_b3ffa4b3b701)
- `.specs/features/_template_operacional/tasks.md` -> [file_7cde61057f28](#file_7cde61057f28)
- `.specs/features/_template_operacional_sprint/CHECKLIST.md` -> [file_df91d6111d17](#file_df91d6111d17)
- `.specs/features/_template_operacional_sprint/STATE.md` -> [file_dea2c04e539b](#file_dea2c04e539b)
- `.specs/features/_template_operacional_sprint/design.md` -> [file_e8d353f63af3](#file_e8d353f63af3)
- `.specs/features/_template_operacional_sprint/spec.md` -> [file_6c7ec05b2f9e](#file_6c7ec05b2f9e)
- `.specs/features/_template_operacional_sprint/tasks.md` -> [file_f623b71a536c](#file_f623b71a536c)
- `.specs/features/contract_sprints_v2_safe/STATE.md` -> [file_c6539441c702](#file_c6539441c702)
- `.specs/features/contract_sprints_v2_safe/spec.md` -> [file_f26b9f244534](#file_f26b9f244534)
- `.specs/features/contract_sprints_v2_safe/tasks.md` -> [file_4f8d9b00b4a4](#file_4f8d9b00b4a4)
- `.specs/features/governance_rules_hardening/STATE.md` -> [file_c1d55217ac2a](#file_c1d55217ac2a)
- `.specs/features/governance_rules_hardening/design.md` -> [file_99c81edef6ff](#file_99c81edef6ff)
- `.specs/features/governance_rules_hardening/spec.md` -> [file_58b215a340da](#file_58b215a340da)
- `.specs/features/governance_rules_hardening/tasks.md` -> [file_4f9bb146f536](#file_4f9bb146f536)
- `GUIA_ESTABILIZACAO_NOTEBOOKLM.md` -> [file_95dabcdf3543](#file_95dabcdf3543)
- `README.md` -> [file_8ec9a00bfd09](#file_8ec9a00bfd09)
- `README_CONTEXT.md` -> [file_4efb6293109d](#file_4efb6293109d)
- `TEMPLATE_MIGRATION.md` -> [file_19e76e009f38](#file_19e76e009f38)
- `VERSION.md` -> [file_f6f7100f063b](#file_f6f7100f063b)
- `_modoLight/Modo_Light.md` -> [file_1f98938d3cd9](#file_1f98938d3cd9)
- `init_ai_project.sh` -> [file_c59135753d26](#file_c59135753d26)
- `package.json` -> [file_7030d0b2f71b](#file_7030d0b2f71b)
- `run_context.py` -> [file_350a79f8b829](#file_350a79f8b829)
- `run_context.sh` -> [file_86bac54f32d7](#file_86bac54f32d7)
- `tests/test_context.py` -> [file_4c6bbd05056e](#file_4c6bbd05056e)
- `tests/test_oracle.py` -> [file_357f74cc7014](#file_357f74cc7014)

---
<a id="file_5a0c0f1b1bd0"></a>
FILE_START id=file_5a0c0f1b1bd0 path=.agent/subagents/qa-validator.md domain=docs lang=markdown lines=34 bytes=1910 mtime=2026-04-30T21:18:30.151867+00:00 sha1=a48e251779eb5cf186a998851e4d02704db7dcdf
CONTENT_OMITTED toc_only=true
FILE_END id=file_5a0c0f1b1bd0

---
<a id="file_a412f1bb7017"></a>
FILE_START id=file_a412f1bb7017 path=.agent/subagents/spec-driver.md domain=docs lang=markdown lines=24 bytes=1834 mtime=2026-04-29T03:51:20.865135+00:00 sha1=c6e6648d2a635418ed4f7d36998c01b89b0bb4bb
CONTENT_OMITTED toc_only=true
FILE_END id=file_a412f1bb7017

---
<a id="file_dbef1acce0d4"></a>
FILE_START id=file_dbef1acce0d4 path=.context/_scripts/_tz_utils.py domain=source lang=python lines=37 bytes=1257 mtime=2026-04-12T02:47:25.198957+00:00 sha1=a49568f45d4b962ab01f0ed4b359ee4c09f65741
CONTENT_OMITTED toc_only=true
FILE_END id=file_dbef1acce0d4

---
<a id="file_9ee5d49278ad"></a>
FILE_START id=file_9ee5d49278ad path=.context/_scripts/_wiki_log_utils.py domain=source lang=python lines=66 bytes=2586 mtime=2026-04-29T23:25:43.168444+00:00 sha1=9eee06f81a5d98bdda3ce503a7ddc2b3b3d64b86
CONTENT_OMITTED toc_only=true
FILE_END id=file_9ee5d49278ad

---
<a id="file_4ffe1a34765a"></a>
FILE_START id=file_4ffe1a34765a path=.context/_scripts/check_version_consistency.py domain=source lang=python lines=80 bytes=2486 mtime=2026-04-22T12:37:52.914197+00:00 sha1=0f0bcd180ff803df099fc5f865ce6d3106e196d2
CONTENT_OMITTED toc_only=true
FILE_END id=file_4ffe1a34765a

---
<a id="file_82cd6bde54ff"></a>
FILE_START id=file_82cd6bde54ff path=.context/_scripts/cleanup_specs.py domain=source lang=python lines=102 bytes=3655 mtime=2026-04-30T22:03:01.202091+00:00 sha1=362bd063cb5f099b6d28f99c135093ce4c3559ce
CONTENT_OMITTED toc_only=true
FILE_END id=file_82cd6bde54ff

---
<a id="file_10081abf87e1"></a>
FILE_START id=file_10081abf87e1 path=.context/_scripts/context_oracle.py domain=source lang=python lines=200 bytes=8477 mtime=2026-04-29T23:44:35.875177+00:00 sha1=be9c070b99c0a242757843d869e9ef38d1410613
CONTENT_OMITTED toc_only=true
FILE_END id=file_10081abf87e1

---
<a id="file_e94b4e40315c"></a>
FILE_START id=file_e94b4e40315c path=.context/_scripts/enrich_context.py domain=source lang=python lines=125 bytes=4876 mtime=2026-04-17T00:17:17.361963+00:00 sha1=6ab638ce0553fdafde495ea2f64fc30ae300f765
CONTENT_OMITTED toc_only=true
FILE_END id=file_e94b4e40315c

---
<a id="file_1edef35c2f56"></a>
FILE_START id=file_1edef35c2f56 path=.context/_scripts/harness_runner.py domain=source lang=python lines=647 bytes=26097 mtime=2026-04-30T21:55:22.603573+00:00 sha1=6ee3838b43644369ac98d779ca33c1e134c3970b
CONTENT_OMITTED toc_only=true
FILE_END id=file_1edef35c2f56

---
<a id="file_a642d240b9ab"></a>
FILE_START id=file_a642d240b9ab path=.context/_scripts/health_sync.py domain=source lang=python lines=111 bytes=4132 mtime=2026-04-12T03:40:11.302253+00:00 sha1=1f23d31d0c88fe19ee916b4d6dd9676fb2f0018b
CONTENT_OMITTED toc_only=true
FILE_END id=file_a642d240b9ab

---
<a id="file_0731dcfd7873"></a>
FILE_START id=file_0731dcfd7873 path=.context/_scripts/ingest_wiki_guard.py domain=source lang=python lines=131 bytes=4932 mtime=2026-04-29T23:05:09.652881+00:00 sha1=40b8732e20e069a48afd820b2c56a395e27a5c26
CONTENT_OMITTED toc_only=true
FILE_END id=file_0731dcfd7873

---
<a id="file_ab41b07fb3fb"></a>
FILE_START id=file_ab41b07fb3fb path=.context/_scripts/lint_wiki.py domain=source lang=python lines=116 bytes=4999 mtime=2026-04-22T23:34:42.090035+00:00 sha1=844cbc05474f73fa7addd3038fbbc60b86ab460a
CONTENT_OMITTED toc_only=true
FILE_END id=file_ab41b07fb3fb

---
<a id="file_d65b48a9d56c"></a>
FILE_START id=file_d65b48a9d56c path=.context/_scripts/migration_registry.py domain=source lang=python lines=44 bytes=1700 mtime=2026-04-12T02:18:47.875961+00:00 sha1=a1e9beb894aba2b44931e9c41522a020b7359ebf
CONTENT_OMITTED toc_only=true
FILE_END id=file_d65b48a9d56c

---
<a id="file_6e825c0bd6ad"></a>
FILE_START id=file_6e825c0bd6ad path=.context/_scripts/oracle_analytics.py domain=source lang=python lines=60 bytes=2162 mtime=2026-04-29T23:37:15.393689+00:00 sha1=7d8c8c35739ed1ff63529220af41f1f2204753fa
CONTENT_OMITTED toc_only=true
FILE_END id=file_6e825c0bd6ad

---
<a id="file_02d732116d93"></a>
FILE_START id=file_02d732116d93 path=.context/_scripts/project_bundler.py domain=source lang=python lines=429 bytes=17861 mtime=2026-04-30T01:25:29.689806+00:00 sha1=9567f0399ca22a577183619b877e92abd8c6c5df
CONTENT_OMITTED toc_only=true
FILE_END id=file_02d732116d93

---
<a id="file_024b28a37d29"></a>
FILE_START id=file_024b28a37d29 path=.context/_scripts/purge_journal.py domain=source lang=python lines=82 bytes=2761 mtime=2026-04-12T02:48:42.689091+00:00 sha1=8b12ecb77b7b91c035a2d7c9752910c71064d1e5
CONTENT_OMITTED toc_only=true
FILE_END id=file_024b28a37d29

---
<a id="file_e98b95e5fb6d"></a>
FILE_START id=file_e98b95e5fb6d path=.context/_scripts/secrets_scanner.py domain=source lang=python lines=69 bytes=2622 mtime=2026-04-14T12:47:41.549578+00:00 sha1=f73abf4fe2fa1a6e146de3fefae50c9016b77045
CONTENT_OMITTED toc_only=true
FILE_END id=file_e98b95e5fb6d

---
<a id="file_f122711ba9e1"></a>
FILE_START id=file_f122711ba9e1 path=.context/_scripts/sync_project.py domain=source lang=python lines=102 bytes=3426 mtime=2026-04-12T02:48:59.755191+00:00 sha1=d2b0f3541ccaab8c75f381f47d539c762618a0b7
CONTENT_OMITTED toc_only=true
FILE_END id=file_f122711ba9e1

---
<a id="file_1077e9084ea1"></a>
FILE_START id=file_1077e9084ea1 path=.context/_scripts/validate_context.py domain=source lang=python lines=517 bytes=18055 mtime=2026-05-01T02:16:16.212265+00:00 sha1=3e592b584a869dc0b3ad8cb07a5905a624c29c3e
CONTENT_OMITTED toc_only=true
FILE_END id=file_1077e9084ea1

---
<a id="file_8f42e61c8a29"></a>
FILE_START id=file_8f42e61c8a29 path=.context/_scripts/workflow_journal_auditor.py domain=source lang=python lines=173 bytes=7728 mtime=2026-05-01T02:24:27.604653+00:00 sha1=25d482d6d9667483e2df6d8027779bca9ec86234
CONTENT_OMITTED toc_only=true
FILE_END id=file_8f42e61c8a29

---
<a id="file_e7c17acb71ff"></a>
FILE_START id=file_e7c17acb71ff path=.context/brain/AGENT_REGISTRY.md domain=docs lang=markdown lines=149 bytes=11038 mtime=2026-05-01T02:25:33.691912+00:00 sha1=1c59c742e176cf3574f563648161585c7b171493
CONTENT_OMITTED toc_only=true
FILE_END id=file_e7c17acb71ff

---
<a id="file_14666768162a"></a>
FILE_START id=file_14666768162a path=.context/brain/FILE_GLOSSARY.md domain=docs lang=markdown lines=98 bytes=7394 mtime=2026-05-01T03:54:28.688421+00:00 sha1=edb91217402d03f000b08ce01192f00bd1b536ed
CONTENT_OMITTED toc_only=true
FILE_END id=file_14666768162a

---
<a id="file_4b29e274836e"></a>
FILE_START id=file_4b29e274836e path=.context/brain/HARNESS_REGISTRY.md domain=docs lang=markdown lines=21 bytes=1331 mtime=2026-05-01T01:49:50.086418+00:00 sha1=ef00f95720c4a3a5def076c77dc1ab64ad4c37dc
CONTENT_OMITTED toc_only=true
FILE_END id=file_4b29e274836e

---
<a id="file_de9ef20db2be"></a>
FILE_START id=file_de9ef20db2be path=.context/brain/INCEPTION.md domain=docs lang=markdown lines=43 bytes=3455 mtime=2026-04-23T15:10:01.045421+00:00 sha1=1c3639bff80071b9781712b04dfd7edd74ca73bc
CONTENT_OMITTED toc_only=true
FILE_END id=file_de9ef20db2be

---
<a id="file_d833c436f547"></a>
FILE_START id=file_d833c436f547 path=.context/brain/MASTER_FLOW.md domain=docs lang=markdown lines=161 bytes=10288 mtime=2026-05-01T03:17:59.846263+00:00 sha1=237ed0670b66bc5daea1b5113dc8ab1fdc50c038
CONTENT_OMITTED toc_only=true
FILE_END id=file_d833c436f547

---
<a id="file_d124f6374cab"></a>
FILE_START id=file_d124f6374cab path=.context/brain/PRD.md domain=docs lang=markdown lines=29 bytes=1406 mtime=2026-04-17T01:21:43.543040+00:00 sha1=c75b72944c19fabc58237fb903784cb79ae6b4da
CONTENT_OMITTED toc_only=true
FILE_END id=file_d124f6374cab

---
<a id="file_9fe16e5591f0"></a>
FILE_START id=file_9fe16e5591f0 path=.context/brain/PROMPT_LIBRARY.md domain=docs lang=markdown lines=242 bytes=11813 mtime=2026-05-01T01:50:10.792730+00:00 sha1=5cd3fb95cf8da526073a048446b9ce2ae94e9a8d
CONTENT_OMITTED toc_only=true
FILE_END id=file_9fe16e5591f0

---
<a id="file_c94f001202db"></a>
FILE_START id=file_c94f001202db path=.context/brain/ROADMAP.md domain=docs lang=markdown lines=15 bytes=719 mtime=2026-04-21T23:32:04.607493+00:00 sha1=55fb929dd00b9a0eff1c9a253ec37e0609445e92
CONTENT_OMITTED toc_only=true
FILE_END id=file_c94f001202db

---
<a id="file_cd6526d17218"></a>
FILE_START id=file_cd6526d17218 path=.context/brain/RULES.md domain=docs lang=markdown lines=177 bytes=13033 mtime=2026-05-01T00:55:32.442355+00:00 sha1=4cf24140ce9676d5b60b30d5037164e72bd67128
CONTENT_OMITTED toc_only=true
FILE_END id=file_cd6526d17218

---
<a id="file_aa59d3515582"></a>
FILE_START id=file_aa59d3515582 path=.context/brain/SCRIPT_GLOSSARY.md domain=docs lang=markdown lines=77 bytes=6590 mtime=2026-05-01T01:49:57.046373+00:00 sha1=71ddc55326f96abc82d0b7bda46e6e47f9bdeb2f
CONTENT_OMITTED toc_only=true
FILE_END id=file_aa59d3515582

---
<a id="file_e11d89201917"></a>
FILE_START id=file_e11d89201917 path=.context/brain/START_HERE.md domain=docs lang=markdown lines=42 bytes=1749 mtime=2026-04-17T00:07:25.637908+00:00 sha1=482d0d056987215305ae88da18b37a59faa64658
CONTENT_OMITTED toc_only=true
FILE_END id=file_e11d89201917

---
<a id="file_450d7ec70909"></a>
FILE_START id=file_450d7ec70909 path=.context/brain/TLC_INTEGRATION.md domain=docs lang=markdown lines=57 bytes=3381 mtime=2026-04-30T17:10:44.443731+00:00 sha1=62eea4d3afa318562bae15b2adf6f87a056c7553
CONTENT_OMITTED toc_only=true
FILE_END id=file_450d7ec70909

---
<a id="file_d2f31e4696a6"></a>
FILE_START id=file_d2f31e4696a6 path=.context/brain/VISION.md domain=docs lang=markdown lines=44 bytes=7254 mtime=2026-04-23T15:26:57.151891+00:00 sha1=43246ab516dda1697b1efe4e634120aebce63c56
CONTENT_OMITTED toc_only=true
FILE_END id=file_d2f31e4696a6

---
<a id="file_9b6470da8849"></a>
FILE_START id=file_9b6470da8849 path=.context/maintenance/ARCHITECTURE.md domain=docs lang=markdown lines=17 bytes=827 mtime=2026-04-21T23:31:39.053793+00:00 sha1=e56f0939f55e5a0897bf89642150226cb048abd1
CONTENT_OMITTED toc_only=true
FILE_END id=file_9b6470da8849

---
<a id="file_41c3d3da4381"></a>
FILE_START id=file_41c3d3da4381 path=.context/maintenance/HARNESS_LOG.md domain=docs lang=markdown lines=479 bytes=21804 mtime=2026-05-01T01:40:52.353780+00:00 sha1=52fa8f0e2d876dc0bc4bbe2722d7db2234c0a785
CONTENT_OMITTED toc_only=true
FILE_END id=file_41c3d3da4381

---
<a id="file_019509328844"></a>
FILE_START id=file_019509328844 path=.context/maintenance/JOURNAL.md domain=docs lang=markdown lines=573 bytes=33183 mtime=2026-05-01T03:54:46.464985+00:00 sha1=0dec8995a89398f02b4eb807eabb2c0db57f5a7a
CONTENT_OMITTED toc_only=true
FILE_END id=file_019509328844

---
<a id="file_cc20d1370d98"></a>
FILE_START id=file_cc20d1370d98 path=.context/maintenance/JOURNAL_SYNAPSE.md domain=docs lang=markdown lines=51 bytes=1690 mtime=2026-04-24T17:11:19.470439+00:00 sha1=ec593364edce7aa5584a7ac651525ea5387ff8a5
CONTENT_OMITTED toc_only=true
FILE_END id=file_cc20d1370d98

---
<a id="file_ef714e7c8162"></a>
FILE_START id=file_ef714e7c8162 path=.context/maintenance/RX_REPOSITORIO.md domain=docs lang=markdown lines=71 bytes=4570 mtime=2026-04-26T19:08:42.983773+00:00 sha1=22df80c224f92b26457f149c2f39d41ea9b8ce1d
CONTENT_OMITTED toc_only=true
FILE_END id=file_ef714e7c8162

---
<a id="file_d069d4f2ebef"></a>
FILE_START id=file_d069d4f2ebef path=.context/maintenance/TECHNICAL_REQUIREMENTS.md domain=docs lang=markdown lines=149 bytes=1010 mtime=2026-04-29T04:34:53.625388+00:00 sha1=b094637e9fa390ab5587964baff5244f35fd89c5
CONTENT_OMITTED toc_only=true
FILE_END id=file_d069d4f2ebef

---
<a id="file_0858a02cf53f"></a>
FILE_START id=file_0858a02cf53f path=.context/maintenance/TESTS.md domain=docs lang=markdown lines=14 bytes=487 mtime=2026-04-21T23:31:41.224778+00:00 sha1=41caf1bd5e6bf513c1924db0b4dca9fb6f92322b
CONTENT_OMITTED toc_only=true
FILE_END id=file_0858a02cf53f

---
<a id="file_3707c3aa3239"></a>
FILE_START id=file_3707c3aa3239 path=.context/maintenance/migrations/001_init.sql domain=db lang=sql lines=12 bytes=450 mtime=2026-04-12T02:14:15.429255+00:00 sha1=a4e5465634cd084041656f59f9093be09f5a8fc9
CONTENT_OMITTED toc_only=true
FILE_END id=file_3707c3aa3239

---
<a id="file_a5c71962029a"></a>
FILE_START id=file_a5c71962029a path=.context/maintenance/rebuild_guide.md domain=docs lang=markdown lines=63 bytes=1988 mtime=2026-04-11T00:43:15.350621+00:00 sha1=28659c89fedac91d1973177b8cedcf60ad5f622a
CONTENT_OMITTED toc_only=true
FILE_END id=file_a5c71962029a

---
<a id="file_54a6a553d34b"></a>
FILE_START id=file_54a6a553d34b path=.context/maintenance/rx-anatomy.md domain=docs lang=markdown lines=35 bytes=2209 mtime=2026-04-26T20:05:14.112951+00:00 sha1=ff59b0326c4c35941a940ff02e478302cae30f20
CONTENT_OMITTED toc_only=true
FILE_END id=file_54a6a553d34b

---
<a id="file_ca8da4f87431"></a>
FILE_START id=file_ca8da4f87431 path=.context/maintenance/rx-biology.md domain=docs lang=markdown lines=75 bytes=3568 mtime=2026-04-26T03:54:11.545017+00:00 sha1=af5a04f2f81eaec0af44c847f35ce989c100faae
CONTENT_OMITTED toc_only=true
FILE_END id=file_ca8da4f87431

---
<a id="file_4f9504df2efc"></a>
FILE_START id=file_4f9504df2efc path=.context/maintenance/rx-communications.md domain=docs lang=markdown lines=97 bytes=3437 mtime=2026-05-01T03:51:00.422129+00:00 sha1=546539fe3ab0161ef5bdee5f7c741f976c805fca
CONTENT_OMITTED toc_only=true
FILE_END id=file_4f9504df2efc

---
<a id="file_91d5627a725e"></a>
FILE_START id=file_91d5627a725e path=.context/maintenance/schema.sql domain=source lang=sql lines=9 bytes=334 mtime=2026-04-11T01:25:08.344668+00:00 sha1=1814fd1f837ef5f31c2a6031222ba3055f9fd3c8
CONTENT_OMITTED toc_only=true
FILE_END id=file_91d5627a725e

---
<a id="file_51ed93c9d8ab"></a>
FILE_START id=file_51ed93c9d8ab path=.context/maintenance/version_targets.json domain=config lang=json lines=22 bytes=538 mtime=2026-04-22T12:37:34.654694+00:00 sha1=c2279f3056490c43cd112154c87f7b6b97e852ac
CONTENT_OMITTED toc_only=true
FILE_END id=file_51ed93c9d8ab

---
<a id="file_81ef387da7b7"></a>
FILE_START id=file_81ef387da7b7 path=.context/market/MARKET_INBOX.md domain=docs lang=markdown lines=11 bytes=341 mtime=2026-04-15T19:15:21.935146+00:00 sha1=66adcca82c5eae73d386371aef29795c87e283b3
CONTENT_OMITTED toc_only=true
FILE_END id=file_81ef387da7b7

---
<a id="file_65a089176b85"></a>
FILE_START id=file_65a089176b85 path=.context/market/SSOT_MAP.md domain=docs lang=markdown lines=28 bytes=1933 mtime=2026-04-24T00:53:50.356599+00:00 sha1=bb3a4cfc6e8100499b964cc7af0d4144a647f95d
CONTENT_OMITTED toc_only=true
FILE_END id=file_65a089176b85

---
<a id="file_578d56cac1a4"></a>
FILE_START id=file_578d56cac1a4 path=.context/market/WIKI/_index.md domain=docs lang=markdown lines=8 bytes=683 mtime=2026-04-29T22:57:40.778023+00:00 sha1=88e95b638c8214ffe557e70ecbf62f5201d72323
CONTENT_OMITTED toc_only=true
FILE_END id=file_578d56cac1a4

---
<a id="file_491684f3a96e"></a>
FILE_START id=file_491684f3a96e path=.context/market/WIKI/_template.md domain=docs lang=markdown lines=26 bytes=451 mtime=2026-04-21T21:52:58.658989+00:00 sha1=cff3271c1a095ae525f40835ebdcf49adc208d3a
CONTENT_OMITTED toc_only=true
FILE_END id=file_491684f3a96e

---
<a id="file_d3053a37c321"></a>
FILE_START id=file_d3053a37c321 path=.context/market/WIKI/concepts/harness_architecture.md domain=docs lang=markdown lines=42 bytes=3676 mtime=2026-04-24T00:58:55.142319+00:00 sha1=5ce062b892682b4b0d1027859f571880ae8fd219
CONTENT_OMITTED toc_only=true
FILE_END id=file_d3053a37c321

---
<a id="file_377d3d8e4da4"></a>
FILE_START id=file_377d3d8e4da4 path=.context/market/WIKI/concepts/harness_behavior.md domain=docs lang=markdown lines=42 bytes=3379 mtime=2026-04-24T01:00:54.793992+00:00 sha1=a51761fa79dfb0fdf782ed146f1c90415a342b76
CONTENT_OMITTED toc_only=true
FILE_END id=file_377d3d8e4da4

---
<a id="file_2589e52b2eed"></a>
FILE_START id=file_2589e52b2eed path=.context/market/WIKI/concepts/harness_maintainability.md domain=docs lang=markdown lines=41 bytes=3150 mtime=2026-04-24T00:54:26.558700+00:00 sha1=e09e05c4338ed20e592d9eb79ea7f43ff67aa681
CONTENT_OMITTED toc_only=true
FILE_END id=file_2589e52b2eed

---
<a id="file_a19b6a994237"></a>
FILE_START id=file_a19b6a994237 path=.context/market/WIKI/concepts/ralph_wiggum_loop.md domain=docs lang=markdown lines=43 bytes=2953 mtime=2026-04-24T01:03:27.706309+00:00 sha1=e6a0a485d4afe6b61264be774b38a3c771f83a48
CONTENT_OMITTED toc_only=true
FILE_END id=file_a19b6a994237

---
<a id="file_b5d38697335e"></a>
FILE_START id=file_b5d38697335e path=.context/market/economics.md domain=docs lang=markdown lines=7 bytes=109 mtime=2026-04-15T17:50:11.975520+00:00 sha1=17852efa34dbaea46351dcabac87aa67286e2e93
CONTENT_OMITTED toc_only=true
FILE_END id=file_b5d38697335e

---
<a id="file_c255058b56fe"></a>
FILE_START id=file_c255058b56fe path=.context/market/wiki_log.md domain=docs lang=markdown lines=53 bytes=5131 mtime=2026-04-29T23:30:56.879877+00:00 sha1=2d421e2d6672672b17f7eee82146c1504748252f
CONTENT_OMITTED toc_only=true
FILE_END id=file_c255058b56fe

---
<a id="file_068a21d64bec"></a>
FILE_START id=file_068a21d64bec path=.context/monitoring/CONTEXT_HEALTH.md domain=docs lang=markdown lines=38 bytes=1503 mtime=2026-04-29T04:34:54.863691+00:00 sha1=6b946c25c3816a3d043008c21610cc1c9ff51ada
CONTENT_OMITTED toc_only=true
FILE_END id=file_068a21d64bec

---
<a id="file_c6d44cc7da35"></a>
FILE_START id=file_c6d44cc7da35 path=.context/monitoring/EXECUTION_BUFFER.md domain=docs lang=markdown lines=10 bytes=327 mtime=2026-04-18T14:24:14.955191+00:00 sha1=d7989e55f1d5b4c9c8c2fa6057d6c8407b80e134
CONTENT_OMITTED toc_only=true
FILE_END id=file_c6d44cc7da35

---
<a id="file_3667001850eb"></a>
FILE_START id=file_3667001850eb path=.context/monitoring/PROJECT_INDEX.md domain=docs lang=markdown lines=788 bytes=42817 mtime=2026-04-30T01:27:51.106455+00:00 sha1=2696f291a60390cf7408fa1265814f82b5527fb0
CONTENT_OMITTED toc_only=true
FILE_END id=file_3667001850eb

---
<a id="file_e477c4c5a96c"></a>
FILE_START id=file_e477c4c5a96c path=.github/workflows/context-health.yml domain=config lang=yaml lines=25 bytes=569 mtime=2026-04-14T12:47:48.321567+00:00 sha1=7c7488139d3c3c4327aa9889700f683ee1f47be1
CONTENT_OMITTED toc_only=true
FILE_END id=file_e477c4c5a96c

---
<a id="file_3adfd36c1559"></a>
FILE_START id=file_3adfd36c1559 path=.husky/_/husky.sh domain=source lang=bash lines=9 bytes=160 mtime=2026-04-11T01:12:06.610441+00:00 sha1=e8c52ee10c10eaa739ae7eca69c373dd437d9f33
CONTENT_OMITTED toc_only=true
FILE_END id=file_3adfd36c1559

---
<a id="file_b838611f038c"></a>
FILE_START id=file_b838611f038c path=.specs/_template.md domain=docs lang=markdown lines=65 bytes=2402 mtime=2026-04-30T20:28:38.924724+00:00 sha1=7526208de9157806c4685e14b981fdf5ae7f4b4a
CONTENT_OMITTED toc_only=true
FILE_END id=file_b838611f038c

---
<a id="file_cec7fa80a0cf"></a>
FILE_START id=file_cec7fa80a0cf path=.specs/features/SDD_ERRORS_LEDGER.md domain=docs lang=markdown lines=62 bytes=2999 mtime=2026-05-01T00:48:12.356318+00:00 sha1=6d8037e0a1d268508bc7bb75642e309b2fa44388
CONTENT_OMITTED toc_only=true
FILE_END id=file_cec7fa80a0cf

---
<a id="file_b33d2a2116cd"></a>
FILE_START id=file_b33d2a2116cd path=.specs/features/SDD_PLAYBOOK.md domain=docs lang=markdown lines=77 bytes=2967 mtime=2026-05-01T00:47:51.926370+00:00 sha1=74d175bb8255fd3c1549d2d3a1cbebbe787925fc
CONTENT_OMITTED toc_only=true
FILE_END id=file_b33d2a2116cd

---
<a id="file_5353fbc27cc1"></a>
FILE_START id=file_5353fbc27cc1 path=.specs/features/_arquive_features/harness_fail_closed/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-22T23:02:55.455444+00:00 sha1=a627e9b0e39cebcd966bff38fff2869fb72544c9
CONTENT_OMITTED toc_only=true
FILE_END id=file_5353fbc27cc1

---
<a id="file_e56f737897cf"></a>
FILE_START id=file_e56f737897cf path=.specs/features/_arquive_features/harness_fail_closed/spec.md domain=docs lang=markdown lines=14 bytes=630 mtime=2026-04-21T22:16:15.283651+00:00 sha1=32ea04febe6e93d0fa8959cc525575f3bd2bb3eb
CONTENT_OMITTED toc_only=true
FILE_END id=file_e56f737897cf

---
<a id="file_f7b3adad01fe"></a>
FILE_START id=file_f7b3adad01fe path=.specs/features/_arquive_features/log_old_features.md domain=docs lang=markdown lines=16 bytes=1320 mtime=2026-04-30T16:29:51.864349+00:00 sha1=5a3dec8453cc6c11eb0ad1f510ee5be33aca9f4e
CONTENT_OMITTED toc_only=true
FILE_END id=file_f7b3adad01fe

---
<a id="file_0fa0b6b078a5"></a>
FILE_START id=file_0fa0b6b078a5 path=.specs/features/_arquive_features/meta-inception/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-21T22:01:44.285888+00:00 sha1=4647d09b6cba8ee228ab2e51d8c647537a9c41a5
CONTENT_OMITTED toc_only=true
FILE_END id=file_0fa0b6b078a5

---
<a id="file_b544f5358fb0"></a>
FILE_START id=file_b544f5358fb0 path=.specs/features/_arquive_features/meta-inception/spec.md domain=docs lang=markdown lines=30 bytes=1389 mtime=2026-04-17T14:33:18.003175+00:00 sha1=0cd48f6f6251020721a35d1efcec750576473d60
CONTENT_OMITTED toc_only=true
FILE_END id=file_b544f5358fb0

---
<a id="file_976dca62e5de"></a>
FILE_START id=file_976dca62e5de path=.specs/features/_arquive_features/multi_agent_choreography/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-29T04:34:54.226138+00:00 sha1=71453a8519bf6455452aa7e57c7f54e04369c8b6
CONTENT_OMITTED toc_only=true
FILE_END id=file_976dca62e5de

---
<a id="file_dcdf7269aabc"></a>
FILE_START id=file_dcdf7269aabc path=.specs/features/_arquive_features/multi_agent_choreography/spec.md domain=docs lang=markdown lines=30 bytes=2015 mtime=2026-04-29T04:33:53.553136+00:00 sha1=7594877b728618e362c2938b4ea4d50f03d8baaa
CONTENT_OMITTED toc_only=true
FILE_END id=file_dcdf7269aabc

---
<a id="file_3377cfe00b2d"></a>
FILE_START id=file_3377cfe00b2d path=.specs/features/_arquive_features/oracle_v3/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-30T04:33:59.463898+00:00 sha1=f72117a55a53bae3739d4583cb6cbacf74930ae5
CONTENT_OMITTED toc_only=true
FILE_END id=file_3377cfe00b2d

---
<a id="file_96f9097dbbd2"></a>
FILE_START id=file_96f9097dbbd2 path=.specs/features/_arquive_features/oracle_v3/spec.md domain=docs lang=markdown lines=46 bytes=3205 mtime=2026-04-30T00:13:47.066525+00:00 sha1=02ac4a47ace8e296ed23593ec6d3954c6277a071
CONTENT_OMITTED toc_only=true
FILE_END id=file_96f9097dbbd2

---
<a id="file_96a2bcfd8479"></a>
FILE_START id=file_96a2bcfd8479 path=.specs/features/_arquive_features/qa_subagent/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-26T20:26:18.109414+00:00 sha1=0ad50dd6b8c1506fc32bc6c97cad870207d47765
CONTENT_OMITTED toc_only=true
FILE_END id=file_96a2bcfd8479

---
<a id="file_07e43f982f2d"></a>
FILE_START id=file_07e43f982f2d path=.specs/features/_arquive_features/qa_subagent/spec.md domain=docs lang=markdown lines=22 bytes=1169 mtime=2026-04-26T18:27:10.870230+00:00 sha1=7474b521b7b686ed11fae0943c58b8f07110f069
CONTENT_OMITTED toc_only=true
FILE_END id=file_07e43f982f2d

---
<a id="file_2bad8249610a"></a>
FILE_START id=file_2bad8249610a path=.specs/features/_arquive_features/sam_chronology_fix/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-26T18:20:04.784593+00:00 sha1=6a534b07b054bbbcc966dade113b0a3c87ab3b8f
CONTENT_OMITTED toc_only=true
FILE_END id=file_2bad8249610a

---
<a id="file_a969b2604ea8"></a>
FILE_START id=file_a969b2604ea8 path=.specs/features/_arquive_features/sam_chronology_fix/spec.md domain=docs lang=markdown lines=51 bytes=2550 mtime=2026-04-26T18:19:47.789302+00:00 sha1=8468ef12308baca668fabdfc41aca8206ad13f70
CONTENT_OMITTED toc_only=true
FILE_END id=file_a969b2604ea8

---
<a id="file_a47ad3f11faa"></a>
FILE_START id=file_a47ad3f11faa path=.specs/features/_arquive_features/synapse_workflow/STATE.md domain=docs lang=markdown lines=13 bytes=378 mtime=2026-04-26T04:39:21.446038+00:00 sha1=bb9cde9c3c43964ea1c8017a0117423a079aab4c
CONTENT_OMITTED toc_only=true
FILE_END id=file_a47ad3f11faa

---
<a id="file_08d15183b50c"></a>
FILE_START id=file_08d15183b50c path=.specs/features/_arquive_features/synapse_workflow/spec.md domain=docs lang=markdown lines=38 bytes=1890 mtime=2026-04-24T18:07:53.542998+00:00 sha1=bc5ea2e2ad98d39f870c7512a4cc4ae416741041
CONTENT_OMITTED toc_only=true
FILE_END id=file_08d15183b50c

---
<a id="file_26b5471905f2"></a>
FILE_START id=file_26b5471905f2 path=.specs/features/_arquive_features/wiki_level2/STATE.md domain=docs lang=markdown lines=5 bytes=79 mtime=2026-04-24T01:03:39.917219+00:00 sha1=cc017238b0e6ff18156502ec8d318a50c984646d
CONTENT_OMITTED toc_only=true
FILE_END id=file_26b5471905f2

---
<a id="file_25a85d147e2a"></a>
FILE_START id=file_25a85d147e2a path=.specs/features/_arquive_features/wiki_level2/spec.md domain=docs lang=markdown lines=43 bytes=1834 mtime=2026-04-22T23:11:15.675831+00:00 sha1=71be78a7b5b40a5dd98bb2d0f899312d14766a6d
CONTENT_OMITTED toc_only=true
FILE_END id=file_25a85d147e2a

---
<a id="file_df9a30cacfaa"></a>
FILE_START id=file_df9a30cacfaa path=.specs/features/_arquive_features/wiki_level2/tasks.md domain=docs lang=markdown lines=55 bytes=2460 mtime=2026-04-22T23:32:40.379948+00:00 sha1=161c580635c9ecd7ba0d68aa9fab0db1d788b1af
CONTENT_OMITTED toc_only=true
FILE_END id=file_df9a30cacfaa

---
<a id="file_1a22b8bd3423"></a>
FILE_START id=file_1a22b8bd3423 path=.specs/features/_template_operacional/STATE.md domain=docs lang=markdown lines=22 bytes=587 mtime=2026-04-30T16:46:37.439099+00:00 sha1=29500753c8dd6de693e724c5cb7b66cd666359d0
CONTENT_OMITTED toc_only=true
FILE_END id=file_1a22b8bd3423

---
<a id="file_c26edabf0ec4"></a>
FILE_START id=file_c26edabf0ec4 path=.specs/features/_template_operacional/design.md domain=docs lang=markdown lines=13 bytes=268 mtime=2026-04-30T16:43:01.443053+00:00 sha1=757fdbf8cd47b545f182a0abf5b37e39969c1f30
CONTENT_OMITTED toc_only=true
FILE_END id=file_c26edabf0ec4

---
<a id="file_b3ffa4b3b701"></a>
FILE_START id=file_b3ffa4b3b701 path=.specs/features/_template_operacional/spec.md domain=docs lang=markdown lines=27 bytes=740 mtime=2026-05-01T00:14:35.831268+00:00 sha1=7c76b40388e21d17becf2fbc1c762fcda054fa6a
CONTENT_OMITTED toc_only=true
FILE_END id=file_b3ffa4b3b701

---
<a id="file_7cde61057f28"></a>
FILE_START id=file_7cde61057f28 path=.specs/features/_template_operacional/tasks.md domain=docs lang=markdown lines=13 bytes=361 mtime=2026-04-30T16:43:07.984885+00:00 sha1=68f88914d970b2461ea50e1cea3c677bcbc462e3
CONTENT_OMITTED toc_only=true
FILE_END id=file_7cde61057f28

---
<a id="file_df91d6111d17"></a>
FILE_START id=file_df91d6111d17 path=.specs/features/_template_operacional_sprint/CHECKLIST.md domain=docs lang=markdown lines=36 bytes=1263 mtime=2026-05-01T00:48:01.126371+00:00 sha1=d36d7bd338af53b67530c2039e43f08f10056984
CONTENT_OMITTED toc_only=true
FILE_END id=file_df91d6111d17

---
<a id="file_dea2c04e539b"></a>
FILE_START id=file_dea2c04e539b path=.specs/features/_template_operacional_sprint/STATE.md domain=docs lang=markdown lines=39 bytes=759 mtime=2026-05-01T00:15:03.531344+00:00 sha1=f07e02dcdff8057056c9f8429aaa394c4268e709
CONTENT_OMITTED toc_only=true
FILE_END id=file_dea2c04e539b

---
<a id="file_e8d353f63af3"></a>
FILE_START id=file_e8d353f63af3 path=.specs/features/_template_operacional_sprint/design.md domain=docs lang=markdown lines=14 bytes=217 mtime=2026-05-01T00:15:23.052977+00:00 sha1=7e45caa834e18925a08b6b30210051be577ddf0b
CONTENT_OMITTED toc_only=true
FILE_END id=file_e8d353f63af3

---
<a id="file_6c7ec05b2f9e"></a>
FILE_START id=file_6c7ec05b2f9e path=.specs/features/_template_operacional_sprint/spec.md domain=docs lang=markdown lines=44 bytes=1136 mtime=2026-05-01T00:14:50.952844+00:00 sha1=257cb5f264589b348ea67d4669db37d71866919d
CONTENT_OMITTED toc_only=true
FILE_END id=file_6c7ec05b2f9e

---
<a id="file_f623b71a536c"></a>
FILE_START id=file_f623b71a536c path=.specs/features/_template_operacional_sprint/tasks.md domain=docs lang=markdown lines=17 bytes=504 mtime=2026-05-01T00:15:14.384020+00:00 sha1=9c1094e39b643e8b08f4e048038502dd0bed6bab
CONTENT_OMITTED toc_only=true
FILE_END id=file_f623b71a536c

---
<a id="file_c6539441c702"></a>
FILE_START id=file_c6539441c702 path=.specs/features/contract_sprints_v2_safe/STATE.md domain=docs lang=markdown lines=71 bytes=1747 mtime=2026-04-30T21:57:56.298068+00:00 sha1=3bdcbf4d866633bf8ea154e3f4a604b1d8b4d973
CONTENT_OMITTED toc_only=true
FILE_END id=file_c6539441c702

---
<a id="file_f26b9f244534"></a>
FILE_START id=file_f26b9f244534 path=.specs/features/contract_sprints_v2_safe/spec.md domain=docs lang=markdown lines=53 bytes=2924 mtime=2026-04-30T21:56:40.332350+00:00 sha1=6181df8f9bf6e547f14de144d58d7e35484c7ab8
CONTENT_OMITTED toc_only=true
FILE_END id=file_f26b9f244534

---
<a id="file_4f8d9b00b4a4"></a>
FILE_START id=file_4f8d9b00b4a4 path=.specs/features/contract_sprints_v2_safe/tasks.md domain=docs lang=markdown lines=38 bytes=1984 mtime=2026-04-30T21:56:59.898711+00:00 sha1=29ee1fadffa2a76afa592781631ffcde707d7af6
CONTENT_OMITTED toc_only=true
FILE_END id=file_4f8d9b00b4a4

---
<a id="file_c1d55217ac2a"></a>
FILE_START id=file_c1d55217ac2a path=.specs/features/governance_rules_hardening/STATE.md domain=docs lang=markdown lines=35 bytes=1713 mtime=2026-05-01T03:55:07.386875+00:00 sha1=dace4851d4f3fc90a6c18fefd9c98c0936ffddf9
CONTENT_OMITTED toc_only=true
FILE_END id=file_c1d55217ac2a

---
<a id="file_99c81edef6ff"></a>
FILE_START id=file_99c81edef6ff path=.specs/features/governance_rules_hardening/design.md domain=docs lang=markdown lines=13 bytes=268 mtime=2026-04-30T16:43:01.443053+00:00 sha1=757fdbf8cd47b545f182a0abf5b37e39969c1f30
CONTENT_OMITTED toc_only=true
FILE_END id=file_99c81edef6ff

---
<a id="file_58b215a340da"></a>
FILE_START id=file_58b215a340da path=.specs/features/governance_rules_hardening/spec.md domain=docs lang=markdown lines=149 bytes=6085 mtime=2026-05-01T03:00:10.790352+00:00 sha1=47b62ce4c991aa8d8cbd2932ebea9510402059d0
CONTENT_OMITTED toc_only=true
FILE_END id=file_58b215a340da

---
<a id="file_4f9bb146f536"></a>
FILE_START id=file_4f9bb146f536 path=.specs/features/governance_rules_hardening/tasks.md domain=docs lang=markdown lines=42 bytes=2324 mtime=2026-05-01T02:59:57.318603+00:00 sha1=6233cec933839e53214f90017aeefeddba9c2ba3
CONTENT_OMITTED toc_only=true
FILE_END id=file_4f9bb146f536

---
<a id="file_95dabcdf3543"></a>
FILE_START id=file_95dabcdf3543 path=GUIA_ESTABILIZACAO_NOTEBOOKLM.md domain=docs lang=markdown lines=56 bytes=2342 mtime=2026-04-16T01:24:16.342106+00:00 sha1=42fda535b309349df1a8c83c959f0cc2e534875a
CONTENT_OMITTED toc_only=true
FILE_END id=file_95dabcdf3543

---
<a id="file_8ec9a00bfd09"></a>
FILE_START id=file_8ec9a00bfd09 path=README.md domain=docs lang=markdown lines=97 bytes=4687 mtime=2026-04-23T16:12:13.144613+00:00 sha1=23e3abb6e9ba9b868808626442bbec6112a64a74
CONTENT_OMITTED toc_only=true
FILE_END id=file_8ec9a00bfd09

---
<a id="file_4efb6293109d"></a>
FILE_START id=file_4efb6293109d path=README_CONTEXT.md domain=docs lang=markdown lines=124 bytes=6151 mtime=2026-04-26T19:23:46.993611+00:00 sha1=12c4ecdab7d37bd1ede6d808fc3b826c8dbdb3e5
CONTENT_OMITTED toc_only=true
FILE_END id=file_4efb6293109d

---
<a id="file_19e76e009f38"></a>
FILE_START id=file_19e76e009f38 path=TEMPLATE_MIGRATION.md domain=docs lang=markdown lines=59 bytes=1930 mtime=2026-04-15T13:55:12.936320+00:00 sha1=a3590439f4c18d976ff928504760f8f35a29d25c
CONTENT_OMITTED toc_only=true
FILE_END id=file_19e76e009f38

---
<a id="file_f6f7100f063b"></a>
FILE_START id=file_f6f7100f063b path=VERSION.md domain=docs lang=markdown lines=11 bytes=673 mtime=2026-04-26T20:25:19.735804+00:00 sha1=c262bc32870ead58b83fddaf73a89b7eb4d532be
CONTENT_OMITTED toc_only=true
FILE_END id=file_f6f7100f063b

---
<a id="file_1f98938d3cd9"></a>
FILE_START id=file_1f98938d3cd9 path=_modoLight/Modo_Light.md domain=docs lang=markdown lines=140 bytes=5961 mtime=2026-04-11T03:09:45.201801+00:00 sha1=267fea8bb9a67840095155f98e5860cd0cf82760
CONTENT_OMITTED toc_only=true
FILE_END id=file_1f98938d3cd9

---
<a id="file_c59135753d26"></a>
FILE_START id=file_c59135753d26 path=init_ai_project.sh domain=source lang=bash lines=129 bytes=4545 mtime=2026-04-26T20:03:25.730753+00:00 sha1=787c754dec5d442f485c2a35346827d8f358ec96
CONTENT_OMITTED toc_only=true
FILE_END id=file_c59135753d26

---
<a id="file_7030d0b2f71b"></a>
FILE_START id=file_7030d0b2f71b path=package.json domain=config lang=json lines=41 bytes=1670 mtime=2026-04-26T20:03:15.234425+00:00 sha1=175eb33cadfea1e970819bda42dfe283708089c3
CONTENT_OMITTED toc_only=true
FILE_END id=file_7030d0b2f71b

---
<a id="file_350a79f8b829"></a>
FILE_START id=file_350a79f8b829 path=run_context.py domain=source lang=python lines=150 bytes=5694 mtime=2026-04-26T20:02:40.996990+00:00 sha1=8df94515229ce3edbceae07a28d15cad4a96f496
CONTENT_OMITTED toc_only=true
FILE_END id=file_350a79f8b829

---
<a id="file_86bac54f32d7"></a>
FILE_START id=file_86bac54f32d7 path=run_context.sh domain=source lang=bash lines=17 bytes=798 mtime=2026-04-17T02:31:37.204327+00:00 sha1=a6c29d302d9d9c3f99917dd1da64da3d07f635ac
CONTENT_OMITTED toc_only=true
FILE_END id=file_86bac54f32d7

---
<a id="file_4c6bbd05056e"></a>
FILE_START id=file_4c6bbd05056e path=tests/test_context.py domain=source lang=python lines=135 bytes=6249 mtime=2026-04-17T00:13:58.569614+00:00 sha1=9d17651da9da5326350654941d201d72c37c42c4
CONTENT_OMITTED toc_only=true
FILE_END id=file_4c6bbd05056e

---
<a id="file_357f74cc7014"></a>
FILE_START id=file_357f74cc7014 path=tests/test_oracle.py domain=source lang=python lines=166 bytes=7913 mtime=2026-04-29T23:22:58.196941+00:00 sha1=4458c77a484e4bf9ff9a7fc04ab6f1e46f9cb385
CONTENT_OMITTED toc_only=true
FILE_END id=file_357f74cc7014
