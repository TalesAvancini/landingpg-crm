---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-04-24 13:51
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
3. **[ ] Role Layer:** Conforme definido em `brain/AGENT_REGISTRY.md` + prompts físicos em `.agent/subagents/`.
4. **[ ] Ephemeral Layer:** `brain/PRD.md` ativo + `maintenance/schema.sql` + últimas 30-50 linhas do `maintenance/JOURNAL.md`
5. **[ ] Navigation Layer:** `monitoring/PROJECT_INDEX.md` (Consultar obrigatoriamente antes de criar novos arquivos)

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

## 🛡️ 1.3 Pre-flight Gate & Impact Radius (Anti-SCOPE_BLOWOUT)
1. **Mapeamento Obrigatório:** Antes de modificar interfaces, schemas ou contratos cross-layer, o Executor DEVE rodar `grep` nos termos impactados.
2. **Circuit Breaker:** Se o impacto real (número de arquivos afetados) > `max_impact_radius` (definido na SPEC), o Executor deve:
   - Alterar status para `⚠️ SCOPE_BLOWOUT` no `STATE.md`.
   - Listar a telemetria (arquivos/referências) e abortar.
3. **Feedback Loop:** O Hub (Planner) deve utilizar a telemetria do `SCOPE_BLOWOUT` para re-fragmentar a SPEC em unidades menores e atômicas.
4. **Log Estruturado:** O resultado do Pre-flight deve ser registrado de forma parseável no `STATE.md` para auditoria do QA e do Harness.

---

## 🔢 2. Ansiedade de Contexto & Ralph Wiggum Loop
Para combater o *Context Anxiety* e alucinações por inchaço:
- **Ralph Wiggum Loop:** O foco é absoluto e efêmero. Apenas resolver a Spec atômica atual no `The Workshop` (`.specs/`), persistir os descobrimentos difíceis no `JOURNAL.md`, e encerrar a sessão. A cada ciclo, a memória sintética zera e o sistema de arquivos assume como memória indestrutível.
- **Gatilhos de Alerta:** ~50.000 caracteres ou 15 trocas densas. Se atingido, purgue o Journal ou inicie chat limpo.

---

## 🧠 3. Protocolo de Manutenção do Contexto
A IA atua como bibliotecário chefe. Consistência entre Código e Contexto é obrigatória.
- **`journal_mode: strict`**: Commits são bloqueados se a matriz `JOURNAL_SYNAPSE.md` não for cumprida (Git Diff vs Journal).
- **`maintenance/JOURNAL.md`**: Apenas decisões de arquitetura, resoluções de bugs complexos e mudanças de lógica. Proibido logar erros triviais. Ao atingir ~600 linhas ou 50k chars → acionar `_scripts/purge_journal.py`.
- **`maintenance/HARNESS_LOG.md`**: Log técnico automático do Harness (`[HARNESS-PASS]`/`[HARNESS-FAIL]`). Proibido gravar esses eventos no `JOURNAL.md`.
- **`maintenance/TECHNICAL_REQUIREMENTS.md`**: Atualizar sempre que houver mudança em `package.json`, alteração de Schema ou integração de novas APIs.
- **`maintenance/rebuild_guide.md`**: Atualizar com hacks de ambiente local, CI/CD ou passos manuais de deploy.
- **`.specs/` (Workshop Efêmero):** Specs são rascunhos de execução. Pós-merge ou >48h inativo → arquivar em `_archive_context/specs/`. Decisões técnicas devem migrar para o `JOURNAL.md` antes da limpeza.

---

## 🗄️ 4. Protocolo Database & Architecture First (Anti-Alucinação)
É proibido construir código baseado em suposições sobre a estrutura do Banco de Dados ou Arquitetura.
1. **Verificação de Dados Obrigatória:** Antes de criar UI/lógica dependente de dados, validar `maintenance/schema.sql`.
2. **Aviso de Divergência:** Se o código exigir um campo inexistente, parar e avisar: *"⚠️ Alerta: O Frontend exige o campo X, mas ele não existe no Schema. Sugiro gerar a migration antes de prosseguir."*
3. **Prevenção de Duplicidade:** Antes de criar *qualquer* arquivo, componente (ex: botão, modal) ou utilitário novo, a IA DEVE inspecionar `monitoring/PROJECT_INDEX.md`. Se a responsabilidade já existir, reescreva ou estenda o código existente. NUNCA crie duplicatas funcionais.

---

## 🤖 5. Comportamento do Agente (Transparência & Roteamento)
- **Ativação:** Toda tarefa complexa inicia com: `🤖 Ativando @[role] | Escopo: [descrição]`
- **Isolamento:** Carregar APENAS `Global + Role-Specific + Task-Ephemeral`. Ignorar o resto.
- **Handoff:** Cruzar 2+ domínios? Pausar → registrar no `JOURNAL.md`:  
  `🔄 Handoff: @[role-atual] → @[role-próxima] | Estado: [resumo técnico] | Próximo: [ação]`
- **Context Gate (Pré-Código):** Validar antes de gerar:  
  `[ ] PRD ativo` | `[ ] schema contém estruturas` | `[ ] JOURNAL < 550 linhas` | `[ ] zero secrets hardcoded`
- **Sistema Anti-Migué (SAM):** Toda entrada no Journal deve seguir o template de narrativa + checklist de propagação + contrato de validação com IDs segregados.

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

---

> **Nota Final para a IA:** Você é a extensão cognitiva do desenvolvedor. Sem contexto atualizado e blindado, sua capacidade de longo prazo é nula. Seu compromisso é com a verdade documentada.
