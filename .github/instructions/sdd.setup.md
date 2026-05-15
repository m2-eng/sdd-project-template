# SDD – Setup & Referenz

Diese Datei gehört zur SDD-Vorlage und wird **nicht** pro Projekt angepasst.
Projektspezifische Werte (Kürzel, ID-Zähler, Tooling-Switches) liegen
ausschließlich in `.github/project.config.md`.

---

## Ordnerstruktur

```
spec/                    → Spezifikationen (*.md, StrictDoc Markdown)
src/                     → Produktionscode
tests/                   → Tests
docs/
  review/                → Review-Dokumente (YYYY-MM-DD_[Spec-ID]_review.md)
CHANGELOG.md             → Versionshistorie mit Spec-ID-Referenzen (baseline-mode)
.github/
  agents/
    spec-agent.agent.md    → Phase 1: Spec erstellen / einpflegen
    plan-agent.agent.md    → Phase 2: Technischen Plan erstellen
    test-agent.agent.md    → Phase 3: Tests schreiben (Red-Phase)
    impl-agent.agent.md    → Phase 4: Implementierung (Green-Phase)
    review-agent.agent.md  → Phase 5: Review gegen Spec
    refactor-agent.agent.md → Phase 6: Spec-Verfeinerung aus Review
  instructions/
    specification.instructions.md  → Spec-Format (applyTo: spec/**)
    plan.instructions.md           → Plan-Regeln (applyTo: spec/**)
    test.instructions.md           → Test-Regeln (applyTo: tests/**)
    impl.instructions.md           → Impl-Regeln (applyTo: src/**)
    review.instructions.md         → Review-Prüflisten (applyTo: **)
    refactor.instructions.md       → Refactor-Regeln (applyTo: spec/**)
    workflow.instructions.md       → SDD-Workflow 6 Phasen (applyTo: **)
    sdd.setup.md                   → diese Datei
  ISSUE_TEMPLATE/
    needs-statement.md               → Needs Statement Template (Interview-Leitfaden + Checkliste)
    config.yml                       → Deaktiviert Blank Issues, erzwingt Template-Nutzung
  copilot-instructions.md          → Globale Kern-Regeln (immer aktiv)
  project.config.md                → Projektspezifische Werte ← hier anpassen
strictdoc_config.py                → StrictDoc-Projektkonfiguration
.venv/                             → Python venv (nicht einchecken)
```

## Zugriffsmatrix pro Phase

| Ordner         | spec-agent | plan-agent | test-agent | impl-agent | review-agent | refactor-agent |
|----------------|:----------:|:----------:|:----------:|:----------:|:------------:|:--------------:|
| `spec/`        | R/W        | R          | R          | –          | R            | R/W*           |
| `src/`         | –          | R          | R          | R/W        | R            | –              |
| `tests/`       | –          | R          | R/W        | R          | R            | –              |
| `docs/review/` | –          | –          | –          | –          | R/W          | –              |
| `CHANGELOG.md` | –          | –          | –          | –          | R/W          | –              |

\* refactor-agent schlägt vor, spec-agent führt aus

**baseline-mode** (Phase 7) wird vom review-agent nach erfolgreichem Review ausgeführt.

---

## Projekt-Setup

> **Pflicht**: Alle Python-Befehle laufen ausschließlich in der aktivierten `.venv`. Kein globales `pip install`.

### Schnellstart (empfohlen)

```powershell
.\setup.ps1
```

Das Skript erstellt die `.venv` (falls nicht vorhanden), aktiviert sie und
installiert alle Abhängigkeiten aus `requirements-dev.txt` automatisch.

### Manuelle Einrichtung (Python 3.10+ vorausgesetzt)

```powershell
# 1. Venv erstellen und aktivieren
python -m venv .venv
.venv\Scripts\Activate.ps1

# 2. Alle Entwicklungsabhängigkeiten installieren
pip install -r requirements-dev.txt
```

### Abhängigkeiten

Alle Entwicklungs- und Testwerkzeuge sind in `requirements-dev.txt` gepflegt:

| Package | Zweck |
|---------|-------|
| `strictdoc` | Spec-Server + HTML-Export |
| `pytest` | Test-Runner |
| `pytest-cov` | Code-Coverage (XML + HTML) |
| `allure-pytest` | Test-Reports mit Traceability |

### StrictDoc verwenden

```powershell
# HTML-Export erzeugen (in output/ Ordner)
strictdoc export .

# Web-Server starten (http://127.0.0.1:5111)
strictdoc server .
```

Konfiguration liegt in `strictdoc_config.py` im Projektroot.
Der `output/`-Ordner (generiert von StrictDoc) gehört in `.gitignore`.

**Hinweis Windows**: Schlägt `.venv\Scripts\Activate.ps1` fehl, Execution Policy
prüfen:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## SDD-Workflow – Modussteuerung

Der aktive Workflow ist in `workflow.instructions.md` definiert.

Modussteuerung per Prompt:

| Prompt | Phase | Ausgabe |
|--------|-------|---------|
| `spec-mode` | 1 | Spec erstellen / verfeinern |
| `plan-mode` | 2 | Technischen Plan erstellen |
| `test-mode` | 3 | Tests schreiben (Red-Phase) |
| `impl-mode` | 4 | Implementierung (Green-Phase) |
| `review-mode` | 5 | Code-Review gegen Spec + Review-Dokument |
| `refactor-mode` | 6 | Spec-Verfeinerung aus Review-Befunden |

---

## Neues Projekt aus dieser Vorlage erstellen

1. Repository kopieren / Template verwenden
2. `.github/project.config.md` anpassen:
   - `Projektkürzel` (z.B. `PROJ` → `MYAPP`)
   - `Projekttitel` und `Repository`
   - ID-Zähler auf `001` zurücksetzen
   - Tooling-Switches überprüfen
3. `strictdoc_config.py` anpassen: `project_title`
4. In den Agent-Dateien unter `.github/agents/` das Projektkürzel in den Annotationsbeispielen anpassen (z.B. `PROJ-BE-001` → `MYAPP-BE-001`)
5. Alle anderen Dateien unverändert übernehmen
