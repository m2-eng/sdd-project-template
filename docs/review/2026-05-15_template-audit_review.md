# Template-Audit: Widersprüche, SSOT, Compliance, Erweiterbarkeit

**Datum**: 2026-05-15
**Reviewer**: GitHub Copilot (review-mode)
**Scope**: Vollständiger Audit des SDD-Project-Templates – Instruction-Dateien, Workflow, Compliance-Specs, Erweiterbarkeit

---

## 1 – Widersprüche & Ungenauigkeiten

| Datei:Zeile | Befund | Empfehlung |
|-------------|--------|------------|
| `project.config.md:4` | Referenz auf `.github/instructions/sdd.setup.md` – diese Datei existiert nicht. `SETUP.md` liegt im Root, nicht unter `.github/instructions/`. | Referenz korrigieren zu `SETUP.md` |
| `SETUP.md:15–17` | Widerspruch in derselben Datei: "Die **einzige Datei**, die pro Projekt angepasst werden muss: `.github/project.config.md`" – wenige Zeilen später (Abschnitt 2) wird explizit `strictdoc_config.py` als weitere Pflichtanpassung beschrieben. | Formulierung ändern: "Hauptkonfiguration" statt "einzige Datei", oder `strictdoc_config.py`-Änderung in `project.config.md` automatisieren. |
| `scripts/validate_specs.py:191–196` | Funktionaler Bug: `--include-draft` ist mit `action="store_true"` und `default=True` definiert. Das Flag hat dadurch keine Wirkung – der Wert ist immer `True`. Es gibt keinen Mechanismus, Draft-Nodes auszuschließen. | `default=False` setzen (Standardverhalten: Draft wird nicht geprüft) oder Flag in `--exclude-draft` mit `action="store_true", default=False` umbenennen. |
| `.github/workflows/ci.yml:23` | `pip install -r requirements-dev.txt` ohne `.venv`. `impl.instructions.md` fordert absolut: "Alle Packages werden ausschließlich in `.venv` installiert – **nie global**". In GitHub Actions-Runners existiert keine `.venv` – die Regel gilt also nicht für CI, ist aber ohne Ausnahme formuliert. | `impl.instructions.md` um Ausnahme ergänzen: "Ausnahme: CI/CD-Runner (GitHub Actions) – dort entfällt die venv-Pflicht." |
| `.github/workflows/release.yml:24` | Gleiches Problem: `pip install` ohne `.venv` in Release-Pipeline. | Wie oben. |
| `spec/aspice-compliance.md` – alle 7 Active-Nodes | Status ist `Active`, aber alle `**Statement**:`-Felder enthalten nur Platzhalter (`TODO – Normtext hier einfügen`). `specification.instructions.md` Abschnitt 9 definiert als Quality-Gate für `Active`: "Alle Statements messbar formuliert (Given/When/Then)". Platzhalter-Statements erfüllen dieses Gate nicht. | Entweder Status auf `Draft` zurücksetzen (bis Normtext eingepflegt) oder in `specification.instructions.md` eine Ausnahmeregelung für Compliance-Stubs mit Normtext-Verweis dokumentieren. |
| `plan.instructions.md:1` (applyTo) | `applyTo: "spec/**"` – aber Plan-Richtlinien gelten für plan-mode, der primär Dateien in `docs/architecture/` und den gesamten Codebase liest/schreibt, nicht nur `spec/`. | `applyTo` auf `**` oder `docs/architecture/**` erweitern. |
| `activate-test-levels.prompt.md:31–33` | Der Prompt instruiert, `PROJ-SYS-008` auf `Active` zu setzen, ohne das Statement-Gate zu erwähnen. Da SWE.5/6 Normtext ebenfalls ein Platzhalter ist, entsteht dieselbe Gate-Verletzung wie oben. | Hinweis ergänzen: Statement-Platzhalter vor Status-Änderung befüllen. |
| `test.instructions.md` (Red-Phase-Abschnitt, letzte Zeile) | Abschnitt "Red-Phase" ist unvollständig – nur eine Zeile ohne Inhalt: `Tests müssen initial **fehlschlagen**. Kein Produktionscode in Testdateien.` Es fehlt Anleitung, wie die Red-Phase verifiziert wird (z.B. Befehl zum isolierten Test-Run). | Abschnitt um konkreten Pytest-Befehl ergänzen: `pytest tests/ --no-cov` um Red-Phase zu verifizieren. |
| `workflow.instructions.md` Phase 3 (test-mode) | "Alle Tests müssen zunächst fehlschlagen (Red-Phase)" – aber `pytest.ini` hat `addopts = --cov=src ...` als Standard. Ein leeres `src/` erzeugt beim ersten pytest-Run eine Coverage-Warnung, die den Red-Phase-Nachweis unübersichtlich macht. | `pytest.ini`-Hinweis in test-mode ergänzen oder separate pytest-Konfiguration für Red-Phase. |

