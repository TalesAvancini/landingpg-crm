# 🕸️ Ideia: Matriz de Afinidade & Grafo de Dependência (Blast Radius)

**Data da Ideia:** 2026-05-04
**Origem:** Sessão de Hardening do MiMo (Reflexão sobre as propagações do `spec-driver`)

## 📌 O Problema
Atualmente, se um arquivo vital do framework é alterado (ex: `spec-driver.md`), nós dependemos da memória humana ou de anotações estáticas manuais no topo do arquivo para lembrar de atualizar os arquivos correlacionados (como `RULES.md`, `MASTER_FLOW.md`). Precisamos de uma forma automatizada de "perceber as propagações" e o grau de correlação entre eles.

## 💡 A Visão (Níveis de Maturidade)

### Nível 2: Grafo Semi-Automático (Via Python)
Um script utilitário (`context:affinity` ou `context:coupling`) que:
1. Varre os arquivos `.md` (como o `.context` e `.agent`).
2. Identifica menções estruturais e links entre eles.
3. "Cospe um arquivo" (como o `rx-communications.md`) com um diagrama Mermaid ou matriz gerada no ato, mostrando quem está acoplado com quem.

### Nível 3: Grafo de Dependência de Metadados (O Santo Graal)
Uso de "Coupling Tags" no frontmatter dos arquivos `.md`. 
Exemplo: o arquivo A avisa na cabeça dele que é atrelado ao arquivo B.
O nosso validador SAM (Husky) ou o `validate_context.py` leria essas tags. Se você tentar commitar uma alteração no Arquivo A, o Husky checa e diz: *"A Matriz diz que A afeta B. Você não tocou em B. Block!"*

---

## 🛠️ Insight de Implementação
> **Dica de Ouro:** A skill `tlc-spec-driven` possui dentro dela uma **"skill de coupling"** (análise e mapeamento de correlações) que pode e DEVE ser usada como fundação e inspiração para montar esse sistema no H.O.K Forge.
