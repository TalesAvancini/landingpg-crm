---
Criado em: 2026-04-10 20:50
Ultima Atualizacao: 2026-05-22 14:56
Status: Ativo
---

# 📊 Health Check do Contexto - Dashboard

💡 *Insight Humano: Este dashboard permite saber rapidamente se a IA pode operar com precisão ou se o contexto está "poluído" ou "desatualizado".*

<!-- HEALTH_TABLE_START -->
| Metrica | Valor Atual | Limite Ideal | Pilar | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Manutencao** | | | | |
| Linhas do Journal | 213 | 600 | Tracker | [OK] |
| Carga do Journal | 13k chars | 50k chars | Tracker | [OK] |
| **Cognitivo** | | | | |
| Estimativa Tokens | ~305k | 128k (Max) | Eficiencia | [WARN] Context Bloat |
| **Consistencia** | | | | |
| Tabelas no Schema | 1 | N/A | DB-First | [OK] |
| Migrations Pendentes | 1 file(s) | N/A | DB-First | [OK] |
| Ultimo Harness | Role Check | Pass/Fail | Integridade | N/A |
| Ultima Sincronia | 2026-05-22 14:56 | Real-Time | Automacao | [OK] |
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