---

## 2 – SSOT-Verletzungen

| Information | Fundstelle A | Fundstelle B | Empfehlung |
|-------------|-------------|-------------|------------|
| **Annotationsformat** `@spec: PROJ-[CODE]-NNN` | `workflow.instructions.md` – Abschnitt "Annotationsformat (alle Modi)" | `impl.instructions.md` – Abschnitt "Traceability" + `test.instructions.md` – Abschnitt "Annotationsformat" + `copilot-instructions.md` – Abschnitt "Traceability" | Eine kanonische Definition in `specification.instructions.md` Abschnitt 2, alle anderen Stellen per Verweis. Aktuell 4 eigenständige Erklärungen. |
| **Spec-Gate-Regel** | `copilot-instructions.md`: "Generiere niemals Code ohne eine gültige Spec-ID. Fehlt eine passende Spezifikation: stoppe und weise explizit darauf hin." | `workflow.instructions.md`: "Spec-Gate (immer aktiv, in allen Modi)" – nahezu identischer Text | Eine SSOT in `workflow.instructions.md`, `copilot-instructions.md` nur Verweis. |
| **DON'T DO: Nie UIDs erfinden** | `copilot-instructions.md`: "Nie UIDs erfinden – IDs immer aus `project.config.md` entnehmen" | `.github/agents/spec-agent.agent.md`: "Erfinde KEINE UIDs – immer aus `project.config.md` ablesen" | SSOT in `copilot-instructions.md`, agent-Datei verweist darauf. |
| **DON'T DO: Keine Architekturentscheidungen stillschweigend** | `copilot-instructions.md`: "Nie Architekturentscheidungen stillschweigend treffen" | `.github/agents/plan-agent.agent.md`: "Keine Architekturentscheidungen ohne Rückfrage treffen" | SSOT in `copilot-instructions.md`, agent-Datei verweist darauf. |
| **ASPICE-Prozess → Spec-ID-Mapping** | `SETUP.md` Abschnitt 7: Tabelle mit ASPICE-Prozess → Spec-UID | `spec/aspice-compliance.md`: Rationale-Felder beschreiben dieselbe Zuordnung | `SETUP.md`-Tabelle als "Schnellübersicht" kennzeichnen und auf `aspice-compliance.md` als SSOT verweisen. Bei neuem Prozess: zwei Stellen aktualisieren nötig. |
| **Tooling-Entscheidungen** | `project.config.md` – Abschnitt "Tooling-Entscheidungen" (vollständige Tabelle) | `SETUP.md` – Abschnitt 3 enthält redundante Tooling-Infos (pytest-Befehle, strictdoc-Aufruf) inline | `project.config.md` als SSOT beibehalten, `SETUP.md` verweist nur noch auf spezifische Abschnitte. |
| **Phasenbeschreibungen** | `workflow.instructions.md`: vollständige 7-Phasen-Beschreibung inkl. Vorgehen | Jede `*.agent.md`-Datei: wiederholt Vorgehen der eigenen Phase | Agent-Dateien nur mit Constraints und Stopp-Bedingungen; Hauptvorgehen in `workflow.instructions.md` als SSOT. |

---

## 3 – Compliance-Lücken

### 3.1 ASPICE PAM 3.1

