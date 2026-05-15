# Projektkonfiguration

**Nur diese Datei** muss beim Start eines neuen Projekts angepasst werden.
Setup, Ordnerstruktur und Workflow-Referenz: `.github/instructions/sdd.setup.md`.

---

## Projekt-Identifikation

| Feld | Wert |
|------|------|
| Projektkürzel | `SCAN` |
| Projekttitel | ScanBrother |
| Repository | m2-eng/ScanBrother |

---

## Spec-ID-Zähler

Format: `SCAN-[CODE]-NNN` · Nummernraum pro Code getrennt · Datei: `spec/SCAN-[CODE]-NNN-<titel>.md`
Code-Definitionen: `specification.instructions.md`, Abschnitt 7.

| Code | Nächste freie ID |
|------|-----------------|
| `SYS` | `SCAN-SYS-001` |
| `UI` | `SCAN-UI-001` |
| `BE` | `SCAN-BE-001` |
| `API` | `SCAN-API-001` |
| `DATA` | `SCAN-DATA-001` |
| `INT` | `SCAN-INT-001` |
| `SEC` | `SCAN-SEC-001` |
| `SAF` | `SCAN-SAF-001` |
| `TC` | `SCAN-TC-001` |

← Zähler bei Vergabe aktualisieren. Nicht verwendete Codes einfach weglassen.

---

## Tooling-Entscheidungen

| Tool | Eingesetzt | Begründung |
|------|-----------|------------|
| Python venv | **Pflicht** | Alle Python-Befehle (pytest, strictdoc, pip) laufen ausschließlich in `.venv`. Kein globales pip install. |
| StrictDoc | **Ja** | MD-Support seit v0.21.0. Automatische Traceability-Matrix. |
| CI Spec-Validator | Nein | Noch nicht spezifiziert. |
| Test-Runner | **pytest** | Standard Python Test-Framework. |
| Code Coverage | **pytest-cov** | Integriert in pytest. XML-Output für CI. `pytest --cov=src --cov-report=xml --cov-report=html` |
| Test-Reports / Traceability | **allure-pytest** | Apache-2.0. HTML-Reports mit Requirement-Linking via `@allure.link()`. CI: `allure-report/allure-action`. Upgrade-Pfad: `mlx.traceability` (Melexis, ASPICE-grade). |
