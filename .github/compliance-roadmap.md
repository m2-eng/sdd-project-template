# Compliance Roadmap – ASPICE / DO-X

Diese Datei listet sinnvolle nächste Schritte für eine formale Norm-Konformität.
Sie ist eine **Entscheidungshilfe**, kein verbindlicher Plan.
Jeder Eintrag beschreibt: Was, Warum, Aufwand (S/M/L).

---

## Aktueller Stand

Der SDD-Workflow deckt bereits ab:
- ✅ SWE.1 (Software Requirements): `spec/` mit StrictDoc + UID-Traceability
- ✅ SUP.1 (Quality Assurance – Reviews): Review-Dokumente in `docs/review/`
- ✅ SUP.10 (Change Request): Needs Statement Issue → formale Spec-Nodes
- ✅ Traceability: `@spec`-Annotationen in Code und Tests

---

## Offene Punkte

### 1 – Automatische Testreporte (SWE.4)
**Norm**: ASPICE SWE.4 / DO-178C Section 11 (Test Results)
**Status**: Tool gewählt – Konfiguration ausstehend

**Gewählter Stack:**
- `pytest` – Test-Runner
- `pytest-cov` – Code Coverage (XML + HTML)
- `allure-pytest` – HTML-Reports mit Requirement-Traceability via `@pytest.mark.spec('SCAN-TC-NNN')`
- Upgrade-Pfad: `mlx.traceability` (Melexis, Apache-2.0) wenn ASPICE-Audit nähert

**Nächste Schritte:**
1. `pip install pytest pytest-cov allure-pytest` → `requirements-dev.txt` anlegen
2. `conftest.py` mit `pytest.mark.spec`-Registrierung anlegen
3. `pytest.ini` oder `pyproject.toml` mit Coverage-Konfiguration anlegen
4. GitHub Actions Workflow: Test + Coverage + Allure Report als Artefakt
5. `docs/test-reports/` zur Ordnerstruktur und Zugriffsmatrix hinzufügen
**Aufwand**: S–M

---

### 2 – Architecture Decision Records (SWE.2)
**Norm**: ASPICE SWE.2 (Software Architecture) / DO-178C Section 11.10
**Was fehlt**: Architekturentscheidungen sind aktuell nur in Plan-Chats – nicht persistent
**Vorschlag**:
- `docs/architecture/ADR-NNN-titel.md` (Architecture Decision Records)
- plan-agent erhält `edit`-Zugriff auf `docs/architecture/`
- Lightweight ADR-Format: Kontext | Entscheidung | Konsequenzen
**Aufwand**: M (ADR-Format definieren, plan-agent erweitern)

---

### 3 – Traceability-Matrix Export (SWE.1 / SWE.4 / SUP.1)
**Norm**: ASPICE Traceability zwischen Requirements ↔ Tests ↔ Code
**Was fehlt**: Automatischer Export der Traceability-Matrix als Dokument
**Vorschlag**:
- StrictDoc kann HTML-Traceability-Matrix generieren (`strictdoc export .`)
- CI-Step einrichten: Matrix bei jedem Push generieren und als Artefakt sichern
- Output in `docs/traceability/`
**Aufwand**: S (StrictDoc läuft bereits, nur CI-Integration fehlt)

---

### 4 – CI Spec-Validator (SUP.2 – Verification)
**Norm**: ASPICE SUP.2 (Software Verification)
**Was fehlt**: Automatische Prüfung ob alle Spec-Nodes gültig sind (UID vorhanden, Status gesetzt)
**Vorschlag**:
- StrictDoc CLI in CI: `strictdoc passthrough .` prüft Syntax
- Eigener Validator: Python-Script prüft `@spec`-Annotationen gegen `spec/`-UIDs
**Aufwand**: M (CI-Pipeline + Validator-Script)

---

### 5 – Konfigurationsmanagement (SUP.8)
**Norm**: ASPICE SUP.8 (Configuration Management)
**Was fehlt**: Formale Baseline-Definition (welche Version der Spec gehört zu welchem Release)
**Vorschlag**:
- Git Tags als Baselines: `v1.0-baseline` entspricht einem freigegebenen Spec-Stand
- `CHANGELOG.md` mit Spec-ID-Referenzen
- `docs/baselines/` für freigegebene StrictDoc-Exports (PDF/HTML)
**Aufwand**: M (Prozess definieren, kein neues Tooling nötig)

---

### 6 – Integrations- und Qualifikationstests (SWE.5 / SWE.6)
**Norm**: ASPICE SWE.5 (Integration) / SWE.6 (Qualification)
**Was fehlt**: Separate Testebenen für Integration und System-Qualifikation
**Vorschlag**:
- `tests/unit/`, `tests/integration/`, `tests/qualification/` als Ordnerstruktur
- Separate TC-Codes: `TC-U`, `TC-I`, `TC-Q` (oder Subsystem-Codes erweitern)
- Separate Testreporte pro Ebene
**Aufwand**: L (Scope-Erweiterung, erfordert neue Spec-Nodes)

---

### 7 – GitHub Issues als formale Change Requests (SUP.10)
**Norm**: ASPICE SUP.10 (Change Request Management)
**Was fehlt**: Formaler CR-Status-Lifecycle im Issue (Offen → Bewertet → Genehmigt → Umgesetzt)
**Vorschlag**:
- GitHub Labels als CR-Status: `cr-open`, `cr-assessed`, `cr-approved`, `cr-implemented`
- GitHub Projects Board mit Spalten pro Status
- Needs Statement Issue wird nach spec-mode auf `cr-approved` gesetzt
**Aufwand**: S (Labels + Project Board konfigurieren)

---

## Empfohlene Reihenfolge

1. **Sofort (S)**: Testreporte (#1) + Traceability-Export (#3) + CR-Labels (#7)
2. **Nächste Iteration (M)**: ADR (#2) + CI-Validator (#4)
3. **Später (L)**: Konfigurationsmanagement (#5) + Testebenen (#6)