| ASPICE-Prozess | BP | Status | Lücke / Empfehlung |
|---------------|-----|--------|-------------------|
| **SWE.1** – Requirements Analysis | BP 1–4 (Erhebung, Analyse, Priorisierung, Traceability) | ✅ Abgedeckt | `spec/`, StrictDoc, `spec-mode`, UID-Traceability |
| **SWE.1** – BP 5 | Notifikation bei Anforderungsänderungen | ⚠️ Teilweise | CR-Labels decken Änderungs-Workflow ab (SUP.10), aber kein expliziter Stakeholder-Notifikationsprozess |
| **SWE.2** – Architecture Design | BP 1–5 | ✅ Abgedeckt | ADR-Template, `docs/architecture/`, plan-mode |
| **SWE.2** – BP 6 | Bidirektionale Traceability Anforderungen ↔ Architektur | ⚠️ Teilweise | StrictDoc zeigt Relations, aber ADR-Dokumente haben keine maschinenauswertbare Verknüpfung zu Spec-Nodes |
| **SWE.3** – Detailed Design & Unit Construction | BP 1–6 (Unit-Level Design, Interfaces, Datenstrukturen) | ❌ Fehlt | Kein Spec-Node, kein Workflow-Schritt für Detailed Design. ADRs decken nur Architektur-Ebene. Es fehlen Unit-Interface-Specs. Empfehlung: `PROJ-SYS-009` (SWE.3) anlegen, Subsystem-Code `DD` (Detailed Design) ergänzen. |
| **SWE.4** – Unit Verification | BP 1–6 | ✅ Abgedeckt | pytest, pytest-cov, allure-pytest, test-mode |
| **SWE.5** – Integration Testing | BP 1–6 | ⚠️ Draft | `PROJ-SYS-008` Status: Draft, `tests/integration/` vorbereitet, aber kein aktiver Prozess |
| **SWE.6** – Qualification Testing | BP 1–6 | ⚠️ Draft | Wie SWE.5 |
| **SUP.1** – Quality Assurance | BP 1–6 | ✅ Abgedeckt | review-mode, Review Agent, review.instructions.md |
| **SUP.1** – BP 4 | QS-Unabhängigkeit | ❌ Lücke | Der Review Agent (KI) kann nicht als unabhängiger Reviewer gemäß ASPICE gelten. Kein Menschlicher Reviewer / Sign-off vorgesehen. Empfehlung: Menschliche Review-Bestätigung als Pflichtschritt in workflow.instructions.md |
| **SUP.2** – Verification | BP 1–5 | ✅ Abgedeckt | validate_specs.py, ci.yml |
| **SUP.4** – Joint Review | BP 1–4 | ❌ Fehlt | Kein formaler Peer-Review-Prozess mit mehreren Parteien, kein Sign-off, kein formaler Review-Request-Mechanismus. Empfehlung: GitHub Pull-Request als Joint-Review-Gate integrieren. |
| **SUP.7** – Documentation | BP 1–5 | ❌ Fehlt | Kein Spec-Node, kein dedizierter Dokumentenmanagement-Prozess. SETUP.md und README decken nur Template-Einführung. |
| **SUP.8** – Configuration Management | BP 1–7 | ✅ Abgedeckt | Git-Tags, CHANGELOG.md, baseline-mode |
| **SUP.9** – Problem Resolution Management | BP 1–6 | ❌ Fehlt | GitHub Issues + CR-Labels decken SUP.10 (Change Requests), aber kein dedizierter Defect-/Problem-Workflow. Kein Problem-Schweregrad, kein Eskalationspfad. |
| **SUP.10** – Change Request Management | BP 1–5 | ✅ Abgedeckt | needs-statement Template, CR-Labels, spec-mode |
| **MAN.3** – Project Management | BP 1–7 | ❌ Außerhalb Scope | Kein Projektplan, keine Ressourcenplanung. Für vollständige ASPICE-Konformität erforderlich, aber außerhalb eines reinen Dev-Templates. |
| **MAN.5** – Risk Management | BP 1–5 | ❌ Fehlt | Risiken werden in plan-mode als "offene Entscheidungen" erwähnt (plan-agent.agent.md), aber kein formaler Risikokatalog, keine Risikobewertung (Wahrscheinlichkeit × Auswirkung), kein Risikoregister. |

### 3.2 ISO 9001:2015

| ISO 9001 Abschnitt | Anforderung | Status | Lücke / Empfehlung |
|--------------------|------------|--------|-------------------|
| 4.4 – QMS-Prozesse | Prozesse, Verantwortliche, Schnittstellen | ⚠️ Teilweise | Prozesse dokumentiert (workflow.instructions.md), aber keine Verantwortlichkeitszuordnung (wer = welche Rolle?) |
| 6.1 – Risiken & Chancen | Risikobasiertes Denken | ❌ Fehlt | Kein Risikomanagement-Prozess (siehe auch MAN.5) |
| 7.2 – Kompetenz | Kompetenzanforderungen, Nachweise | ❌ Fehlt | Keine Rollenanforderungen, keine Kompetenz-Kriterien für Reviewer oder Tester |
| 7.5 – Dokumentierte Information | Lenkung von Dokumenten, Versionen | ⚠️ Teilweise | Spec-Dateien versioniert via Git, aber keine Dokumentenliste, kein Freigabe-Workflow für Dokumente |
| 8.3 – Design & Entwicklung | Entwicklungssteuerung, -validierung | ✅ Abgedeckt | SDD-Workflow deckt Design-Input (spec-mode), Design-Output (impl-mode), Design-Review (review-mode) ab |
| 9.1 – Überwachung & Messung | Metriken, KPIs | ⚠️ Teilweise | Code Coverage (pytest-cov) ist einzige Metrik. Fehlende KPIs: Spec-Abdeckungsgrad, Defect-Rate, Review-Durchlaufzeit |
| 10.3 – Fortlaufende Verbesserung | PDCA-Zyklus | ⚠️ Teilweise | refactor-mode adressiert Korrekturen nach Review, aber kein formaler PDCA/KVP-Prozess, kein Lessons-Learned-Format |

