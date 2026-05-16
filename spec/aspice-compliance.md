# ASPICE-Compliance – Prozessanforderungen

## Kontext

Die folgenden Nodes beschreiben Prozessanforderungen gemäß ASPICE für das SDD-Projekt-Template.
Der Normtext ist nicht abgedruckt (kommerzielle Lizenz – ASPICE PAM).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version projektspezifisch ein.

## SWE.1 – Software Requirements Analysis

### Software-Anforderungen werden systematisch erfasst und rückverfolgt

**UID**: PROJ-SYS-001 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.1, BP 1–8]

**Rationale**:

Der SDD-Workflow erfüllt SWE.1 durch:
- Spec-Dateien in `spec/` (StrictDoc-Markdown, maschinenauswertbar)
- Eindeutige UIDs (`PROJ-[CODE]-NNN`) für jeden Requirement-Node
- `@spec`-Annotationen in `src/` und `tests/` für bidirektionale Traceability
- GitHub Issues mit `needs-statement`-Template als formaler Eingangskanal
- Workflow-Phasen `spec-mode` und `plan-mode` strukturieren Erfassung und Ableitung
- `specification.instructions.md` Abschnitt 2 definiert das kanonische `@spec:`-Annotationsformat; alle anderen Instruction-Dateien verweisen nur darauf

## SWE.2 – Software Architectural Design

### Software-Architektur wird dokumentiert und mit Anforderungen verknüpft

**UID**: PROJ-SYS-002 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.2, BP 1–7]

**Rationale**:

Der SDD-Workflow erfüllt SWE.2 durch:
- `docs/architecture/` als dedizierter Ordner für Architekturentscheidungen
- ADR-Template (`ADR-000-template.md`) für strukturierte Entscheidungsdokumentation
- `plan-mode`: Technischer Plan mit betroffenen Modulen, Abhängigkeiten und ADR-Anlage
- Plan Agent mit Edit-Zugriff auf `docs/architecture/` für direkte ADR-Erstellung
- `spec: PROJ-[CODE]-NNN`-Relations verknüpfen Architektur-Entscheidungen mit Requirements

## SWE.3 – Software Detailed Design and Unit Construction

### Software-Detaildesign wird erstellt, dokumentiert und mit der Architektur verknüpft

**UID**: PROJ-SYS-009 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.3, BP 1–7]

**Rationale**:

Der SDD-Workflow adressiert SWE.3 teilweise durch:
- `plan-mode` (Phase 2): Technischer Plan identifiziert betroffene Module, Dateien und Funktionsschnittstellen
- `docs/architecture/` mit `ADR-000-template.md`: Ablageort für entwurfsbezogene Entscheidungen auf Unit-Ebene
- Spec-Nodes mit `**Relations**:`-Verknüpfungen: bidirektionale Traceability von Detaildesign-Entscheidungen zu Systemanforderungen

Vollständige SWE.3-Abdeckung erfordert zusätzlich (für Projekte mit ASPICE Level 3+ Anforderungen):
- Erweiterung `plan-mode` um expliziten Schritt für Unit Interface-Beschreibungen (SWE.3 BP 2)
- Subsystem-Code `DD` (Detailed Design) in `specification.instructions.md` Abschnitt 7 für Interface-Spec-Nodes
- Formaler Verifikationsschritt in `review-mode`: Detaildesign gegen Architektur prüfen (SWE.3 BP 3)

## SWE.4 – Software Unit Verification

### Software-Units werden systematisch verifiziert und Ergebnisse nachvollziehbar dokumentiert

**UID**: PROJ-SYS-003 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.4, BP 1–6]

**Rationale**:

Der SDD-Workflow erfüllt SWE.4 durch:
- `pytest` als Test-Runner mit `pytest.ini`-Konfiguration
- `pytest-cov` für Code-Coverage (HTML + XML-Report)
- `allure-pytest` für strukturierte Test-Reports mit Requirement-Linking
- `conftest.py` registriert Custom-Marker `@pytest.mark.spec("PROJ-TC-NNN")`
- `test-mode` (TDD Red-Phase): Tests werden vor Implementierung geschrieben
- CD-Pipeline (`release.yml`) veröffentlicht Test-Reports als GitHub-Release-Artefakte

Template-Robustheit im Initialzustand (GitHub: #3):
- `release.yml` muss auch dann erfolgreich durchlaufen, wenn `tests/` ausschließlich README-Dateien enthält (keine Testfunktionen vorhanden)
- Exit Code 5 von pytest (keine Tests gesammelt) darf den Release-Prozess nicht abbrechen
- Fehlende Artefakte im Initialzustand (`coverage.xml`, leeres `allure-results/`) dürfen den Release-Schritt nicht blockieren
- Externe Tools in der Pipeline werden mit fixierter Version installiert (Supply-Chain-Schutz gemäß OWASP A08)

## SUP.1 – Quality Assurance

### Qualitätssicherung wird systematisch durchgeführt und dokumentiert

**UID**: PROJ-SYS-004 \
**Status**: Draft

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
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.2, BP 1–5]

