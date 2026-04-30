#!/usr/bin/env python3
"""captura_projeto.py - Gera bundle markdown AI-first do repositorio. TEMPLATE UNIVERSAL."""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from fnmatch import fnmatch
from pathlib import Path

VERSION = "2.5.2"

# 🛠️ CUSTOMIZE AQUI: Padrões universais + adicione os específicos do seu projeto
PASTAS_IGNORAR = {
    ".git", "node_modules", "dist", "build", "out", "target", "bin", "obj",
    "__pycache__", ".venv", "venv", ".tox", ".mypy_cache", ".ruff_cache",
    ".next", ".nuxt", ".vercel", ".netlify", ".vite", ".cache",
    ".vscode", ".idea", ".cursor", "coverage", ".pytest_cache",
    "captura_projeto", # 📝 Ignorar a própria pasta do utilitário
    "_archive_context", "planos", "RAW", "_flash_report",
}

ARQUIVOS_IGNORAR = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "composer.lock",
    "contexto.md", "contexto_*.md", ".*.lock"
}

PASTAS_CORE = {
    # 📝 Defina as pastas ARQUITETURALMENTE essenciais para a IA entender seu projeto
    # Ex: {"src", "lib", "api", "supabase", ".context", ".specs"}
    "src", "lib", "api", ".context", ".specs"
}

# 🛠️ CUSTOMIZE AQUI: Regras de classificação semântica (fallback seguro)
DOMAIN_RULES = {
    r"/api/|/routes/|/handlers/|/controllers/": "api",
    r"/components/|/ui/|/views/|/pages/|/screens/": "ui",
    r"/lib/|/utils/|/helpers/|/core/|/shared/": "lib",
    r"/db/|/migrations/|/models/|/schema/|/supabase/|/prisma/": "db",
    r"/tests/|/spec/|/__tests__/|\.test\.|\.spec\.": "tests",
    r"/config/|/settings/|/env/": "config",
    r"\.md$|\.rst$|\.txt$": "docs",
    r"\.(json|toml|yaml|yml|ini)$": "config",
}

EXTENSOES_PERMITIDAS = {
    ".js", ".jsx", ".ts", ".tsx", ".py", ".html", ".css", ".json", ".md",
    ".yaml", ".yml", ".toml", ".sh", ".sql", ".graphql", ".vue", ".svelte",
    ".rs", ".go", ".java", ".c", ".h", ".hpp", ".cpp", ".ini",
}

LINGUAGENS = {
    ".js": "javascript", ".jsx": "jsx", ".ts": "typescript", ".tsx": "tsx",
    ".py": "python", ".html": "html", ".css": "css", ".json": "json", ".md": "markdown",
    ".yaml": "yaml", ".yml": "yaml", ".toml": "toml", ".sh": "bash", ".sql": "sql",
    ".graphql": "graphql", ".vue": "html", ".svelte": "html", ".rs": "rust",
    ".go": "go", ".java": "java", ".c": "c", ".h": "c", ".hpp": "cpp", ".cpp": "cpp", ".ini": "ini",
}

ARQUIVOS_SENSIVEIS_GLOBS = {
    ".env*", "*.pem", "*.key", "*.p12", "*.pfx",
    "credentials*.json", "id_rsa*", "secrets.*", "*.cert",
    # 📝 Adicione padrões sensíveis do SEU projeto aqui
}

SECRET_PATTERNS = (
    re.compile(r'(["\']?)(\w*(?:API_KEY|SECRET|TOKEN|PASSWORD|AUTH_KEY|PRIVATE_KEY|ACCESS_KEY|DB_PASS|CONNECTION_STRING)\w*)\1\s*[:=]\s*["\']?(\S+)["\']?', re.IGNORECASE),
    re.compile(r'(BEGIN\s+(RSA|EC|DSA|OPENSSH|PGP)\s+PRIVATE\s+KEY)', re.IGNORECASE),
)

DEFAULT_OUTPUT = "contexto.md"
logging.basicConfig(level=logging.WARNING, format="⚠️ %(message)s")

@dataclass(frozen=True)
class BundleConfig:
    diretorio: Path
    output: str = DEFAULT_OUTPUT
    only_core: bool = False
    exclude_core: bool = False
    profile: str = "ai-default"
    toc_only: bool = False
    max_lines_per_file: int = 300
    emit_symbol_index: bool = False
    emit_import_map: bool = False
    mask_secrets: bool = False
    include_lockfiles: bool = False

@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_line: int
    end_line: int
    content: str

