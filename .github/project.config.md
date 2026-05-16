# Projektkonfiguration

**Diese Datei** ist die primäre Konfiguration. Zusätzlich muss `strictdoc_config.py` (Feld `project_title`) angepasst werden.
Setup, Ordnerstruktur und Workflow-Referenz: `SETUP.md`.

---

## Projekt-Identifikation

| Feld | Wert |
|------|------|
| Projektkürzel | `PROJ` |
| Projekttitel | MyProject |
| Repository | org/my-project |

---

## Spec-ID-Zähler

Format: `PROJ-[CODE]-NNN` · Nummernraum pro Code getrennt · Datei: `spec/PROJ-[CODE]-NNN-<titel>.md`
Code-Definitionen: `specification.instructions.md`, Abschnitt 7.

| Code | Nächste freie ID |
|------|-----------------|
| `SYS` | `PROJ-SYS-012` |
| `UI` | `PROJ-UI-001` |
| `BE` | `PROJ-BE-001` |
| `API` | `PROJ-API-001` |
| `DATA` | `PROJ-DATA-001` |
| `INT` | `PROJ-INT-001` |
| `SEC` | `PROJ-SEC-001` |
| `SAF` | `PROJ-SAF-001` |
| `TC` | `PROJ-TC-009` |
| `TC-U` | `PROJ-TC-U-001` |
| `TC-I` | `PROJ-TC-I-001` |
| `TC-Q` | `PROJ-TC-Q-001` |

← Zähler bei Vergabe aktualisieren. Nicht verwendete Codes einfach weglassen.

---

## Tooling-Entscheidungen

| Tool | Eingesetzt | Begründung |
|------|-----------|------------|
| Python venv | **Pflicht** | Alle Python-Befehle (pytest, strictdoc, pip) laufen ausschließlich in `.venv`. Kein globales pip install. |
| StrictDoc | **Ja** | MD-Support seit v0.21.0. Automatische Traceability-Matrix. |
| CI Spec-Validator | **Ja** | `scripts/validate_specs.py` + `.github/workflows/ci.yml` – prüft `@spec`-Traceability bei jedem Push |
| Test-Runner | **pytest** | Standard Python Test-Framework. |
| Code Coverage | **pytest-cov** | Integriert in pytest. XML-Output für CI. `pytest --cov=src --cov-report=xml --cov-report=html` |
| Test-Reports / Traceability | **allure-pytest** | Apache-2.0. HTML-Reports mit Requirement-Linking via `@allure.link()`. CI: `allure-report/allure-action`. Upgrade-Pfad: `mlx.traceability` (Melexis, ASPICE-grade). |
