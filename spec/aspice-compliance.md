# ASPICE-Compliance – Prozessanforderungen

## Kontext

Die folgenden Nodes beschreiben Prozessanforderungen gemäß ASPICE für das SDD-Projekt-Template.
Der Normtext ist nicht abgedruckt (kommerzielle Lizenz – ASPICE PAM).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version projektspezifisch ein.

## SWE.1 – Software Requirements Analysis

### Software-Anforderungen werden systematisch erfasst und rückverfolgt

**UID**: PROJ-SYS-001 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.1, BP 1–8]

**Rationale**:

Der SDD-Workflow erfüllt SWE.1 durch:
- Spec-Dateien in `spec/` (StrictDoc-Markdown, maschinenauswertbar)
- Eindeutige UIDs (`PROJ-[CODE]-NNN`) für jeden Requirement-Node
- `@spec`-Annotationen in `src/` und `tests/` für bidirektionale Traceability
- GitHub Issues mit `needs-statement`-Template als formaler Eingangskanal
- Workflow-Phasen `spec-mode` und `plan-mode` strukturieren Erfassung und Ableitung

## SWE.2 – Software Architectural Design

### Software-Architektur wird dokumentiert und mit Anforderungen verknüpft

**UID**: PROJ-SYS-002 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.2, BP 1–7]

**Rationale**:

Der SDD-Workflow erfüllt SWE.2 durch:
- `docs/architecture/` als dedizierter Ordner für Architekturentscheidungen
- ADR-Template (`ADR-000-template.md`) für strukturierte Entscheidungsdokumentation
- `plan-mode`: Technischer Plan mit betroffenen Modulen, Abhängigkeiten und ADR-Anlage
- Plan Agent mit Edit-Zugriff auf `docs/architecture/` für direkte ADR-Erstellung
- `spec: PROJ-[CODE]-NNN`-Relations verknüpfen Architektur-Entscheidungen mit Requirements

## SWE.4 – Software Unit Verification

### Software-Units werden systematisch verifiziert und Ergebnisse nachvollziehbar dokumentiert

**UID**: PROJ-SYS-003 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.4, BP 1–6]

**Rationale**:

Der SDD-Workflow erfüllt SWE.4 durch:
- `pytest` als Test-Runner mit `pytest.ini`-Konfiguration
- `pytest-cov` für Code-Coverage (HTML + XML-Report)
- `allure-pytest` für strukturierte Test-Reports mit Requirement-Linking
- `conftest.py` registriert Custom-Marker `@pytest.mark.spec("PROJ-TC-NNN")`
- `test-mode` (TDD Red-Phase): Tests werden vor Implementierung geschrieben
- CD-Pipeline (`release.yml`) veröffentlicht Test-Reports als GitHub-Release-Artefakte

## SUP.1 – Quality Assurance

### Qualitätssicherung wird systematisch durchgeführt und dokumentiert

**UID**: PROJ-SYS-004 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.1, BP 1–6]

**Rationale**:

Der SDD-Workflow erfüllt SUP.1 durch:
- `review-mode`: strukturierter Review gegen Spec (AC-Abgleich, Traceability, State-of-the-Art, Security)
- Review-Dokumente in `docs/review/YYYY-MM-DD_[Spec-ID]_review.md`
- Review Agent prüft jeden AC, dokumentiert Abweichungen tabellarisch
- `review.instructions.md` definiert verpflichtende Prüfpunkte (OWASP, Lizenzkonflikt, State-of-the-Art)
- Keine Implementierung ohne vorherigen Review bei Abweichungen (`refactor-mode`)

## SUP.2 – Verification

### Spec-Abdeckung wird automatisch verifiziert und Lücken werden sichtbar gemacht

**UID**: PROJ-SYS-005 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.2, BP 1–5]

**Rationale**:

Der SDD-Workflow erfüllt SUP.2 durch:
- `scripts/validate_specs.py`: prüft bidirektionale Traceability
  - Alle aktiven Spec-UIDs in `spec/` müssen durch `@spec:`-Annotationen referenziert sein
  - Alle `@spec:`-Annotationen müssen auf existierende UIDs zeigen
- CI-Workflow (`.github/workflows/ci.yml`): läuft bei jedem Push, bricht mit Exit 1 bei Lücke
- `spec-mode` / `plan-mode` / `impl-mode` als Phasen-Gate: kein Code ohne Spec-ID
- `Spec-Gate` in `copilot-instructions.md`: Copilot verweigert Code ohne gültige Spec-ID

## SUP.8 – Configuration Management

### Baselines werden systematisch erstellt, freigegeben und als Artefakte veröffentlicht

**UID**: PROJ-SYS-006 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.8, BP 1–7]

**Rationale**:

Der SDD-Workflow erfüllt SUP.8 durch:
- Git-Tag `baseline/vX.Y` als unveränderlicher Baseline-Identifier
- `workflow.instructions.md` Phase 7 (baseline-mode): Checkliste, Naming-Konvention, Freigabeprozess
- `CHANGELOG.md` mit Spec-ID-Referenzen als Versionshistorie
- CD-Pipeline (`release.yml`): erzeugt GitHub Release mit Test-Report, Traceability-Matrix, StrictDoc-Export
- Pre-Release-Kennzeichnung automatisch aus Tag-Suffix (`-alpha.N` / `-beta.N`)
- Git-History + Spec-Dateien = vollständiger Audit-Trail

## SUP.10 – Change Request Management

### Änderungsanforderungen werden formal erfasst, bewertet, freigegeben und rückverfolgt

**UID**: PROJ-SYS-007 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.10, BP 1–5]

**Rationale**:

Der SDD-Workflow erfüllt SUP.10 durch:
- GitHub Issues mit `needs-statement`-Template als formaler CR-Eingangskanal
- CR-Status-Lifecycle via Labels: `cr-open` → `cr-assessed` → `cr-approved` → `cr-implemented`
- `setup-labels.ps1`: legt die 4 CR-Labels einmalig im Repository an
- Issue-Nummer wird in der Spec referenziert (`Rationale: GitHub: #NNN`)
- `spec-mode`: aus dem Issue wird eine formale Spec mit ACs abgeleitet
- `refactor-mode`: Feature-Drift oder Spec-Abweichungen starten neuen CR-Zyklus

## SWE.5 / SWE.6 – Integration and Qualification Testing

> Aktivierung: Copilot-Prompt `.github/prompts/activate-test-levels.prompt.md` ausführen.

### Software wird auf Integrations- und Qualifikationsebene systematisch getestet

**UID**: PROJ-SYS-008 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.5, BP 1–6] und [ASPICE PAM, SWE.6, BP 1–6]

**Rationale**:

Der SDD-Workflow bereitet SWE.5/6 durch folgende Infrastruktur vor:
- `tests/unit/`: Unit-Tests (Einzelfunktionen, kein I/O)
- `tests/integration/`: Integrationstests (Zusammenspiel von Modulen, externe Dienste gemockt)
- `tests/qualification/`: Qualifikationstests (End-to-End, gegen reale Umgebung)
- TC-Codes `TC-U` / `TC-I` / `TC-Q` für separate Traceability pro Testebene
- Aktivierung: `activate-test-levels.prompt.md` konfiguriert pytest.ini und CHANGELOG

Vollständige Aktivierung erfordert: pytest.ini-Erweiterung + separate Allure-Reporte + neue TC-Nodes.
