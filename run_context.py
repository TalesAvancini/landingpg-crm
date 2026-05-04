#!/usr/bin/env python3
"""
🐍 run_context.py - Gestor Universal de Contexto v2.5.0 (Hardened Pipeline)
Sequencia otimizada: validate → scan-secrets → sync → migrations → harness → lint(strict) → health
"""

import sys
import subprocess
from pathlib import Path

stdout_reconfigure = getattr(sys.stdout, "reconfigure", None)
stderr_reconfigure = getattr(sys.stderr, "reconfigure", None)
if callable(stdout_reconfigure):
    stdout_reconfigure(encoding="utf-8", errors="replace")
if callable(stderr_reconfigure):
    stderr_reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(__file__).parent
SCRIPTS_DIR = BASE_DIR / ".context" / "_scripts"


def run_script(name, args=None, capture=False):
    if args is None:
        args = []
    script_path = SCRIPTS_DIR / name
    if not script_path.exists():
        print(f"[ERROR] Script {name} nao encontrado em {SCRIPTS_DIR}")
        sys.exit(1)

    print(f"[RUN] Executando {name}...")
    try:
        # Refatoração sugerida pela auditoria: Remover check=True para tratar códigos semânticos
        res = subprocess.run([sys.executable, str(script_path)] + args, check=False)

        if res.returncode == 0:
            print(f"[OK] Concluido: {name}\n")
            return 0
        elif res.returncode == 2:
            print(f"[STRATEGIC BLOCK] Pendência em {name}. Pipeline local TRAVADO.\n")
            sys.exit(2)
        else:
            print(
                f"[FATAL] Falha estrutural em {name}. Exit: {res.returncode}. Pipeline abortado."
            )
            sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Erro na execução de {name}: {e}\n")
        sys.exit(1)


def get_inception_status():
    """Lê o status do Inception mestre."""
    path = BASE_DIR / ".context" / "brain" / "INCEPTION.md"
    if not path.exists():
        return "MISSING"
    try:
        content = path.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.strip().startswith("status:"):
                # Captura o valor antes de qualquer comentário #
                return line.split(":")[1].strip().split("#")[0].strip()
    except:
        return "ERROR"
    return "UNKNOWN"


def main():
    if len(sys.argv) < 2:
        print(
            "[USAGE] python run_context.py [validate|purge|sync|cleanup|harness|lint|lint-strict|oracle|health|scan-secrets|check-migrations|check-version|enrich|workflow-journal|map|bundle|all|help]"
        )
        sys.exit(1)

    cmd = sys.argv[1]
    extra_args = sys.argv[2:]

    # Bloqueio global preventivo (Auditoria: TRANSLATION_LOCK uniforme)
    status = get_inception_status()
    if status == "TRANSLATION_LOCK" and cmd != "enrich" and cmd != "help":
        print(
            "[LOCKED] O projeto está em TRANSLATION_LOCK. Aceite ou rejeite o INCEPTION.proposed.md primeiro."
        )
        sys.exit(2)

    if cmd == "validate":
        run_script("validate_context.py", extra_args)
    elif cmd == "purge":
        run_script("purge_journal.py", extra_args)
    elif cmd == "sync":
        run_script("sync_project.py", extra_args)
    elif cmd == "cleanup":
        run_script("cleanup_specs.py", extra_args)
    elif cmd == "harness":
        run_script("harness_runner.py", extra_args)
    elif cmd == "lint":
        run_script("lint_wiki.py", extra_args)
    elif cmd == "lint-strict":
        run_script("lint_wiki.py", ["--strict"] + extra_args)
    elif cmd == "oracle":
        run_script("context_oracle.py", extra_args)
    elif cmd == "health":
        run_script("health_sync.py", extra_args)
    elif cmd == "scan-secrets":
        run_script("secrets_scanner.py", extra_args)
    elif cmd == "check-migrations":
        run_script("migration_registry.py", extra_args)
    elif cmd == "check-version":
        run_script("check_version_consistency.py", extra_args)

    elif cmd == "enrich":
        run_script("enrich_context.py", extra_args)
    elif cmd == "learnings":
        run_script("learnings_aggregator.py", extra_args)
    elif cmd == "inject":
        run_script("inject_learnings.py", extra_args)
    elif cmd == "wiki-health":
        run_script("validate_context.py", ["check_wiki_integrity"] + extra_args)
    elif cmd == "workflow-journal":
        run_script("workflow_journal_auditor.py", extra_args)
    elif cmd == "map":
        run_script("project_bundler.py", ["--toc-only", "-o", ".context/monitoring/PROJECT_INDEX.md"] + extra_args)
    elif cmd == "bundle":
        run_script("project_bundler.py", ["-o", "contexto.md"] + extra_args)

    elif cmd == "all":
        # Pipeline Fail-Fast (Hardened v2.5.0 + Hybrid Discovery)
        run_script("check_version_consistency.py")
        run_script("validate_context.py")
        run_script("secrets_scanner.py")
        run_script("sync_project.py")
        run_script("migration_registry.py")
        run_script("learnings_aggregator.py") # Adicionado ao pipeline ALL
        run_script("harness_runner.py")
        run_script("ingest_wiki_guard.py")
        print("[RUN] Executando lint_wiki.py (Strict)...")
        run_script("lint_wiki.py", ["--strict"])
        print("[RUN] Sincronizando Health Dashboard...")
        run_script("health_sync.py")
        print("[RUN] Gerando Mapa de Arquivos Atualizado (PROJECT_INDEX)...")
        run_script("project_bundler.py", ["--toc-only", "-o", ".context/monitoring/PROJECT_INDEX.md"])
        print(
            "[DONE] Pipeline H.O.K. + Security + Migrations + Health + Index + Learnings concluído com sucesso."
        )

    elif cmd in ["help", "--help", "-h"]:
        print(
            "Comandos: validate | purge | sync | cleanup | harness | lint | lint-strict | oracle | health | scan-secrets | check-migrations | check-version | enrich | learnings | inject | workflow-journal | map | bundle | all"
        )
    else:
        print(f"❌ Comando desconhecido: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
