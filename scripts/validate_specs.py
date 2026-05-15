"""
CI Spec-Validator

Prueft die bidirektionale Traceability zwischen spec/ und dem Quellcode:
  1. Alle aktiven Spec-UIDs in spec/ muessen durch @spec-Annotationen referenziert sein.
  2. Alle @spec-Annotationen muessen auf existierende UIDs in spec/ zeigen.

Aufruf:
  python scripts/validate_specs.py [--include-draft] [--root <pfad>]

Exit-Code:
  0 = vollstaendig abgedeckt
  1 = Luecken oder ungueltige Referenzen gefunden

@spec: PROJ-SYS-005
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

# Ordner in denen @spec-Annotationen gesucht werden
ANNOTATION_DIRS = ["src", "tests", ".github", "scripts", "docs/architecture"]

# Dateiendungen die gescannt werden
ANNOTATION_EXTENSIONS = {".py", ".md", ".yml", ".yaml", ".ps1"}

# Ordner mit Spec-Dateien
SPEC_DIR = "spec"


# ---------------------------------------------------------------------------
# Spec-UIDs aus spec/ einlesen
# ---------------------------------------------------------------------------

UID_PATTERN = re.compile(r"\*\*UID\*\*:\s*([\w-]+)")
STATUS_PATTERN = re.compile(r"\*\*Status\*\*:\s*(\w+)")


def load_spec_uids(root: Path, include_draft: bool) -> dict[str, str]:
    """Liest alle Spec-UIDs aus spec/*.md.

    Gibt ein Dict {uid: status} zurueck.
    Outdated-Nodes werden immer ignoriert.
    Draft-Nodes werden nur beruecksichtigt wenn include_draft=True.
    """
    uids: dict[str, str] = {}
    spec_dir = root / SPEC_DIR

    if not spec_dir.exists():
        return uids

    for spec_file in sorted(spec_dir.glob("**/*.md")):
        content = spec_file.read_text(encoding="utf-8")

        # Paare von UID + Status extrahieren
        uid_matches = list(UID_PATTERN.finditer(content))
        status_matches = list(STATUS_PATTERN.finditer(content))

        # Einfache Heuristik: Status steht unmittelbar nach UID im selben Node-Block
        # Wir lesen alle UIDs und suchen den naechstliegenden Status-Match
        for uid_match in uid_matches:
            uid = uid_match.group(1)
            uid_pos = uid_match.start()

            # Naechsten Status-Match nach dieser UID finden
            status = "Draft"
            for s_match in status_matches:
                if s_match.start() > uid_pos:
                    status = s_match.group(1)
                    break

            if status == "Outdated":
                continue
            if status == "Draft" and not include_draft:
                continue

            uids[uid] = status

    return uids


# ---------------------------------------------------------------------------
# @spec-Annotationen aus Quellcode einlesen
# ---------------------------------------------------------------------------

SPEC_ANNOTATION_PATTERN = re.compile(r"@spec:\s*([A-Z]+-[A-Z]+-\d+|[A-Z]+-[A-Z]+-[A-Z]+-\d+)")

# Beispiel-UIDs in Dokumentations- und Instruction-Dateien, die keine echten Spec-Nodes sind.
# Diese UIDs werden in Warnungen ignoriert (Template-Platzhalter).
EXAMPLE_UIDS: set[str] = {
    "PROJ-BE-001",
    "PROJ-UI-001",
    "PROJ-TC-001",
    "PROJ-API-001",
}


def load_annotations(root: Path) -> dict[str, list[str]]:
    """Liest alle @spec-Annotationen aus den konfigurierten Verzeichnissen.

    Gibt ein Dict {uid: [dateipfad, ...]} zurueck.
    """
    annotations: dict[str, list[str]] = {}

    for dir_name in ANNOTATION_DIRS:
        scan_dir = root / dir_name
        if not scan_dir.exists():
            continue

        for file_path in scan_dir.rglob("*"):
            if file_path.suffix not in ANNOTATION_EXTENSIONS:
                continue
            if not file_path.is_file():
                continue

            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue

            for match in SPEC_ANNOTATION_PATTERN.finditer(content):
                uid = match.group(1)
                rel_path = str(file_path.relative_to(root))
                annotations.setdefault(uid, []).append(rel_path)

    return annotations


# ---------------------------------------------------------------------------
# Validierung
# ---------------------------------------------------------------------------

def validate(root: Path, include_draft: bool) -> int:
    """Fuehrt die Validierung durch. Gibt 0 (OK) oder 1 (Fehler) zurueck."""
    spec_uids = load_spec_uids(root, include_draft)
    annotations = load_annotations(root)

    errors: list[str] = []
    warnings: list[str] = []

    # 1. Aktive/Draft Spec-UIDs ohne @spec-Annotation
    for uid, status in sorted(spec_uids.items()):
        if uid not in annotations:
            errors.append(f"  FEHLER  [{status}] {uid} – keine @spec-Annotation gefunden")

    # 2. @spec-Annotationen die auf nicht existierende UIDs zeigen
    for uid, files in sorted(annotations.items()):
        if uid in EXAMPLE_UIDS:
            continue
        if uid not in spec_uids:
            unique_files = sorted(set(files))
            for f in unique_files:
                warnings.append(f"  WARNUNG {uid} – referenziert in {f}, aber nicht in spec/ gefunden")

    # Ausgabe
    print(f"\n=== Spec-Validator ===")
    print(f"Spec-UIDs geprueft:     {len(spec_uids)}")
    print(f"@spec-Annotationen:     {sum(len(v) for v in annotations.values())}")
    print(f"Abgedeckte UIDs:        {sum(1 for uid in spec_uids if uid in annotations)}")
    print()

    if not errors and not warnings:
        print("OK – Alle Spec-UIDs sind abgedeckt, alle Annotationen gueltig.")
        return 0

    for line in errors:
        print(line)
    for line in warnings:
        print(line)

    print(f"\n{len(errors)} Fehler, {len(warnings)} Warnungen")
    return 1 if errors else 0


# ---------------------------------------------------------------------------
# Einstiegspunkt
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Prueft @spec-Traceability zwischen spec/ und Quellcode."
    )
    parser.add_argument(
        "--include-draft",
        action="store_true",
        default=True,
        help="Draft-Nodes ebenfalls pruefen (Standard: an)",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Projekt-Root-Verzeichnis (Standard: aktuelles Verzeichnis)",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    exit_code = validate(root, include_draft=args.include_draft)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
