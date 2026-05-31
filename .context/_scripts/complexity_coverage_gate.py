#!/usr/bin/env python3
"""
🛡️ complexity_coverage_gate.py — Complexity and Semantic Coverage Gate
Avisos pedagógicos educativos no pre-commit sobre complexidade de arquivos
e ausência de testes mínimos para novas funções.
"""
import os
import re
import sys
import subprocess
from pathlib import Path

# Configuração de encoding para Windows
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parents[2]

def get_modified_js_files():
    """Retorna lista de arquivos JS modificados ou criados em stage ou working tree."""
    try:
        res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True, cwd=str(BASE_DIR))
        files = []
        for line in res.stdout.splitlines():
            path = line[3:].strip()
            if path.endswith(".js") and not path.startswith((".context", "scratch", "node_modules")):
                files.append(path)
        return files
    except Exception:
        return []

def check_file_complexity(file_path: Path):
    """Verifica se o arquivo JS excede o limite de linhas ou aninhamento excessivo."""
    if not file_path.exists():
        return []
    
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines()
    num_lines = len(lines)
    
    warnings = []
    if num_lines > 250:
        warnings.append(f"Arquivo longo ({num_lines} linhas). Ideal é mantê-lo abaixo de 250 linhas para coesão.")
        
    max_nesting = 0
    curr_nesting = 0
    for line in lines:
        curr_nesting += line.count("{") - line.count("}")
        if curr_nesting > max_nesting:
            max_nesting = curr_nesting
            
    if max_nesting > 4:
        warnings.append(f"Aninhamento de chaves excessivo ({max_nesting} níveis). Considere extrair subfunções.")
        
    return warnings

def check_semantic_coverage(file_path: Path):
    """Verifica se novas funções declaradas no arquivo JS possuem strings de teste associadas."""
    if not file_path.exists():
        return []
        
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    
    test_file_candidates = [
        BASE_DIR / "tests" / f"{file_path.stem}.test.js",
        BASE_DIR / "tests" / f"{file_path.name}",
    ]
    
    test_path = None
    for candidate in test_file_candidates:
        if candidate.exists():
            test_path = candidate
            break
            
    if not test_path:
        return [f"Arquivo de testes '{file_path.stem}.test.js' não encontrado na pasta tests/."]
        
    test_content = test_path.read_text(encoding="utf-8", errors="ignore")
    
    funcs = re.findall(r"function\s+([a-zA-Z_][a-zA-Z0-9_]*)|(?:const|let|var)\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(?:\(|async\s*\(|function)", content)
    func_names = [f[0] or f[1] for f in funcs if f[0] or f[1]]
    
    warnings = []
    for func in func_names:
        if func.startswith("_") or func in {"require", "exports", "module"}:
            continue
            
        if func not in test_content:
            warnings.append(f"Função '{func}' não possui referências no arquivo de teste '{test_path.name}'.")
            
    return warnings

def check_complexity_and_coverage():
    print("🛡️ Executando Complexity & Semantic Coverage Gate (Consultivo)...")
    js_files = get_modified_js_files()
    
    has_warnings = False
    for rel_path in js_files:
        abs_path = BASE_DIR / rel_path
        comp_warns = check_file_complexity(abs_path)
        cov_warns = check_semantic_coverage(abs_path)
        
        all_warns = comp_warns + cov_warns
        if all_warns:
            has_warnings = True
            print(f"\n⚠️ Alertas pedagógicos em '{rel_path}':")
            for w in all_warns:
                print(f"  - {w}")
                
    if has_warnings:
        print("\n💡 Dica de Governança: Tente resolver os alertas acima para melhorar a manutenibilidade.")
        print("ℹ️ Nota: Por estar no Modo Light, este gate é apenas informativo (WARNING) e não bloqueou seu commit.")
    else:
        print("✅ Complexity & Semantic Coverage: Sem alertas pedagógicos pendentes.")
        
    return 0

if __name__ == "__main__":
    sys.exit(check_complexity_and_coverage())
