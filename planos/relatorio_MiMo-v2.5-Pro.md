# Sugestões e Insights para o Harness do H.O.K Forge

Aqui vão ideias que vão desde melhorias incrementais até mudanças mais estruturais. Organizei por impacto e viabilidade.

---

## 1. Telemetria e Métricas do Harness

Hoje o HARNESS_LOG.md registra PASS/FAIL por execução, mas não há **séries temporais**. Você poderia:

- Adicionar um contador acumulado de PASS/FAIL por spec no `STATE.md` (ex: `pass_count: 12`, `fail_count: 3`, `last_fail_reason: "schema contract"`)
- Isso permite identificar **quais checks são os que mais falham**, revelando gargalos reais no workflow
- Um script simples `harness_stats.py` que lê o HARNESS_LOG.md e gera um resumo por tipo de falha já daria visibilidade

**Por que importa:** Se 80% das falhas são de `enrichment_integrity`, o problema não é o código — é o processo de preenchimento do PRD. Métricas direcionam melhorias no lugar certo.

---

## 2. Validação Incremental (não full-scan a cada vez)

O `harness_runner.py` roda todos os 6 checks toda vez. Mas nem todo commit mexe em tudo:

```python
# Sugestão: mapear arquivos alterados → checks necessários
AFFECTED_MAP = {
    "schema.sql": ["schema"],
    "JOURNAL.md": ["handoff", "journal_sam"],
    "PRD.md": ["strategy", "enrichment"],
    "spec.md": ["sprint_contract"],
    "INCEPTION.md": ["strategy"],
}
```

- Usar `git diff --name-only HEAD~1` para detectar o escopo
- Rodar apenas os checks afetados
- Manter o full-scan como opção explícita (`--full`)

**Por que importa:** Em iterações rápidas (escrever no JOURNAL, ajustar um spec), rodar tudo é desnecessariamente lento. Validação incremental reduz atrito.

---

## 3. Sistema de Severidade nos Checks

Hoje todos os checks são binários (PASS ou FAIL). Mas há uma diferença real entre:

- **FATAL**: sprint_contract não assinado → bloqueia commit
- **WARNING**: handoff legado incompleto → loga mas não bloqueia
- **INFO**: enrichment skip (sem integrações) → informativo

```python
# Sugestão de estrutura
checks = {
    "schema":           (SEVERITY.WARNING, check_schema_contract(spec_path)),
    "handoff":          (SEVERITY.WARNING, check_handoff_integrity(...)),
    "strategy":         (SEVERITY.FATAL,   check_strategic_alignment()),
    "enrichment":       (SEVERITY.FATAL,   check_enrichment_integrity(PRD)),
    "sprint_contract":  (SEVERITY.FATAL,   check_sprint_contract(spec_path)),
    "journal_sam":      (SEVERITY.DYNAMIC, check_journal_sam()),  # depende do modo
}
```

O exit code refletiria apenas os FATALs. Warnings iriam para o log.

**Por que importa:** O SAM já tem essa lógica (assist vs strict), mas os outros checks não. Padronizar a severidade evita que warnings bloqueiem indevidamente o fluxo.

---

## 4. Contrato Extensível (Plugin System)

O harness hoje é monolítico — adicionar um novo check exige editar `harness_runner.py`. Uma abordagem mais sustentável:

```
.context/_checks/
    schema_contract.py
    handoff_integrity.py
    strategic_alignment.py
    enrichment_integrity.py
    sprint_contract.py
    journal_sam.py
    # Novos checks aqui ↓
    dependency_freshness.py
    test_coverage_gate.py
```

O `harness_runner.py` descobriria e executaria automaticamente todos os módulos em `_checks/` que implementassem uma interface padrão:

```python
# Interface esperada
def check(context: HarnessContext) -> tuple[bool, str, str]:
    """Retorna (passed, detail, severity)"""
```

**Por que importa:** Desacopla a extensão do core. Você (ou outros contribuidores) podem adicionar validações sem tocar no orquestrador.

---

## 5. Gate de Testes Automatizados