**Rationale**:

Der SDD-Workflow erfüllt SUP.2 durch:
- `scripts/validate_specs.py`: prüft bidirektionale Traceability
  - Alle aktiven Spec-UIDs in `spec/` müssen durch `@spec:`-Annotationen referenziert sein
  - Alle `@spec:`-Annotationen müssen auf existierende UIDs zeigen
- CI-Workflow (`.github/workflows/ci.yml`): läuft bei jedem Push, bricht mit Exit 1 bei Lücke
- `spec-mode` / `plan-mode` / `impl-mode` als Phasen-Gate: kein Code ohne Spec-ID
- `Spec-Gate` in `copilot-instructions.md`: Copilot verweigert Code ohne gültige Spec-ID

## SUP.4 – Joint Review

### Joint Reviews werden systematisch durchgeführt und Ergebnisse persistiert

**UID**: PROJ-SYS-011 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.4, BP 1–6]

**Rationale**:

Der SDD-Workflow adressiert SUP.4 durch:
- `review-mode` (Phase 5): strukturierter Review gegen Spec mit dokumentierten Abweichungen
- Review-Dokumente in `docs/review/YYYY-MM-DD_[Spec-ID]_review.md` als persistente Aufzeichnung
- `refactor-mode` (Phase 6): Abweichungen führen zu Spec-Änderungsvorschlägen mit User-Bestätigung
- Konkrete Ablage- und Commit-Strategie: PROJ-SYS-010

### Review-Dokumente werden persistent committed und als Baseline-Artefakt veröffentlicht

**UID**: PROJ-SYS-010 \
**Status**: Active \
**Relations**: PROJ-SYS-011

**Statement**:

Given ein Review-Bericht im `review-mode` unter
`docs/review/YYYY-MM-DD_[Spec-ID]_review.md` erstellt wurde,
When eine neue Baseline (`baseline/vX.Y`) veröffentlicht wird,
Then sind alle bis dahin erstellten Review-Dokumente aus `docs/review/` im
Repository committed und als ZIP-Archiv `review-reports-vX.Y.zip` dem
zugehörigen GitHub Release angehängt, sodass Review-Ergebnisse dauerhaft
rückverfolgbar und dem Baseline-Artefakt-Set explizit zugeordnet sind.

**Rationale**:

ASPICE erfordert persistente, rückverfolgbare Review-Aufzeichnungen:
- SUP.1 BP 4/5: QA-Aufzeichnungen müssen zugänglich und rückverfolgbar sein
- SUP.4 BP 1/4: Joint-Review-Ergebnisse müssen persistiert werden, Abweichungen nachvollziehbar
- SUP.8: Qualitätsnachweise gehören zum Baseline-Artefakt-Set (Querref. PROJ-SYS-006)