@dataclass(frozen=True)
class FileRecord:
    file_id: str
    relative_path: str
    domain: str
    language: str
    line_count: int
    byte_count: int
    mtime_utc: str
    sha1: str
    symbols: tuple[str, ...]
    imports: tuple[str, ...]
    chunks: tuple[Chunk, ...]

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXTENSOES_PERMITIDAS:
        return True
    mime, _ = mimetypes.guess_type(path)
    if not mime:
        return False
    return mime.startswith("text/") or mime in {"application/json", "application/xml", "application/javascript"}

def is_sensitive_file(path: Path) -> bool:
    return any(fnmatch(path.name.lower(), pat.lower()) for pat in ARQUIVOS_SENSIVEIS_GLOBS)

def classify_domain(relative_path: str) -> str:
    p = relative_path.lower()
    for pattern, domain in DOMAIN_RULES.items():
        if re.search(pattern, p):
            return domain
    return "source"

def should_include_profile(record_domain: str, config: BundleConfig) -> bool:
    if config.profile == "ai-compact":
        return record_domain not in {"tests", "docs"}
    return True

def mask_sensitive(content: str, enabled: bool) -> str:
    if not enabled:
        return content
    out = content
    for pattern in SECRET_PATTERNS:
        out = pattern.sub(r"\1***", out)
    return out