O harness valida **contratos e governança**, mas não valida se o **código funciona**. Um check adicional:

```python
def check_test_gate():
    """Executa suite de testes e verifica resultado."""
    res = subprocess.run(["pytest", "--tb=short", "-q"], 
                         capture_output=True, text=True)
    if res.returncode != 0:
        return False, f"Testes falharam:\n{res.stdout[-500:]}"
    return True, "Testes OK"
```

Integrar como check de severidade WARNING ou FATAL (configurável por spec type).

**Por que importa:** O QA validator confia no Git Diff, mas não executa testes. Um gate de testes no harness fecha essa lacuna.

---

## 6. Validação Semântica Mais Profunda (Sem Regex Pura)

Muitas validações hoje dependem de regex frágeis. Sugestões:

- **Schema contract**: Em vez de regex para extrair nomes de tabelas, usar um parser SQL simples (mesmo que manual com `sqlparse` ou uma abordagem baseada em AST)
- **Strategic alignment**: A detecção de violações `NUNCA:` usa `re.search` com escape. Uma abordagem por **fuzzy matching** ou similaridade de strings capturaria paráfrases também
- **Enrichment**: Em vez de checar literalmente `"fonte:"` e `"market/"`, validar se o path referenciado **existe fisicamente** no repositório

**Por que importa:** Regex é o calcanhar de Aquiles da validação. Um formato inesperado no documento passa batido. Validação semântica é mais resiliente.

---

## 7. Dry-Run Mode

Adicionar um modo `--dry-run` que executa todos os checks mas **não escreve nada** (não atualiza STATE.md, não loga no HARNESS_LOG). Útil para:

- Testar se uma spec passaria antes de submeter
- Debugar falsos positivos
- CI/CD pipelines que querem apenas reportar

---

## 8. Insight Geral: O Harness como "Sistema Imunológico"

Pensando na metáfora que você já usa (rx-anatomy, rx-biology), o Harness funciona como o **sistema imunológico** do projeto. Algumas implicações dessa metáfora que você poderia explorar:

- **Memória imunológica**: O HARNESS_LOG.md poderia manter um "histórico de anticorpos" — padrões de falha que já foram resolvidos, para não re-acionar a falsos positivos já conhecidos
- **Autoimune (false positive)**: Checks que falham sem motivo real (ex: schema check que ignora tabelas de migração pendente). Identificar e corrigir esses "ataques autoimunes" melhora a confiança no sistema
- **Febre (degradação controlada)**: Quando múltiplos checks falham simultaneamente, o sistema poderia entrar em modo degradado (só permite fixes, não novas features) em vez de simplesmente bloquear tudo

---

## 9. Integração com o JOURNAL_SYNAPSE

O `JOURNAL_SYNAPSE.md` já define modos (`assist`/`strict`), mas o harness só usa isso para o SAM. Sugestão: **tornar o modo do Synapse o controlador global de severidade**:

- `assist`: Warnings logam mas não bloqueiam
- `strict`: Tudo é FATAL
- `monitor` (novo): Só loga, nunca bloqueia (útil para observabilidade em projetos novos)

Isso centraliza a "política de imunidade" em um único ponto de controle.

---

## 10. Priorização Sugerida

| Prioridade | Sugestão | Esforço | Impacto |
|---|---|---|---|
| **Alta** | Severidade por check (FATAL/WARNING/INFO) | Baixo | Alto |
| **Alta** | Dry-run mode | Baixo | Médio-Alto |
| **Média** | Validação incremental via git diff | Médio | Alto |
| **Média** | Plugin system para checks | Médio | Alto (longo prazo) |
| **Média** | Telemetria/harness_stats | Baixo | Médio |
| **Baixa** | Gate de testes | Baixo | Médio |
| **Baixa** | Validação semântica profunda | Alto | Médio |

---

A base que você construiu é sólida. O harness já faz o mais difícil: **impedir que coisas erradas avancem**. As sugestões acima são sobre tornar isso mais granular, extensível e informativo — sem perder a rigidez que é o ponto forte do framework.
