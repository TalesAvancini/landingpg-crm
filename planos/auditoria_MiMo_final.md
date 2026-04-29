# 🔎 Auditoria Final do Plano Consolidado Oracle v3 (MiMo — Segunda Rodada)

> **Autor:** MiMo (Auditor)
> **Alvo:** `plano_consolidado_Oracle_v3.md`
> **Data:** 2026-04-28
> **Contexto:** O plano não foi atualizado após a primeira auditoria. As 7 críticas originais permanecem sem endereçamento.

---

## O Problema Central

Há uma contradição entre a filosofia do plano ("Consertar primeiro. Calibrar depois.") e o próprio processo de criação do plano. Cinco relatórios diferentes foram sintetizados, decisões foram tomadas, descartes foram justificados — mas **nenhum feedback externo foi incorporado**. O documento é idêntico ao que eu critiquei antes.

Isso é relevante porque o Oracle vai ter o mesmo problema se não houver feedback loop. O item 2.5 (oracle_analytics.py) existe justamente para isso — transformar queries falhadas em melhorias. Mas o plano em si não pratica o que prega.

---

## O Que Eu Insisto

**O item mais importante do plano continua ausente: testes automatizados.** Sem testes, cada um dos 15 itens é uma mudança cega. A ordem deveria ser:

```
0.0  Criar suíte de testes com 10-15 queries de validação
0.1  Fix _index.md
0.2  Aliases
0.3  Siglas
0.4  Warnings
1.1  Stemming (rodar testes — verificar que não regrediu)
1.2  Confidence (rodar testes — verificar que não regrediu)
...
```

A suíte de testes é o item 0.0, não um complemento.

---

## O Que Eu Aceito

A estrutura de fases está correta. A tabela de descartes continua sendo a melhor parte. A decisão de busca imparcial sem multiplicador de role é acertada. O Gate Epistemológico em Modo Light é a postura certa. O fallback para NotebookLM estar adiado é pragmático.

---

## Minha Posição Final

O plano é **8/10 como documento de direção** e **6/10 como documento de execução**. Sem a suíte de testes, é um salto de fé. Com ela, é engenharia.