def extract_symbols(content: str, suffix: str) -> tuple[str, ...]:
    symbols: list[str] = []
    if suffix == ".py":
        symbols.extend(re.findall(r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content, re.MULTILINE))
        symbols.extend(re.findall(r"^class\s+([A-Za-z_][A-Za-z0-9_]*)\s*[:(]", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        symbols.extend(re.findall(r"(?:export\s+)?function\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", content))
        symbols.extend(re.findall(r"(?:export\s+)?class\s+([A-Za-z_][A-Za-z0-9_]*)\s*", content))
        symbols.extend(re.findall(r"export\s+const\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", content))
    seen, seen_set = [], set()
    for s in symbols:
        if s not in seen_set:
            seen.append(s)
            seen_set.add(s)
    return tuple(seen[:80])

def extract_imports(content: str, suffix: str) -> tuple[str, ...]:
    imports: list[str] = []
    if suffix == ".py":
        imports.extend(re.findall(r"^import\s+([^\n]+)", content, re.MULTILINE))
        imports.extend(re.findall(r"^from\s+([^\s]+)\s+import\s+([^\n]+)", content, re.MULTILINE))
    elif suffix in {".js", ".jsx", ".ts", ".tsx"}:
        imports.extend(re.findall(r"^import\s+[^\n]*?from\s+['\"]([^'\"]+)['\"]", content, re.MULTILINE))
        imports.extend(re.findall(r"require\(['\"]([^'\"]+)['\"]\)", content))
    normalized, seen_set = [], set()
    for item in imports:
        val = f"from {item[0]} import {item[1]}" if isinstance(item, tuple) else item
        if val not in seen_set:
            normalized.append(val)
            seen_set.add(val)
    return tuple(normalized[:120])

def chunk_content(content: str, file_id: str, max_lines: int) -> tuple[Chunk, ...]:
    lines = content.splitlines()
    if not lines:
        return (Chunk(f"{file_id}_c001", 1, 1, ""),)
    if max_lines <= 0 or len(lines) <= max_lines:
        return (Chunk(f"{file_id}_c001", 1, len(lines), content),)
    chunks = []
    idx = 1
    for start in range(0, len(lines), max_lines):
        end = min(start + max_lines, len(lines))
        part = "\n".join(lines[start:end])
        if end < len(lines) or content.endswith("\n"):
            part += "\n"
        chunks.append(Chunk(f"{file_id}_c{idx:03d}", start + 1, end, part))
        idx += 1
    return tuple(chunks)

def make_file_id(relative_path: str) -> str:
    return hashlib.sha1(relative_path.encode("utf-8")).hexdigest()[:12]

def collect_files(config: BundleConfig) -> tuple[FileRecord, ...]:
    records: list[FileRecord] = []
    root = config.diretorio.resolve()

    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        current = Path(dirpath)
        is_root = (current == root)

        # 🛡️ Isolamento Cirúrgico (v2.4.1): Ignora pastas densas específicas
        rel_dir = current.relative_to(root).as_posix()
        if rel_dir == ".context/market":
            dirnames[:] = [d for d in dirnames if d not in {"compliance", "research", "RAW"}]

        if config.only_core:
            dirnames[:] = sorted(d for d in dirnames if (d in PASTAS_CORE or not is_root) and d not in PASTAS_IGNORAR)
        elif config.exclude_core:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_CORE and d not in PASTAS_IGNORAR)
        else:
            dirnames[:] = sorted(d for d in dirnames if d not in PASTAS_IGNORAR)

        for filename in sorted(filenames):
            path = current / filename
            rel = path.relative_to(root)
            rel_path = rel.as_posix()
            top = rel.parts[0] if rel.parts else ""

            if config.only_core and is_root and top not in PASTAS_CORE:
                continue
            if config.exclude_core and is_root and top in PASTAS_CORE:
                continue
            
            # 🛡️ Blindagem contra Self-Capture e Locks
            is_output_file = (filename == config.output or filename == get_dynamic_filename(config))
            is_ignored_file = any(fnmatch(filename.lower(), pat.lower()) for pat in ARQUIVOS_IGNORAR)
            is_lockfile = ("lock" in filename.lower() and path.suffix in {".json", ".yaml", ".yml", ".lock"})

            # Filtro path-scoped para Market (v2.4.1 Hardened)
            # Ignora pastas de documentos brutos para evitar token bloat no bundle
            if "market/compliance" in rel_path.lower() or "market/research" in rel_path.lower():
                continue

            if is_output_file: 
                continue
            if is_ignored_file and not (is_lockfile and config.include_lockfiles):
                continue

            if is_sensitive_file(path):
                continue
            if not is_text_file(path):
                continue

            try:
                raw_content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                try:
                    raw_content = path.read_text(encoding="latin-1")
                except OSError as e:
                    logging.warning("Pulando %s: %s", rel_path, e)
                    continue
            except OSError as e:
                logging.warning("Pulando %s: %s", rel_path, e)
                continue

            domain = classify_domain(rel_path)
            if not should_include_profile(domain, config):
                continue

            raw_sha1 = hashlib.sha1(raw_content.encode("utf-8", errors="ignore")).hexdigest()
            content = mask_sensitive(raw_content, config.mask_secrets)
            file_id = make_file_id(rel_path)
            stat = path.stat()
            suffix = path.suffix.lower()

            symbols = extract_symbols(content, suffix) if config.emit_symbol_index else ()
            imports = extract_imports(content, suffix) if config.emit_import_map else ()
            chunks = chunk_content(content, file_id, config.max_lines_per_file)

            records.append(FileRecord(
                file_id=file_id, relative_path=rel_path, domain=domain,
                language=LINGUAGENS.get(suffix, suffix[1:] if suffix else "text"),
                line_count=len(content.splitlines()),
                byte_count=len(content.encode("utf-8", errors="ignore")),
                mtime_utc=datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat(),
                sha1=raw_sha1, symbols=symbols, imports=imports, chunks=chunks
            ))

    records.sort(key=lambda r: r.relative_path)
    return tuple(records)

def mode_name(config: BundleConfig) -> str:
    parts = []
    if config.only_core: parts.append("only-core")
    elif config.exclude_core: parts.append("exclude-core")
    else: parts.append("full")
    if config.toc_only: parts.append("TOC")
    return " | ".join(parts)

def get_dynamic_filename(config: BundleConfig) -> str:
    # Se o usuário não mudou o default, geramos um nome inteligente
    if config.output != DEFAULT_OUTPUT:
        return config.output
    
    base = "contexto"
    ver = f"_v{VERSION}"
    suffix = ""
    if config.toc_only: suffix += "_toc"
    if config.only_core: suffix += "_core"
    
    return f"{base}{ver}{suffix}.md"

def render_frontmatter(config: BundleConfig, records: tuple[FileRecord, ...]) -> str:
    total_bytes = sum(r.byte_count for r in records)
    lines = [
        "---", "schema_version: 1",
        f"generated_at: {datetime.now(timezone.utc).isoformat()}",
        f"root: {config.diretorio.resolve().name}",
        f"mode: {mode_name(config)}", f"profile: {config.profile}",
        f"file_count: {len(records)}", f"byte_count: {total_bytes}",
        "ignored_dirs:"
    ]
    lines.extend(f"  - {d}" for d in sorted(PASTAS_IGNORAR))
    lines.append("sensitive_rules:")
    lines.extend(f"  - {r}" for r in sorted(ARQUIVOS_SENSIVEIS_GLOBS))
    lines.append("---")
    return "\n".join(lines)

def render_index_by_domain(records: tuple[FileRecord, ...]) -> str:
    grouped: dict[str, list[FileRecord]] = {}
    for r in records:
        grouped.setdefault(r.domain, []).append(r)
    lines = ["## INDEX_BY_DOMAIN"]
    for domain in sorted(grouped):
        lines.append(f"- `{domain}`:")
        lines.extend(f"  - `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in grouped[domain])
    return "\n".join(lines)

def render_index_by_path(records: tuple[FileRecord, ...]) -> str:
    lines = ["## INDEX_BY_PATH"]
    lines.extend(f"- `{r.relative_path}` -> [file_{r.file_id}](#file_{r.file_id})" for r in records)
    return "\n".join(lines)

def render_symbols(records: tuple[FileRecord, ...]) -> str:
    lines = ["## SYMBOL_INDEX"]
    for r in records:
        if not r.symbols: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{s}`" for s in r.symbols)
    return "\n".join(lines)

def render_imports(records: tuple[FileRecord, ...]) -> str:
    lines = ["## IMPORT_MAP_MIN"]
    for r in records:
        if not r.imports: continue
        lines.append(f"- `{r.relative_path}`:")
        lines.extend(f"  - `{i}`" for i in r.imports)
    return "\n".join(lines)

def pick_fence(content: str) -> str:
    return "````" if "```" in content else "```"

def render_file_record(record: FileRecord, toc_only: bool) -> str:
    lines = [
        "---", f'<a id="file_{record.file_id}"></a>',
        f"FILE_START id=file_{record.file_id} path={record.relative_path} "
        f"domain={record.domain} lang={record.language} lines={record.line_count} "
        f"bytes={record.byte_count} mtime={record.mtime_utc} sha1={record.sha1}"
    ]
    if toc_only:
        lines.append("CONTENT_OMITTED toc_only=true")
    else:
        for chunk in record.chunks:
            lines.append(f"CHUNK_START id={chunk.chunk_id} start_line={chunk.start_line} end_line={chunk.end_line}")
            fence = pick_fence(chunk.content)
            lines.extend([f"{fence}{record.language}", chunk.content, fence, f"CHUNK_END id={chunk.chunk_id}"])
    lines.append(f"FILE_END id=file_{record.file_id}")
    return "\n".join(lines)

def generate_context_markdown(config: BundleConfig) -> str:
    if config.only_core and config.exclude_core:
        raise ValueError("only_core e exclude_core nao podem ser usados juntos")
    
    records = collect_files(config)
    blocks = ["# Project Context Bundle", "", render_frontmatter(config, records), "",
              render_index_by_domain(records), "", render_index_by_path(records)]
    if config.emit_symbol_index:
        blocks.extend(["", render_symbols(records)])
    if config.emit_import_map:
        blocks.extend(["", render_imports(records)])
    for r in records:
        blocks.extend(["", render_file_record(r, toc_only=config.toc_only)])
    return "\n".join(blocks) + "\n"

def write_output(config: BundleConfig) -> Path:
    target_name = get_dynamic_filename(config)
    output_path = config.diretorio / target_name
    content = generate_context_markdown(config)
    output_path.write_text(content, encoding="utf-8")
    return output_path

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="captura_projeto.py - Consolida repositorio em markdown AI-first")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretorio raiz")
    parser.add_argument("-o", "--output", default=DEFAULT_OUTPUT, help="Arquivo de saida")
    core = parser.add_mutually_exclusive_group()
    core.add_argument("--only-core", action="store_true", help="Inclui apenas escopo core")
    core.add_argument("--exclude-core", action="store_true", help="Exclui escopo core")
    parser.add_argument("--profile", choices=["ai-default", "ai-compact", "ai-forensics"], default="ai-default")
    parser.add_argument("--toc-only", action="store_true", help="Apenas indices e envelopes")
    parser.add_argument("--max-lines-per-file", type=int, default=300, help="Limite de linhas por chunk (0=ilimitado)")
    parser.add_argument("--emit-symbol-index", action="store_true", help="Adiciona SYMBOL_INDEX")
    parser.add_argument("--emit-import-map", action="store_true", help="Adiciona IMPORT_MAP_MIN")
    parser.add_argument("--mask-secrets", action="store_true", help="Ofusca segredos no conteudo")
    parser.add_argument("--include-lockfiles", action="store_true", help="Força a inclusão de package-lock.json e similares")
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    config = BundleConfig(
        diretorio=Path(args.diretorio), output=args.output,
        only_core=args.only_core, exclude_core=args.exclude_core,
        profile=args.profile, toc_only=args.toc_only,
        max_lines_per_file=args.max_lines_per_file,
        emit_symbol_index=args.emit_symbol_index,
        emit_import_map=args.emit_import_map, mask_secrets=args.mask_secrets,
        include_lockfiles=args.include_lockfiles
    )
    out = write_output(config)
    print(f"\n[OK] Gerado: {out}")
    print(f"   Mode: {mode_name(config)} | Profile: {config.profile}")

if __name__ == "__main__":
    main()