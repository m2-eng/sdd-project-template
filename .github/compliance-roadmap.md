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
- ✅ SUP.10 (Needs Statement): Issue-Template `needs-statement.md` erstellt
- ✅ SWE.4 (Test Results – lokal): `conftest.py` + `pytest.ini` im Template – Report-Veröffentlichung → #3 CD-Pipeline

---

## Offene Punkte

### 1 – Architecture Decision Records (SWE.2)
**Norm**: ASPICE SWE.2 (Software Architecture) / DO-178C Section 11.10
**Was fehlt**: Architekturentscheidungen sind aktuell nur in Plan-Chats – nicht persistent
**Vorschlag**:
- `docs/architecture/ADR-NNN-titel.md` (Architecture Decision Records)
- plan-agent erhält `edit`-Zugriff auf `docs/architecture/`
- Lightweight ADR-Format: Kontext | Entscheidung | Konsequenzen
**Aufwand**: M (ADR-Format definieren, plan-agent erweitern)

---

### 2 – CD-Pipeline / Release-Automatisierung (SWE.4 / SWE.1 / SUP.8)
**Norm**: ASPICE SWE.4 (Test Results), SWE.1 (Traceability), SUP.8 (Baseline Artifacts)
**Status**: Konzept definiert – Implementierung ausstehend (eigene Spec empfohlen)

**Trigger**: `git tag baseline/vX.Y` + Push auf GitHub

**Was die Pipeline tut:**
1. Tests ausführen (`pytest --cov=src`)
2. Allure-Report generieren
3. StrictDoc-Export generieren (Traceability-Matrix)
4. GitHub Release mit allen Artefakten veröffentlichen
5. Pre-Release-Flag automatisch aus Tag-Suffix ableiten (`-alpha.N` / `-beta.N` → Pre-Release, sonst Release)

**Was sie abdeckt:**
- Test-Ergebnisnachweis für SWE.4
- Traceability-Matrix-Snapshot für SWE.1/SUP.1
- Baseline-Artefakte für SUP.8

**Aufwand**: M (eigene Spec empfohlen, da drei verknüpfte Schritte koordiniert werden müssen)

---

### 3 – CI Spec-Validator (SUP.2 – Verification)
**Norm**: ASPICE SUP.2 (Software Verification)
**Was fehlt**: Automatische Prüfung ob alle Spec-Nodes gültig sind (UID vorhanden, Status gesetzt)
**Vorschlag**:
- StrictDoc CLI in CI: `strictdoc passthrough .` prüft Syntax
- Eigener Validator: Python-Script prüft `@spec`-Annotationen gegen `spec/`-UIDs
**Aufwand**: M (CI-Pipeline + Validator-Script)

---

### 4 – Konfigurationsmanagement (SUP.8)
**Norm**: ASPICE SUP.8 (Configuration Management)
**Status**: Prozess definiert (`workflow.instructions.md` Phase 7, `CHANGELOG.md`) – CI-Automatisierung ausstehend

**Definierter Prozess:**
- Baseline-Trigger, Checkliste und Naming: `workflow.instructions.md`, Phase 7
- Versionshistorie: `CHANGELOG.md` mit Spec-ID-Referenzen pro Eintrag
- Baseline-Naming: `vMAJOR.MINOR` | Pre-Release: `vMAJOR.MINOR-alpha.N` / `vMAJOR.MINOR-beta.N`
- Git-Tag bei Freigabe: `baseline/vX.Y` – Git-History ist Audit-Trail
- Deliverable-Artefakte → **#2 CD-Pipeline**

---

### 5 – Integrations- und Qualifikationstests (SWE.5 / SWE.6)
**Norm**: ASPICE SWE.5 (Integration) / SWE.6 (Qualification)
**Was fehlt**: Separate Testebenen für Integration und System-Qualifikation
**Vorschlag**:
- `tests/unit/`, `tests/integration/`, `tests/qualification/` als Ordnerstruktur
- Separate TC-Codes: `TC-U`, `TC-I`, `TC-Q` (oder Subsystem-Codes erweitern)
- Separate Testreporte pro Ebene
**Aufwand**: L (Scope-Erweiterung, erfordert neue Spec-Nodes)

---

### 6 – GitHub Issues als formale Change Requests (SUP.10)
**Norm**: ASPICE SUP.10 (Change Request Management)
**Was fehlt**: Formaler CR-Status-Lifecycle im Issue (Offen → Bewertet → Genehmigt → Umgesetzt)
**Offene Schritte:**
- GitHub Labels als CR-Status anlegen: `cr-open`, `cr-assessed`, `cr-approved`, `cr-implemented`
- GitHub Projects Board mit Spalten pro Status konfigurieren
**Aufwand**: S (Labels + Project Board konfigurieren)

---

## Empfohlene Reihenfolge

1. **Sofort (S)**: CR-Labels (#6)
2. **Nächste Iteration (M)**: CD-Pipeline (#2) + ADR (#1) + CI-Validator (#3)
3. **Später (L)**: Testebenen (#5)