### 3.3 DO-178C (Hinweis: nur relevant wenn explizit angesteuert)

| DO-178C Bereich | Anforderung | Status | Lücke / Empfehlung |
|-----------------|------------|--------|-------------------|
| Planungsdokumente | SDP, SVP, SCMP, SQAP | ❌ Fehlt | Keine formalen Plandokumente. Für DAL A/B/C Pflicht. Workflow-Dokumente sind kein Ersatz. |
| Coverage-Kriterien | MC/DC Coverage (DAL A), Decision Coverage (DAL B) | ❌ Fehlt | pytest-cov erzeugt nur Line/Branch-Coverage. Kein MC/DC. |
| Review-Unabhängigkeit | Unabhängige Verifikation (DER) | ❌ Fehlt | AI-Review nicht als unabhängig anerkennbar; kein menschlicher Reviewer vorgeschrieben |
| Konfigurationsmanagement | Part Number, Problem Report Lifecycle | ⚠️ Teilweise | Git-Tags als Baseline-IDs, aber kein DO-178C-konformes Part-Number-Schema |
| Traceability | Requirements → Design → Code → Tests (bidirektional) | ✅ Gut vorbereitet | StrictDoc + @spec-Annotationen decken die Kette gut ab |

---

## 4 – Erweiterbarkeit: Neuen Prozessrahmen einpflegen

### 4.1 Stellen mit ASPICE-Hardcoding (Generalisierungsbedarf)

| Datei:Zeile | ASPICE-hardcodierter Inhalt | Generalisierungsempfehlung |
|-------------|----------------------------|---------------------------|
| `.github/prompts/activate-test-levels.prompt.md:10–12` | Pytest-Marker: `unit: Unit-Test (ASPICE SWE.4)`, `integration: Integrationstest (ASPICE SWE.5)` | Marker ohne ASPICE-Verweis formulieren: `unit: Unit-Test`, `integration: Integrationstest`. Standard-Dokumentation referenziert den Norm-Kontext |
| `spec/aspice-compliance.md` | Komplett ASPICE-spezifisch | Ordner `spec/compliance/` einführen; für jeden Standard eine eigene Datei: `aspice-compliance.md`, `iso26262-compliance.md`, etc. |
| `SETUP.md:143–152` | "ASPICE-Compliance-Übersicht" Tabelle | Abschnitt verallgemeinern: "Compliance-Übersicht" mit Verweis auf jeweilige compliance-Dateien |
| `tests/conftest.py` (nach activate-prompt) | Marker mit ASPICE-Bezug | Marker-Texte generisch halten |

### 4.2 Bereits gut vorbereitet für Erweiterbarkeit

- **Subsystem-Code `SAF`** (`specification.instructions.md` Abschnitt 7): Bereits für Safety-Anforderungen (ISO 26262: ASIL-Anforderungen) reserviert
- **`project.config.md`-Struktur**: Erweiterbar um neue SYS-Nummern ohne Format-Änderung
- **ADR-Template**: Prozessunabhängig formuliert
- **StrictDoc Relations**: Funktionieren mit beliebigen UID-Schemata
- **review.instructions.md**: Generisch formuliert, bereits OWASP + Lizenz + State-of-the-Art

### 4.3 Schritt-für-Schritt: ISO 26262 einpflegen (Beispiel)

**Voraussetzung**: Lizenzierte ISO 26262-Norm vorhanden.

#### Schritt 1 – Neue Compliance-Spec-Datei anlegen

Datei: `spec/PROJ-SYS-009-iso26262-compliance.md`

