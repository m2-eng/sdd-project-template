# Changelog

Alle Baseline-Freigaben werden hier dokumentiert.
Format orientiert sich an [Keep a Changelog](https://keepachangelog.com).
Versionierung: `vMAJOR.MINOR` – Major bei Spec-Änderung, Minor bei Code/Test-Korrektur.
Jeder Eintrag referenziert die enthaltenen Spec-IDs (`PROJ-[CODE]-NNN`).
Git-Tag bei Baseline: `baseline/vX.Y`.

---

## [Unreleased]

---

## [v1.0] - 2026-05-15

### Neue Anforderungen
- PROJ-SYS-001: ASPICE SWE.1 – Software Requirements Analysis
- PROJ-SYS-002: ASPICE SWE.2 – Software Architectural Design
- PROJ-SYS-003: ASPICE SWE.4 – Software Unit Verification
- PROJ-SYS-004: ASPICE SUP.1 – Quality Assurance
- PROJ-SYS-005: ASPICE SUP.2 – Verification (CI Spec-Validator)
- PROJ-SYS-006: ASPICE SUP.8 – Configuration Management
- PROJ-SYS-007: ASPICE SUP.10 – Change Request Management

### Infrastruktur
- `spec/` mit 7 ASPICE-Compliance-Nodes (PROJ-SYS-001..007, Status: Active)
- `scripts/validate_specs.py`: CI Spec-Validator (bidirektionale Traceability)
- `.github/workflows/ci.yml`: Validator läuft bei jedem Push
- `.github/workflows/release.yml`: CD-Pipeline für Baseline-Releases
- `docs/architecture/ADR-000-template.md`: ADR-Vorlage
- `.github/setup-labels.ps1`: CR-Labels für SUP.10
- `tests/conftest.py` + `pytest.ini`: Test-Infrastruktur

### Review
- `docs/review/2026-05-15_PROJ-SYS-001-007_review.md`: DONE, keine Abweichungen

---

<!--
Beispieleintrag:

## [v1.0] - YYYY-MM-DD

### Neue Anforderungen
- PROJ-BE-001: [Feature-Titel]
- PROJ-UI-001: [Feature-Titel]

### Geänderte Anforderungen
- PROJ-SYS-001: [Was wurde geändert]

### Obsolete Anforderungen
- keine
-->
