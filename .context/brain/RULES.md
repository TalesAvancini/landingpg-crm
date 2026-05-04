---
Criado em: 2026-04-10 20:50
Última Atualização: 2026-05-03 22:50
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

## 🔄 1.4 Protocolo Contract Sprints (v2-Safe)
Padrão obrigatório para features de alta complexidade ou segurança crítica.
1. **Modo Dual:** O Harness detecta `contract_mode: sprint_based` para ativar a fiscalização polimórfica.
2. **Enforcement HG04 (Ordem de Sprint):** Bloqueio absoluto de avanço se qualquer sprint anterior estiver sem `qa_signoff: true`.
3. **Imunidade de Cleanup (E1):** Sprints ativas com signoff pendente são imunes ao arquivamento automático do `cleanup_specs.py`.
4. **Impacto Incremental (D1/D2):** Churn (linhas +/-) capturado automaticamente pelo Harness e persistido no `STATE.md` para auditoria passiva.
5. **Bloqueio C2 (Global Signoff):** Proibido dar signoff global na feature se houver qualquer pendência nas sprints internas.

## 🛡️ 1.5 Regra `CLOSE_WAVE` (Rigor de Fechamento)
Uma onda/sprint só pode ser declarada **concluída** se **todas** as condições forem verdadeiras:
1. **Harness PASS:** Pipeline de validação sem erros.
2. **Coerência:** Artefatos (`spec.md`, `STATE.md`, `tasks.md`) em sincronia total.
3. **Higiene:** `git status --short` sem saída (árvore 100% limpa).
4. **Signoff:** `qa_signoff: true` registrado no bloco da sprint/onda.

**Falha em qualquer critério:**
- O status **deve** permanecer `🚧 IN_PROGRESS`.
- É proibido declarar conclusão ou mover para `PASSED`.
- Emissão obrigatória de evento `[GOVERNANCE-FRICTION]`.

## 🛡️ 1.6 Regra `ANTI_FALSE_PASS` (Integridade Narrativa)
É proibido forçar estados narrativos de conclusão sem evidência técnica objetiva.
1. **Claims Reais:** Afirmações como "100% concluído" ou "baseline limpa" devem ser verificáveis via Git/Harness.
2. **Fraude Narrativa:** Declarar conclusão no `JOURNAL.md` enquanto o `qa_signoff` é `false` é classificado como fraude crítica.
3. **Exemplos Binários:**
   - **PASS:** Árvore limpa + Signoff OK + Harness OK ⮕ Conclusão Autorizada.
   - **FAIL:** "Tudo pronto" no Journal + 2 arquivos untracked ⮕ **BLOQUEIO** (Fraude Detectada).
   - **FAIL:** "Sprint finalizada" + `qa_signoff: false` ⮕ **BLOQUEIO** (Inconsistência).

## 🛡️ 1.7 Regra `MIMO_STATE_INTEGRITY` (Integridade de Estado)
Toda automação que altere o `STATE.md` deve garantir:
1. **Preservação:** Não deletar campos obrigatórios (`start_hash`, `qa_signoff`, `status`, etc).
2. **Edição Cirúrgica:** Alterar apenas o bloco de metadados ou logs específicos.
3. **Fail-Closed:** Se a escrita falhar ou corromper a estrutura YAML, o arquivo deve ser restaurado ao estado anterior.

## 🛡️ 1.8 Regra `CRITICAL_SCRIPT_SANITY` (Sanidade de Scripts)
Mudanças em scripts de governança (`validate_context.py`, `harness_runner.py`, etc) exigem:
1. **Sanity Check:** Execução mínima do script após a alteração para validar que não há erros de import ou sintaxe.
2. **Non-Regression:** Evidência de que os gates de segurança continuam ativos.

## 🛡️ 1.9 Regra `EXECUTION_GATEKEEPER` (Fail-Closed & Resume Protocol)
A modificação de arquivos de código é um ato estritamente mecânico, governado fisicamente pelo `write_with_validation.py` (A Trava Física - Skill 6).
1. **Bloqueio Inviolável:** Nenhuma ferramenta genérica de escrita deve contornar a validação formal deste script.
2. **Condição de Bloqueio:** O script analisa dinamicamente o `STATE.md` buscando por estados de erro ativo (`[BLOCKED]` ou `[FATAL]`).
3. **Protocolo `[RESUME]`:** Se o sistema estiver bloqueado, qualquer tentativa de escrita resultará em falha e aborto da operação. Para destravar a arquitetura e retomar a execução, a IA deve receber novas diretrizes do Orquestrador Humano e registrar obrigatoriamente a string `RESUME_DIRECTIVE:` dentro da seção de log do `STATE.md`.

## 🛡️ 1.10 Regra `MIMO_MANDATORY_INJECTION` (Memória Ativa)
O Agente orquestrador sofre de amnésia cibernética entre sessões. Para evitar o "Ralph Wiggum Loop":
1. **Injeção Obrigatória:** Nenhuma spec pode ter sua execução iniciada sem que o comando `npm run context:inject` seja executado previamente.
2. **Consumo da Vacina:** O Agente Executor **NÃO DEVE** ler a spec original virgem (`spec.md`). Ele **DEVE OBRIGATORIAMENTE** ler a versão `*.enriched.md`, que contém as *Scars* (Cicatrizes) injetadas no topo.
3. **Fraude Comportamental:** Ignorar as *Scars* do topo da spec e cometer o mesmo erro reportado é considerado quebra de conduta, passível de bloqueio de commit.

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