Entscheidung für Option A + C (GitHub: #5):
- Option A (committed): Einfachste ASPICE-konforme Grundlage; Review-Dateien sind
  direkt in der Git-History nachvollziehbar; keine Zusatzkomplexität
- Option C (Release-Artefakt): `release.yml` liest `docs/review/*.md`, zipt sie
  im CI-Runner und hängt `review-reports-vX.Y.zip` als Asset an den GitHub Release
  an – kein zusätzlicher Commit erforderlich
- Optionen B, D, E, F, G verworfen: B verletzt SUP.1/SUP.4; D/E/F/G erzeugen
  Traceability-Lücken oder unverhältnismäßigen Mehraufwand

Manuelle Pre-Release-Schritte (CHANGELOG, Versionsnummer, Spec-Status) werden
durch ein dediziertes Release-Preparation-Issue-Template abgedeckt (GitHub: #6).

## SUP.8 – Configuration Management

### Baselines werden systematisch erstellt, freigegeben und als Artefakte veröffentlicht

**UID**: PROJ-SYS-006 \
**Status**: Draft

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
**Status**: Draft

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
- Pytest-Marker-Texte enthalten ASPICE-Prozessreferenzen als Konvention; für Projekte mit anderem Prozessrahmen (ISO 26262, DO-178C, ISO 9001) sind Marker-Texte in `pytest.ini` und `conftest.py` projektspezifisch ohne Norm-Verweis zu formulieren

## Test Cases – Release Pipeline Robustheit

### pytest gibt Exit Code 5 zurück wenn keine Tests vorhanden

**UID**: PROJ-TC-001 \
**Status**: Active \
**Relations**: PROJ-SYS-003

**Statement**:

Given ein leeres Testverzeichnis ohne Testfunktionen existiert,
When pytest mit `--collect-only` auf dieses Verzeichnis ausgeführt wird,
Then gibt pytest Exit Code 5 zurück (keine Tests gesammelt).

**Rationale**:

Dokumentiert das bekannte pytest-Verhalten bei leerem `tests/`-Verzeichnis
(Initialzustand des Templates). Grundlage für TC-005 (Pipeline-seitige Behandlung).

### release.yml enthält Guard für leeres allure-results-Verzeichnis

**UID**: PROJ-TC-002 \
**Status**: Active \
**Relations**: PROJ-SYS-003

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert,
When der Inhalt auf den Step „Generate Allure report" geprüft wird,
Then enthält der Step einen Guard der prüft ob `allure-results/` nicht leer ist
(erwartet: `ls -A`-Aufruf als Existenzprüfung).

**Rationale**:

Verhindert, dass `allure generate` auf ein leeres Verzeichnis angewendet wird
und den Release-Prozess abbricht (GitHub Issue #3, AC-3).

### release.yml übergibt coverage.xml konditional an gh release create

**UID**: PROJ-TC-003 \
**Status**: Active \
**Relations**: PROJ-SYS-003

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert,
When der Inhalt auf den Step „Create GitHub Release" geprüft wird,
Then enthält der Step eine `[ -f ... coverage.xml ]`-Existenzprüfung vor der Übergabe
an `gh release create`.

**Rationale**:

Im Initialzustand erzeugt pytest keine `coverage.xml`. Ein unbedingter
Upload bricht den Release-Step mit Fehler ab (GitHub Issue #3, AC-3).

### release.yml installiert allure-commandline mit expliziter Versionsnummer

**UID**: PROJ-TC-004 \
**Status**: Active \
**Relations**: PROJ-SYS-003

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert,
When der Inhalt auf den Step „Install Allure CLI" geprüft wird,
Then enthält der `npm install`-Befehl einen Versions-Pin der Form `allure-commandline@X.Y.Z`.

**Rationale**:

Unpinned `npm install -g allure-commandline` kann durch Breaking Changes
in neuen Versionen die Pipeline ohne Vorwarnung brechen (Supply-Chain-Schutz, OWASP A08,
GitHub Issue #3, AC-4).

### release.yml behandelt Exit Code 5 von pytest explizit

**UID**: PROJ-TC-005 \
**Status**: Active \
**Relations**: PROJ-SYS-003

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert,
When der Inhalt auf den Step „Run tests" geprüft wird,
Then enthält der Step den Ausdruck `$? -eq 5` zur expliziten Behandlung von
pytest Exit Code 5 (keine Tests gesammelt).

**Rationale**:

Exit Code 5 bedeutet „keine Tests gesammelt" und ist im Initialzustand
des Templates der Normalfall. Ohne explizite Behandlung bricht der `run: python -m pytest`
Step die Pipeline ab (GitHub Issue #3, AC-2).

### release.yml enthält ZIP-Schritt für Review-Berichte

**UID**: PROJ-TC-006 \
**Status**: Active \
**Relations**: PROJ-SYS-010

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert und PROJ-SYS-010 implementiert ist,
When der Dateiinhalt gelesen wird,
Then enthält er einen `zip`-Befehl der Dateien aus `docs/review/` in ein Archiv
mit dem Namensmuster `review-reports-` packt.

**Rationale**:

PROJ-SYS-010 fordert dass Review-Berichte als ZIP-Anhang beim GitHub Release bereitgestellt werden.
Der ZIP-Schritt in `release.yml` ist die technische Umsetzung dieser Anforderung.

### release.yml bricht nicht ab wenn docs/review leer ist

**UID**: PROJ-TC-007 \
**Status**: Active \
**Relations**: PROJ-SYS-010

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert,
When der Dateiinhalt gelesen wird,
Then enthält er einen Guard der sicherstellt dass ein leeres `docs/review/`-Verzeichnis
keinen Fehler verursacht (find-basierte Prüfung mit `find docs/review`).

**Rationale**:

Ohne Guard schlägt `zip -j review-reports-*.zip docs/review/*.md` fehl wenn
`docs/review/` leer ist – der Glob expandiert nicht und bricht den Step ab.

### ZIP-Dateiname enthält versionierten review-reports-Präfix

**UID**: PROJ-TC-008 \
**Status**: Active \
**Relations**: PROJ-SYS-010

**Statement**:

Given die Datei `.github/workflows/release.yml` existiert,
When der Dateiinhalt gelesen wird,
Then referenziert der ZIP-Dateiname die Tag-Variable und beginnt mit `review-reports-`.

**Rationale**:

Der versionierte Dateiname ermöglicht die eindeutige Zuordnung des ZIP-Archivs
zur jeweiligen Release-Version (z.B. `review-reports-v1.0.zip`).