Enthält Nodes für ISO 26262 Part 6 (Software):
- PROJ-SYS-009: Part 6 Clause 5 (Software development)
- PROJ-SYS-010: Part 6 Clause 6 (SW architectural design)
- PROJ-SYS-011: Part 6 Clause 9 (SW unit testing)
- PROJ-SYS-012: Part 6 Clause 10 (SW integration and testing)

#### Schritt 2 – ID-Zähler in `project.config.md` aktualisieren

```markdown
| `SYS` | `PROJ-SYS-013`  ←  nach den neuen ISO-26262-Nodes
```

#### Schritt 3 – Subsystem-Codes bei Bedarf erweitern

In `specification.instructions.md` Abschnitt 7 ergänzen:

```markdown
| `ASIL` | ASIL-Anforderungen (ISO 26262) | Safety-Anforderungen mit ASIL-Einstufung A–D |
| `HW`   | Hardware-Anforderungen          | Falls HW-SW-Interface relevant (ISO 26262 Part 4) |
```

Hinweis: `SAF` ist bereits vorhanden und kann für ISO 26262 Safety Goals verwendet werden.

#### Schritt 4 – pytest-Marker generalisieren

In `activate-test-levels.prompt.md` und `tests/conftest.py` Marker ohne ASPICE-Bezeichnung:

```python
config.addinivalue_line("markers", "unit: Unit-Test")
config.addinivalue_line("markers", "integration: Integration Test")
config.addinivalue_line("markers", "qualification: System Test / Qualification Test")
```

#### Schritt 5 – SETUP.md Compliance-Übersicht erweitern

Abschnitt 7 in `SETUP.md` umbenennen in "Compliance-Übersicht" und Tabelle um ISO 26262 ergänzen:

```markdown
| ISO 26262 Part 6 Clause 5–10 | `PROJ-SYS-009..012` | Spec-Dateien, pytest, StrictDoc, review-mode |
```

#### Schritt 6 – Optional: Separate Compliance-Checkliste in `review.instructions.md`

Für Zertifizierungsaudits einen neuen Abschnitt "6 – Norm-spezifische Checklisten" anlegen:

```markdown
## 6 – ISO 26262 Checkliste (aktivieren wenn relevant)
- [ ] ASIL-Einstufung für alle Safety Requirements dokumentiert?
- [ ] ASIL-decomposition nachvollziehbar in ADRs?
- [ ] MC/DC Coverage für ASIL B+ Funktionen nachgewiesen?
```

#### Was NICHT geändert werden muss:
- `validate_specs.py`: UID-Regex funktioniert mit beliebigen `[A-Z]+`-Codes
- Alle `*.agent.md`-Dateien: Prozessunabhängig
- `.github/workflows/ci.yml` und `release.yml`: Norm-unabhängig
- `specification.instructions.md` Abschnitte 1–6: Vollständig generisch

---

## 5 – Zusammenfassung und Empfehlung

| Kategorie | Kritisch | Wichtig | Minor |
|-----------|----------|---------|-------|
| Widersprüche / Ungenauigkeiten | 3 (broken ref, contradicting status gate, `--include-draft` bug) | 3 (venv in CI, Statement-Gate, applyTo) | 2 (Red-Phase-Doku, pytest.ini) |
| SSOT-Verletzungen | 0 | 3 (Annotationsformat, Spec-Gate, ASPICE-Mapping) | 4 (DON'T DOs, Tooling, Phasenbeschreibungen) |
| Compliance-Lücken (ASPICE) | SWE.3, SUP.4, SUP.9 fehlen | MAN.5, SUP.7, SUP.1-Unabhängigkeit | SWE.1 BP5, SWE.2 BP6 |

**Empfehlung**: → **refactor-mode** für folgende priorisierte Befunde:

1. **[Kritisch]** `project.config.md:4` – gebrochene Dateireferenz korrigieren
2. **[Kritisch]** `SETUP.md:15` – Widerspruch "einzige Datei" beheben
3. **[Kritisch]** `validate_specs.py:191` – `--include-draft` Bug beheben (`default=False`)
4. **[ASPICE]** `spec/aspice-compliance.md` – Status-Gate-Verletzung für alle Active-Nodes mit TODO-Statement klären (neue Ausnahmeregel oder Status auf Draft)
5. **[SSOT]** Annotationsformat auf eine SSOT-Definition konsolidieren
6. **[ASPICE]** SWE.3-Gap adressieren: Entscheidung ob im Template-Scope oder explizit als Out-of-Scope dokumentiert
7. **[Erweiterbarkeit]** ASPICE-Hardcoding in `activate-test-levels.prompt.md` generalisieren
