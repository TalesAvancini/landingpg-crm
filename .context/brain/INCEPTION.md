---
version: 3.0.0
mode: STRATEGIC
status: DRAFT  # [DRAFT | ACTIVE | TRANSLATION_LOCK]
---

<!-- 🚨 SYSTEM TRIGGER: IA, NÃO PROSSIGA PARA GERAÇÃO DE CÓDIGO SE OS CAMPOS ABAIXO CONTIVEREM "[TODO]" OU PERGUNTAS. INTERROGUE O HUMANO PRIMEIRO. -->
> 🤖 **INSTRUÇÃO DE FLUXO:** Antes de propor specs ou código, preencha os campos estratégicos. Se `[TODO]` persistir, retorne ao humano com: `"⚠️ Contexto incompleto em INCEPTION.md. Preciso de: [lista]"`.

# 🧭 INCEPTION - Fronteiras Estratégicas (SSOT)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita a Estratégia de Negócio e Limites Arquiteturais (O que NUNCA e SEMPRE fazer).
> - **NÃO** insira UUIDs, IDs de nuvem, mapeamento de pastas, nem configurações de ferramentas.
> - Dependências externas devem ir pro `market/SSOT_MAP.md`.
> - Somente a role `@vision-architect` deve alterar significativamente este arquivo.

*Ratificado a partir da tradução cognitiva do `VISION.md`.*

## 🎯 Visão Mestra
[TODO: Insira aqui a visão técnica unificada do novo projeto]

## 🛑 NUNCA (Boundaries)
> *Limites inegociáveis. Se a IA tentar cruzar estas linhas, o Harness aplicará o fail-fast.*
- [TODO: Ex: Nunca criar banco de dados sem autenticação]

## 🛡️ Checklist Estratégico (Preenchimento Obrigatório)
- [ ] **Transações DB?** (Sim/Não. Se sim, qual engine?)
- [ ] **APIs Externas?** (Ex: Stripe, Meta, OpenAI)
- [ ] **Compliance Obrigatório?** (Ex: LGPD, HIPAA, PCI)

## 🟢 SEMPRE (Restrições de Processo)
> *Processos que a IA deve invocar obrigatoriamente durante o ciclo de vida.*
- [TODO: Ex: Sempre validar entrada de formulário no backend]
