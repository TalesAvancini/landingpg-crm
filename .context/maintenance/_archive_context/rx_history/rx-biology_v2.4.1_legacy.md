---
Criado em: 2026-04-14
Ultima Atualizacao: 2026-04-16
Status: Ativo (v2.4.1-Hardened)
---

# 🧬 rx-biology.md (Raio-X de Comportamento AI)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita como as IAs interagem com a máquina de estados (O MODO DE PENSAR e HANDOFF).
> - **NÃO** descreva arquiteturas de banco de dados ou diagramas de componentes de software aqui.
> - **NÃO** adicione regras de compilação ou deploy (use os scripts raiz ou `.github/`).
> - Foco 100% no Ralph Wiggum Loop e regras comportamentais entre Agentes.

> Documenta as biológicas de interação, limites cognitivos e padrões de resposta esperados da IA orbitando a Tríade H.O.K Forge.

## 🧠 Modus Operandi (O Ralph Wiggum Loop)
As IAs devem atuar de forma **efêmera e cirúrgica**:
1. **Foco Atômico:** Ignorar abstrações além do estritamente necessário para resolver a Spec atual. 
2. **Ciclo de Amnésia:** Uma vez que a tarefa ou conjunto de specs termina, os resultados difíceis ("lições ganhas") são transferidos para o `JOURNAL.md` e o loop "esquece" o resto. A memória reside no `FileSystem (.context/)`.

## 🛡️ Handoff & Cruzamento de Domínio
A integridade da continuidade é garantida pelas transferências no _JOURNAL.md_. O Formato Oficial cobrado pelo `harness_runner.py`:
- `🔄 Handoff: @[role-atual] -> @[role-próxima] | Estado: [Status técnico] | Próximo: [O que precisa ser feito]`

## 🔍 Comportamento Epistemológico (Regra Karpathy)
A IA não tem permissão para assumir dogmas técnicos (claims) sem citar a fonte da documentação original:
- Todo conselho ou decisão estrutural no `.context/` deve vir acompanhado de `> Fonte: raw/nome-do-arquivo.md`.
- **Tratamento de Erro:** Em caso de dúvida técnica ou ausência de documentação de referência cruzada, acione o `npm run context:oracle`. Nunca adivinhe requisitos.

> 🛠️ **Diretriz de Segurança:** Todo o roteamento é impulsionado por `run_context.py`. Evite invocar scripts bash de baixo nível se houver comandos npm (`context:*`) mapeados.
