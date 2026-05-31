# Plano de Flexibilização da Governança H.O.K. (Modo Light) & Novos Harnesses

Este plano descreve o design e a implantação de mudanças no ecossistema de governança local do projeto. O objetivo é reduzir o engessamento mecânico de validações para tarefas de desenvolvimento cotidiano (branches de feature) enquanto implementamos barreiras de segurança ("Harnesses") inteligentes baseadas nas decisões da ata de brainstorm.

---

## 🎯 Escopo de Implantação

Com base no alinhamento estratégico registrado em `planos/Brainstorm_modoLight.md`, implantaremos os seguintes harness e facilidades de governança:

1. **Tolerância SAM em Branches de Feature** (Modo `WARNING` dinâmico).
2. **Harness de Variáveis de Ambiente** (`Env Drift Gate`).
3. **Harness de Exaustão de Loops de Teste** (`Loop Exhaustion Harness`).
4. **Harness de Complexidade Cognitiva & Cobertura Semântica** (Avisos educativos no `pre-commit`).

---

## 🏗️ Proposta de Mudanças

### 1. Sistema Anti-Migué (SAM) Dinâmico
*   **Arquivo**: `.context/_scripts/workflow_journal_auditor.py`
*   **Ação**: Detectar se a branch git ativa não é estável (ex: `main` ou `develop`). Caso seja uma branch secundária (`feature/*`, `bugfix/*`), mudar a execução para modo `WARNING`. Em vez de dar Exit 1 no commit, gerar um relatório visual das inconsistências no terminal para alertar o desenvolvedor.

### 2. Scanner de Variáveis de Ambiente (Env Drift Gate)
*   **Novo Arquivo**: `.context/_scripts/env_drift_gate.py`
*   **Ação**: Escanear código em busca de `process.env.VAR_NAME` e cruzar com as declarações presentes em `.env.example`. Bloquear commits caso novas variáveis não estejam documentadas no template.

### 3. Detector de Loop de Testes (Loop Exhaustion)
*   **Novo Arquivo**: `.context/_scripts/loop_exhaustion_harness.py`
*   **Ação**: Registrar execuções sucessivas falhas sob `scratch/loop_state.json`. Se uma IA rodar testes consecutivos por 5 vezes e falhar todas as vezes sem modificar o diff do git, bloquear a execução subsequente e disparar escalação obrigatória (Bandeira Branca).

### 4. Gate de Complexidade e Cobertura (Complexity & Semantic Check)
*   **Novo Arquivo**: `.context/_scripts/complexity_coverage_gate.py`
*   **Ação**: Dar avisos didáticos caso um arquivo JS passe de 250 linhas ou caso novas funções públicas declaradas não tenham strings correspondentes escritas no arquivo `.test.js` associado.

---

## 🚥 Plano de Ação & Sincronização

A implantação ocorrerá de forma cirúrgica e atômica, utilizando as diretrizes de `plan-writing` para manter a esteira sempre testada.

*   [ ] **Fase 1: SAM Dinâmico**
    *   Modificar `.context/_scripts/workflow_journal_auditor.py` com detecção de branch.
    *   *Verificação*: Criar feature branch local, alterar diário incorretamente e testar exit-code de commit local (deve ser 0, mostrando warnings).
*   [ ] **Fase 2: Env Drift Gate**
    *   Criar `.context/_scripts/env_drift_gate.py`.
    *   Integrar no `harness_runner.py` e `.husky/pre-commit`.
    *   *Verificação*: Inserir `process.env.TEST_NOT_FOUND` no código e verificar bloqueio físico.
*   [ ] **Fase 3: Loop Exhaustion Harness**
    *   Criar `.context/_scripts/loop_exhaustion_harness.py`.
    *   Implementar reset automático da contagem quando o diff do Git sofrer alteração física.
    *   *Verificação*: Rodar simulação de 5 falhas sucessivas sem alteração e ver bloqueio.
*   [ ] **Fase 4: Complexity & Coverage Gate**
    *   Criar `.context/_scripts/complexity_coverage_gate.py` como `WARNING`.
    *   *Verificação*: Escrever código complexo e validar emissão de aviso instrutivo sem abortar commit.

---

## 📝 Questões em Aberto para Validação

1. **Loop Reset**: Resetamos o contador de loop de testes sempre que o diff do Git for modificado ou apenas sob intervenção do humano? *(Recomendado: Auto-reset no diff, garantindo que o agente está livre para tentar de novo após mexer no código).*
2. **Branches Estritas**: Quais branches devem ser STRICT além de `main` e `master`? *(Recomendado: Apenas main/master para manter branches de QA dinâmicas).*
