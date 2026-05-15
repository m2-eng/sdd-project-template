# Compliance Roadmap – ASPICE / DO-X

Diese Datei listet sinnvolle nächste Schritte für eine formale Norm-Konformität.
Sie ist eine **Entscheidungshilfe**, kein verbindlicher Plan.
Jeder Eintrag beschreibt: Was, Warum, Aufwand (S/M/L).

---

## Aktueller Stand

Der SDD-Workflow deckt bereits ab:
- ✅ SWE.1 (Software Requirements): `spec/` mit StrictDoc + UID-Traceability
- ✅ SWE.2 (Architecture): `docs/architecture/` + ADR-Vorlage + plan-agent mit Edit-Zugriff
- ✅ SWE.4 (Test Results – lokal): `conftest.py` + `pytest.ini` – Report-Veröffentlichung via CD-Pipeline
- ✅ SWE.4 / SUP.8 / SWE.1 (CD-Pipeline): `.github/workflows/release.yml` – Trigger `git tag baseline/vX.Y` → GitHub Release mit Test-Report, Traceability-Matrix und Baseline-Artefakten
- ✅ SUP.1 (Quality Assurance – Reviews): Review-Dokumente in `docs/review/`
- ✅ SUP.8 (Konfigurationsmanagement): Baseline-Prozess definiert (`workflow.instructions.md` Phase 7) + CHANGELOG + CD-Pipeline für Artefakte
- ✅ SUP.10 (Change Request Management): Needs Statement Issue-Template + CR-Labels via `setup-labels.ps1`
- ✅ Traceability: `@spec`-Annotationen in Code und Tests

---

## Offene Punkte

### 1 – CI Spec-Validator (SUP.2 – Verification)
**Norm**: ASPICE SUP.2 (Software Verification)
**Was fehlt**: Automatische Prüfung ob alle aktiven Spec-UIDs durch `@spec`-Annotationen abgedeckt sind
**Vorschlag**:
- `scripts/validate_specs.py`: prüft `@spec`-Annotationen gegen UIDs in `spec/`
- CI-Workflow (`ci.yml`): läuft bei jedem Push, bricht mit Exit 1 bei Lücke
**Aufwand**: M

---

### 2 – Integrations- und Qualifikationstests (SWE.5 / SWE.6)
**Norm**: ASPICE SWE.5 (Integration) / SWE.6 (Qualification)
**Was fehlt**: Separate Testebenen für Integration und System-Qualifikation
**Vorschlag**:
- `tests/unit/`, `tests/integration/`, `tests/qualification/` als Ordnerstruktur
- Separate TC-Codes: `TC-U`, `TC-I`, `TC-Q` (oder Subsystem-Codes erweitern)
- Separate Testreporte pro Ebene
**Aufwand**: L (Scope-Erweiterung, erfordert neue Spec-Nodes)

---

## Empfohlene Reihenfolge

1. **Nächste Iteration (M)**: CI Spec-Validator (#1)
2. **Später (L)**: Testebenen (#2)
