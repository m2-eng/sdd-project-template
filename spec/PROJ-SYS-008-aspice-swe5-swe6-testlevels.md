# ASPICE SWE.5 / SWE.6 – Integration and Qualification Testing

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an Integrations- und Qualifikationstests
gemäß ASPICE SWE.5 (Software Integration and Integration Test) und SWE.6
(Software Qualification Test). Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

**Aktivierung**: Copilot-Prompt `.github/prompts/activate-test-levels.prompt.md` ausführen.

## Anforderung

### Software wird auf Integrations- und Qualifikationsebene systematisch getestet

**UID**: PROJ-SYS-008 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.5, BP 1–6] und [ASPICE PAM, SWE.6, BP 1–6]

**Rationale**: Der SDD-Workflow bereitet SWE.5/6 durch folgende Infrastruktur vor:
- `tests/unit/`: Unit-Tests (Einzelfunktionen, kein I/O)
- `tests/integration/`: Integrationstests (Zusammenspiel von Modulen, externe Dienste gemockt)
- `tests/qualification/`: Qualifikationstests (End-to-End, gegen reale Umgebung)
- TC-Codes `TC-U` / `TC-I` / `TC-Q` für separate Traceability pro Testebene
- Aktivierung: `activate-test-levels.prompt.md` konfiguriert pytest.ini und CHANGELOG

Vollständige Aktivierung erfordert: pytest.ini-Erweiterung + separate Allure-Reporte + neue TC-Nodes.
