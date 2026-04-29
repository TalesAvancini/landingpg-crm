# 🏗️ Plano de Arquitetura: A Dança Multi-Agent (Hub & Spoke)

Este plano formaliza a arquitetura de orquestração do Antigravity v2.5.2+. Ele consolida a visão de que a **IA Principal (Hub)** atua como Planner/Arquiteto com contexto estratégico pleno, enquanto o **Executor e o Validador (Spokes)** atuam como subagentes isolados, operando sob contratos determinísticos (não apenas prompts).

## 📌 1. Distribuição de Skills e Responsabilidades

### 👑 O Hub (IA Principal / Planner / Arquiteto)
- **Natureza:** Janela de chat principal interativa com o Humano.
- **Contexto:** Amplo (Lê o ROADMAP, INCEPTION, WIKI, etc).
- **Skills Obrigatórias:** 
  - `tlc-spec-driven`: Para desenhar a arquitetura, quebrar épicos em sprints e features.
- **Skills Autorizadas:**
  - `codenavi`: Usado em modo **Exploratório** (Mapeamento Sistêmico).
  - `mermaid-studio`: Usado **On-demand** para visualizações.
- **Entregável:** Escreve a SPEC (`.specs/features/`) incluindo obrigatoriamente o campo YAML `impact_control`.

### 👷 O Spoke Executor (`@spec-driver` / `@autopilot`)
- **Natureza:** Subagente invocado em background/isolado.
- **Contexto:** Estreito (Recebe apenas a SPEC atual, o arquivo alvo e o contrato DoD).
- **Skills OBRIGATÓRIAS:**
  - `codenavi` / `grep_search`: **Pre-flight Gate de Impacto**.
  - `flash-harness`: **Diário de Bordo Estruturado** obrigatório.
- **Limitação Mecânica:** Nenhuma permissão de escrita em `brain/` ou `market/`.

### 🕵️ O Spoke Validador (`@qa-validator`)
- **Natureza:** Subagente isolado.
- **Responsabilidade:** Validação Puramente **Semântica** (Lógica de negócio, cobertura de DoD, intenção arquitetural).
- **Integração:** Não assina `qa_signoff: true` se o script SAM/Harness falhar na validação estrutural. (Lógica de `AND`).

## 📌 2. Contratos Determinísticos (A Blindagem)

### A. Campo Obrigatório na SPEC (YAML)
O Planner deve incluir no frontmatter da SPEC (`.specs/_template.md`):
```yaml
impact_control:
  max_impact_radius: 3
  pre_flight_grep_terms: ["schema.sql", "api/routes"]
```

### B. Pre-flight Log Estruturado (Parseável)
O Executor não usa texto livre. Ele deve registrar obrigatoriamente no `STATE.md`:
```markdown
## 📝 Pre-Flight Log
- grep_terms: ["user_id"]
- files_scanned: 142
- cross_layer_refs: 2
- circuit_breaker: SAFE (2 <= 3)

## 📝 Execution Log
- [STEP 1] Modificado src/api/users.py
- [STEP 2] Linter: PASS
```

### C. Circuit Breaker & Status SCOPE_BLOWOUT
Se o número de arquivos detectados via grep for > `max_impact_radius`, o Executor NÃO escreve código. Ele altera o `STATE.md` para:
`Status: ⚠️ SCOPE_BLOWOUT`
**Reporte de Telemetria (Obrigatório):** O Executor deve listar no `STATE.md` exatamente quais arquivos e referências cruzadas excederam o limite.
O Hub lê este status e os dados de telemetria para realizar a **Re-fragmentação** da SPEC com base na realidade física do código, e não em suposições. O `harness_runner.py` garantirá que o diff não ultrapasse esse raio.

## 🎯 Verification Plan
- O validador da próxima tarefa exigirá evidência de que os templates de SPEC e o script `harness_runner.py` foram modificados para forçar o limite atômico `max_impact_radius`.
