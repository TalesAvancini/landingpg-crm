# AGENT_SCRATCHPAD: affinity-lite

## 🎯 Current Strategy
Implementar o script `affinity_lite.py` focando em detecção de Drift através de Git e Regex.

## 🔒 Scope Lock (Allow List)
- **Read:**
    - `.context/brain/FILE_GLOSSARY.md`
    - `.context/maintenance/rx-communications.md`
    - Todos os arquivos `.md` e `.py` na raiz e subpastas contextuais.
    - Saída de `git log`.
- **Write:**
    - `.context/_scripts/affinity_lite.py`
    - `.context/maintenance/rx-affinity-lite.md`
    - `.context/maintenance/rx-affinity-lite.json`
    - `STATE.md` (da feature)

## 📥 INBOX (Harness/Blocking Issues)
- *Nenhuma pendência.*

## 📜 DIRECTIVES
1. **Zero-Trust:** Não assumir acoplamento; provar via dados.
2. **Performance:** Usar `subprocess.check_output` para Git.
3. **Auditability:** Gerar JSON estruturado para ferramentas futuras.
