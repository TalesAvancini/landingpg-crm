# 📋 Log Cronológico dos Planos

> Ordem de criação de cada arquivo nesta pasta, com contexto de quem gerou e por quê.

---

| # | Arquivo | Criado em | Autor/Motor | Contexto |
|:---|:---|:---|:---|:---|
| 1 | `relatorio_MiMo-v2.5-Pro.md` | 26/Abr 23:48 | MiMo | Primeiro relatório. Sugestões de Harness Telemetria, severity levels e plugin system. Existia antes da sessão de Deep Research. |
| 2 | `relatorio_Qwen.md` | 27/Abr 23:16 | Qwen | Propostas de Harnesses evolutivos: Auto-Remedy, Drift-Guard, Learnings.md, Budget de Tokens. |
| 3 | `relatorio_oracle_MiMo.md` | 27/Abr 23:53 | MiMo | Análise estratégica da arquitetura. Vulnerabilidades do SAM, proposta do Impact-Aware Harness. |
| 4 | `relatorio_Oracle_Qwen.md` | 28/Abr 00:43 | Qwen | Otimização técnica do Oracle: Cache TTL, Alias Expansion, Smart Chunking, Tool-Calling Schema. |
| 5 | `comentarios_Flash.md` | 28/Abr 00:52 | Flash + Usuário | Consolidação de diretrizes: Busca Imparcial (sem multiplicador de role), Gate Epistemológico em Modo Light. Contém restrições operacionais do usuário. |
| 6 | `relatorio_insights_context.md` | 28/Abr 19:50 | Claude Opus | Radiografia quantitativa do `.context/` e `PROJECT_INDEX.md`. Inclui ideia guardada do Impact-Aware Harness (MiMo). |
| 7 | `relatorio_Oracle_Opus.md` | 28/Abr 20:14 | Claude Opus | Análise original do Oracle: `_index.md` desconectado, campo `aliases` ignorado, retorno binário, 1 query real em toda a história. |
| 8 | `plano_consolidado_Oracle_v3.md` | 28/Abr 20:15 | Claude Opus | Síntese de todos os relatórios. Best-of com atribuição, descartes justificados e roadmap de 15 itens. |
| 9 | `relatorio_MiMo-Oracle.md` | 28/Abr 20:52 | MiMo | Dissecação cirúrgica do algoritmo do Oracle: stemming pt-BR, calibração de confidence, filtro de siglas, top-N, `oracle_analytics.py`, fire-and-forget. |
| 10 | `auditoria_MiMo_plano_consolidado.md` | 28/Abr 21:19 | MiMo (Auditor) | Auditoria crítica do plano consolidado: circularidade da Fase 0.1, testes ausentes, estimativas subdimensionadas, critérios de sucesso faltando. |
| 11 | `log_planos.md` | 28/Abr 21:23 | Claude Opus | Este arquivo. Registro cronológico de todos os planos. |
| 12 | `auditoria_Qwen_plano_consolidado.md` | 28/Abr 21:32 | Qwen (Auditor) | Auditoria do plano consolidado: cache in-memory é inútil em CLI (deve ser disco), normalização pré-query, escrita atômica no `_index.md`. |
| 13 | `auditoria_MiMo_final.md` | 28/Abr 21:40 | MiMo (Auditor, 2ª rodada) | Crítica de que o plano não incorporou o feedback das auditorias. Insistência em testes como item 0.0. Nota: 8/10 direção, 6/10 execução. |
| 14 | `plano_consolidado_Oracle_v3.md` *(atualizado)* | 28/Abr 21:42 | Claude Opus | Plano reescrito incorporando TODAS as correções das 3 auditorias. Testes como Fase -1, cache em disco, estimativas corrigidas para 25-30h. |
| 15 | `auditoria_MiMo_v3_final.md` | 28/Abr 21:50 | MiMo (Auditor, 3ª rodada) | Testes baseline vs target — metade dos testes falha no Oracle atual. Nota final: 9/10 direção, 8/10 execução. Veredicto: "Pode executar." |
| 16 | `plano_consolidado_Oracle_v3.md` *(v3 final)* | 28/Abr 21:52 | Claude Opus | Split baseline/target nos testes, critérios de sucesso preenchidos para itens 10-16. Todas as críticas endereçadas. |
| 17 | `auditoria_Qwen_cirurgica.md` | 28/Abr 22:05 | Qwen (filtrado pelo MiMo) | 7 ajustes cirúrgicos: sandbox de testes, suffix dict, schema_version, cache atomic write, whitelist técnica, top-N char limit, parser regex. |
| 18 | `plano_consolidado_Oracle_v3.md` *(v3 final+)* | 28/Abr 22:07 | Claude Opus | 7 ajustes Qwen incorporados como notas nos itens existentes. Plano encerrado. |

---

## Linhagem de Dependências

```
relatorio_MiMo-v2.5-Pro ──┐
relatorio_Qwen ────────────┤
relatorio_oracle_MiMo ─────┼──→ plano_consolidado_Oracle_v3 ──→ auditoria_MiMo ──┐
relatorio_Oracle_Qwen ─────┤                                  auditoria_Qwen ──┤
comentarios_Flash ─────────┤                                  auditoria_MiMo_2 ┤
relatorio_Oracle_Opus ─────┘                                                    │
relatorio_MiMo-Oracle ─────────→ (incorporado no plano v3)                      │
                                                                                ▼
                                                       plano_consolidado_v3 (ATUALIZADO)

relatorio_insights_context ────→ (relatório geral independente, contém ideia guardada do MiMo)
```
