# ASPICE SWE.4 – Software Unit Verification

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an den Software-Unit-Verifikationsprozess
gemäß ASPICE SWE.4. Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

## Anforderung

### Software-Units werden systematisch verifiziert und Ergebnisse nachvollziehbar dokumentiert

**UID**: PROJ-SYS-003 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.4, BP 1–6]

**Rationale**: Der SDD-Workflow erfüllt SWE.4 durch:
- `pytest` als Test-Runner mit `pytest.ini`-Konfiguration
- `pytest-cov` für Code-Coverage (HTML + XML-Report)
- `allure-pytest` für strukturierte Test-Reports mit Requirement-Linking
- `conftest.py` registriert Custom-Marker `@pytest.mark.spec("PROJ-TC-NNN")`
- `test-mode` (TDD Red-Phase): Tests werden vor Implementierung geschrieben
- CD-Pipeline (`release.yml`) veröffentlicht Test-Reports als GitHub-Release-Artefakte
