# Spec: affinity-lite

## 🎯 Objetivo
Detectar acoplamentos invisíveis através da análise de co-ocorrência no Git (Eixo Temporal) e menções cruzadas (Eixo Referencial), classificando-os em tipos de "Drift".

## 📋 Requisitos Funcionais
1. **Eixo Temporal:**
   - Coletar histórico de commits (`git log`).
   - Calcular índice de Jaccard por par de arquivos.
   - Threshold padrão: `0.3`.
   - Ignorar arquivos com menos de 3 commits (`min_commits`).

2. **Eixo Referencial:**
   - Buscar menções ao nome do arquivo (stem) em outros arquivos.
   - Usar Regex com Word Boundary (`\b`).
   - Score logarítmico baseado no número de menções.

3. **Detecção de Drift:**
   - **Acoplamento Fantasma:** Temporal > 0.3 AND Referencial < 0.1.
   - **Referência Morta:** Referencial > 0.3 AND Temporal < 0.05.
   - **Saudável:** Ambos > 0.2.

## ⚙️ Restrições Técnicas (Constraints)
- **Stdlib Puro:** Proibido usar bibliotecas externas (scikit-learn, numpy).
- **Performance:** Uma única chamada ao Git log para todo o processo.
- **Output:** Salvar em `.context/maintenance/rx-affinity-lite.md` e `.json`.
- **Regra 3.1:** Proibido output em tabelas NxN no Markdown; usar listas de adjacência.

## 🛠️ Contrato de I/O
- **Lê:** `.git/`, `.context/maintenance/rx-communications.md`, arquivos `.md` e `.py`.
- **Escreve:** `.context/maintenance/rx-affinity-lite.md`, `.context/maintenance/rx-affinity-lite.json`.
