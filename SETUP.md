# Projekt-Setup

Dieses Template erstellt ein vollständiges SDD-Projekt mit ASPICE-konformem Workflow
(Spec → Plan → Test → Impl → Review → Baseline).

---

## 1 – Repository anlegen

1. Auf GitHub: **Use this template** → neues Repository erstellen
2. Repository klonen:
   ```powershell
   git clone https://github.com/<org>/<repo>.git
   cd <repo>
   ```

---

## 2 – Pflichtanpassungen (lokal, einmalig)

### `.github/project.config.md`

Die **einzige Datei**, die pro Projekt angepasst werden muss:

| Feld | Beispiel | Beschreibung |
|------|----------|--------------|
| Projektkürzel | `PROJ` | Präfix aller Spec-IDs (`PROJ-BE-001`) |
| Projekttitel | `MeinProjekt` | Anzeigename in StrictDoc |
| Repository | `org/repo` | GitHub Repository-Pfad |

### `strictdoc_config.py`

```python
project_title="MeinProjekt",   # ← anpassen
```

---

## 3 – Lokale Entwicklungsumgebung einrichten

```powershell
.\setup.ps1
```

Erstellt `.venv`, installiert alle Abhängigkeiten aus `requirements-dev.txt`.

**Voraussetzung**: Python 3.10+, PowerShell

> **Hinweis**: Für Schritt 4.2 (CR-Labels) wird zusätzlich die [GitHub CLI (`gh`)](https://cli.github.com/) benötigt:
> ```powershell
> winget install --id GitHub.cli   # Windows
> # brew install gh                 # macOS
> # sudo apt install gh             # Ubuntu/Debian
> gh auth login                    # einmalig authentifizieren
> ```

```powershell
# Tests ausführen
.venv\Scripts\python.exe -m pytest

# Spec-Server starten (http://127.0.0.1:5111)
.venv\Scripts\strictdoc server .
```

---

## 4 – GitHub konfigurieren (manuelle Schritte)

### 4.1 – GitHub Actions (keine Konfiguration nötig)

Die CD-Pipeline (`.github/workflows/release.yml`) läuft automatisch.
`GITHUB_TOKEN` ist in GitHub Actions immer verfügbar – kein Secret anlegen.

**Trigger**: Tag `baseline/vX.Y` pushen → GitHub Release wird automatisch erstellt.

```powershell
git tag baseline/v1.0
git push origin baseline/v1.0
```

Pre-Release: Tag mit `-alpha.N` oder `-beta.N` Suffix → wird automatisch als Pre-Release markiert.

```powershell
git tag baseline/v1.0-alpha.1
git push origin baseline/v1.0-alpha.1
```

### 4.2 – CR-Labels anlegen (SUP.10)

Im geklonten Repository ausführen (einmalig, `gh` CLI muss authentifiziert sein):

```powershell
.github\setup-labels.ps1
```

Das Script legt folgende Labels an:

| Label | Bedeutung |
|-------|-----------|
| `cr-open` | Change Request eingegangen |
| `cr-assessed` | Bewertet, Aufwand bekannt |
| `cr-approved` | Freigegeben zur Umsetzung |
| `cr-implemented` | Umgesetzt, Spec aktualisiert |

### 4.3 – GitHub Projects Board anlegen (optional, SUP.10)

Unter **Projects → New project → Board**:

Spalten: `CR Open` | `CR Assessed` | `CR Approved` | `CR Implemented`

Issues werden per Label automatisch den Spalten zugeordnet (Automation konfigurieren).

---

## 5 – Copilot-Agents verwenden

Die Agents sind unter `.github/agents/` definiert und in VS Code direkt aufrufbar:

| Phase | Agent | Trigger |
|-------|-------|---------|
| Spec | `@Spec Agent` | Neues Feature / Anforderung beschreiben |
| Plan | `@Plan Agent` | Spec-ID nennen |
| Test | `@Test Agent` | Spec-ID nennen |
| Impl | `@Impl Agent` | TC-ID(s) nennen |
| Review | `@Review Agent` | Spec-ID nennen |
| Refactor | `@Refactor Agent` | Nach Review mit Abweichungen |

Für die Ersteinrichtung: Copilot-Prompt `new-project-setup` ausführen
(`.github/prompts/new-project-setup.prompt.md`).

---

## 6 – Erste Baseline erstellen

1. Mindestens eine Spec, Tests und Implementierung vorhanden
2. Review-Agent ausführen → Review-Dokument in `docs/review/` erzeugt
3. `CHANGELOG.md` aktualisieren
4. Baseline setzen:

```powershell
git add .
git commit -m "Baseline v1.0"
git tag baseline/v1.0
git push
git push origin baseline/v1.0
```

→ GitHub Actions erzeugt automatisch den Release mit allen Artefakten.

---

## 7 – ASPICE-Compliance-Übersicht

Das Template deckt folgende ASPICE-Prozesse ab. Jeder Prozess ist als Spec-Node
dokumentiert – der Normtext wird projektspezifisch eingepflegt.

| ASPICE-Prozess | Spec-UID | Implementiert durch |
|---------------|----------|---------------------|
| SWE.1 – Software Requirements | `PROJ-SYS-001` | `spec/`, StrictDoc, UID-Traceability, `spec-mode` |
| SWE.2 – Architectural Design | `PROJ-SYS-002` | `docs/architecture/`, ADR-Template, `plan-mode` |
| SWE.4 – Unit Verification | `PROJ-SYS-003` | `pytest`, `conftest.py`, `pytest.ini`, `test-mode`, CD-Pipeline |
| SUP.1 – Quality Assurance | `PROJ-SYS-004` | `docs/review/`, `review-mode`, Review Agent |
| SUP.2 – Verification | `PROJ-SYS-005` | `scripts/validate_specs.py`, `.github/workflows/ci.yml` |
| SUP.8 – Configuration Mgmt | `PROJ-SYS-006` | Git-Tags, `CHANGELOG.md`, `baseline-mode`, CD-Pipeline |
| SUP.10 – Change Request Mgmt | `PROJ-SYS-007` | GitHub Issues, `needs-statement`-Template, CR-Labels |
| SWE.5/6 – Integration/Qualification | `PROJ-SYS-008` | Vorbereitet (Draft) – Aktivierung: `activate-test-levels`-Prompt |

**Normtext einfügen**: In jeder Spec-Datei unter `spec/PROJ-SYS-00N-*.md` das
`**Statement**`-Feld mit dem lizenzierten ASPICE PAM-Text befüllen.

**Vollständige Traceability-Matrix**: StrictDoc-Export via CD-Pipeline oder lokal:
```powershell
.venv\Scripts\strictdoc server .   # http://127.0.0.1:5111
```
