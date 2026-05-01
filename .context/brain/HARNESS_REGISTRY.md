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
| `H05` | Friction | Governança | `validate_context.py` | Execução Contínua | Journal Chronology & State Freshness | Log `[GOVERNANCE-FRICTION]` |

## ⚙️ Regras de Execução
- ✅ `harness_runner.py` deve rodar antes de qualquer merge ou geração de código produtivo.
- ⚠️ Falha consecutiva >2x → pausa automática + log em `JOURNAL.md` com tag `[harness:fail]`.
- 🔒 Nunca sobrescrever `.context/` sem passar por validação de contrato.
