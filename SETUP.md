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

Unter **Settings → Labels** folgende Labels erstellen:

| Label | Farbe (Vorschlag) | Bedeutung |
|-------|-------------------|-----------|
| `cr-open` | `#e4e669` | Change Request eingegangen |
| `cr-assessed` | `#0075ca` | Bewertet, Aufwand bekannt |
| `cr-approved` | `#0e8a16` | Freigegeben zur Umsetzung |
| `cr-implemented` | `#6f42c1` | Umgesetzt, Spec aktualisiert |

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
