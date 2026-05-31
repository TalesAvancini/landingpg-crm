#!/usr/bin/env python3
"""
🛡️ env_drift_gate.py — Harness de Variáveis de Ambiente
Varre os arquivos do projeto para garantir que as variáveis de ambiente process.env.*
utilizadas no código estejam devidamente declaradas em .env.example.
"""
import os
import re
import sys
from pathlib import Path

# Configuração de encoding para Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_EXAMPLE_PATH = BASE_DIR / ".env.example"

IGNORED_DIRS = {
    "node_modules",
    ".git",
    ".context",
    "scratch",
    "planos",
    "temp",
    ".agent",
    ".agents",
    "graphify-out"
}

def get_env_example_vars():
    """Retorna o conjunto de variáveis declaradas no .env.example."""
    if not ENV_EXAMPLE_PATH.exists():
        return set()
    
    content = ENV_EXAMPLE_PATH.read_text(encoding="utf-8", errors="ignore")
    vars_found = set()
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split("=", 1)
        if parts:
            var_name = parts[0].strip()
            if re.match(r"^[A-Z_][A-Z0-9_]*$", var_name):
                vars_found.add(var_name)
    return vars_found

def scan_code_for_env_vars():
    """Varre arquivos JS do projeto procurando por process.env.VAR ou process.env['VAR']."""
    vars_in_code = {}
    
    # Regex para capturar process.env.VAR e process.env['VAR'] ou process.env["VAR"]
    pattern = r"process\.env\.([a-zA-Z_][a-zA-Z0-9_]*)|process\.env\[['\"]([a-zA-Z_][a-zA-Z0-9_]*)['\"]\]"
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Ignorar diretórios específicos
        dirs[:] = [d for d in dirs if d not in IGNORED_DIRS]
        
        for file in files:
            if not file.endswith((".js", ".ts", ".jsx", ".tsx")):
                continue
                
            file_path = Path(root) / file
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
                matches = re.findall(pattern, content)
                for m in matches:
                    var_name = m[0] or m[1]
                    if var_name:
                        rel_path = file_path.relative_to(BASE_DIR)
                        vars_in_code.setdefault(var_name, []).append(str(rel_path).replace("\\", "/"))
            except Exception as e:
                print(f"[WARN] Falha ao ler {file_path}: {e}")
                
    return vars_in_code

def check_drift():
    print("🛡️ Executando Env Drift Gate (Harness)...")
    example_vars = get_env_example_vars()
    code_vars = scan_code_for_env_vars()
    
    violations = []
    for var, files in code_vars.items():
        if var not in example_vars:
            violations.append(f"Variável '{var}' consumida no código mas ausente no .env.example. Arquivos: {', '.join(files)}")
            
    if violations:
        print("\n❌ VIOLAÇÕES DE DRIFT DE AMBIENTE:")
        for v in violations:
            print(f"  - {v}")
        return 1
        
    print("✅ Env Drift Gate: Todas as variáveis de ambiente utilizadas estão documentadas no .env.example.")
    return 0

if __name__ == "__main__":
    sys.exit(check_drift())
