# Handoff: Blast Radius Inteligente (Lean MVP)

Este documento serve como passagem de bastão para o próximo agente iniciar a execução do plano consolidado sem precisar de histórico de chat anterior.

## 🎯 Contexto e Objetivo
Implementar o motor de blast radius híbrido (`blast_radius.py`) que otimiza o passo 2 do `journal-sync`. Ele cruza o grafo de dependências do Graphify (`graphify-out/graph.json`) com as regras de governança declaradas no `rx-communications.md`.

## 📍 Estado Atual
* **Planejamento Concluído e Consolidado:** O plano final de implementação detalhado e revisado está localizado em [PLANO_FINAL_blast_radius.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md).
* **Fase:** Pronto para **Execução** (nenhum código foi implementado ainda para garantir a castidade do escopo).

## 🛠️ Instruções para o Próximo Agente
1. Abra o arquivo [PLANO_FINAL_blast_radius.md](file:///c:/Users/User/Desktop/ProjetosAntigravity/TEMPLATES/template_inic%C3%ADo_de_projeto/planos/mudanca_propagacao/PLANO_FINAL_blast_radius.md) e leia-o na íntegra.
2. Siga rigorosamente a ordem de execução do checklist de 10 passos detalhados na seção **"Cronograma de Execução"** do plano.
3. Não expanda o escopo além do Lean MVP (não implementar `--mode audit`, nem `governance_edges.json`).
4. Implemente os testes unitários e execute a validação manual com os cenários simulados descritos no plano.
