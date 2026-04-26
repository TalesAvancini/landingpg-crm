Criado em: 2026-04-10 23:27
Ultima Atualizacao: 2026-04-26 00:57
Status: Ativo


# 🧬 rx-anatomy.md (Raio-X de Anatomia)

> 🛡️ **HARNESS PREVENTIVO (PARA MÁQUINAS)** 
> Este arquivo dita EXCLUSIVAMENTE a Estrutura de Pastas Físicas do repositório.
> - **NÃO** insira regras de negócio, fluxos lógicos ou contratos de base de dados aqui.
> - **NÃO** adicione dependências de infraestrutura de pacote (use `TECHNICAL_REQUIREMENTS.md`).
> - Se você está editando as linhas abaixo, você deve estar criando ou justificando uma PASTA FÍSICA no disco.

> Visão estrutural e organizacional do repositório.

## 📂 Estrutura de Pastas
.
├── .context/               # 🏛️ CAMADA DE GOVERNANÇA (Cérebro/Memória)
│   ├── brain/              # Regras, PRD e Fronteiras (VISION/INCEPTION)
│   ├── market/             # Camada Estratégica (SSOT, Limits, Compliance)
│   ├── maintenance/        # Logs (JOURNAL/HARNESS_LOG), Schema e Inventários
│   ├── monitoring/         # Dashboard de Saúde (CONTEXT_HEALTH.md)
│   └── _scripts/           # Motor de Validação em Python (Oráculo, Harness)
├── .specs/                  # 🧪 BANCADA DE EXECUÇÃO (Workshop Efêmero)
│   └── features/            # Specs atômicas ativas (max 3)
├── tests/                   # Suíte de testes (Infra e Unitários)
├── run_context.py          # ⚙️ Orquestrador Universal Python (SSOT de Execução)
├── init_ai_project.sh      # Bootstrapper Supremo (injeta python no NPM)
└── package.json            # Gerenciamento de libs e rotas context:* (Npm scripts)

## 🧪 .specs/ (Workbench de Execução Atômica)
> Diretório efêmero para Spec-Driven Development (TLC). Criado por demanda, destruído ou arquivado pós-merge.
- **Estrutura:** `.specs/features/[nome]/spec.md`, `STATE.md`, `outputs/`
- **Regra de Vida:** Máx 3 specs ativas simultâneas. >48h sem update → arquivar em `.context/maintenance/_archive_context/specs/`
- **Isolamento:** Não é fonte da verdade. O `.context/` permanece como SSOT. As specs são submetidas à validação do Harness (`run_context.py harness`).
