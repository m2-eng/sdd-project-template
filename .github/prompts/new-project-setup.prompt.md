---
mode: agent
description: "Führt durch die initiale Konfiguration eines neuen Projekts aus diesem Template. Passt project.config.md und strictdoc_config.py an."
tools: [read_file, replace_string_in_file]
---

Du hilfst beim Einrichten eines neuen Projekts aus dem SDD-Template.

## Schritt 1 – Projektdaten abfragen

Frage den User nach folgenden Werten (alle Pflicht):

1. **Projektkürzel** (2–6 Großbuchstaben, z.B. `PROJ`) – wird Präfix aller Spec-IDs
2. **Projekttitel** (Freitext, z.B. `Mein Projekt`) – erscheint in StrictDoc
3. **GitHub Repository** (Format `org/repo`, z.B. `myorg/my-project`)

Stelle alle drei Fragen auf einmal. Warte auf die Antwort, bevor du Dateien änderst.

## Schritt 2 – Dateien anpassen

Sobald du alle drei Werte hast, passe folgende Dateien an:

### `.github/project.config.md`

Ersetze:
- `PROJ` → Projektkürzel
- `MyProject` → Projekttitel
- `org/my-project` → GitHub Repository

In der Spec-ID-Tabelle: Alle Einträge von `PROJ-[CODE]-001` auf `[KÜRZEL]-[CODE]-001` umbenennen.

### `strictdoc_config.py`

Ersetze:
- `project_title="MyProject"` → `project_title="[Projekttitel]"`

## Schritt 3 – Abschlussmeldung

Nach den Änderungen ausgeben:

```
✅ Projekt '[Projekttitel]' ([Kürzel]) konfiguriert.

Nächste Schritte:
1. Lokale Umgebung einrichten:  .\setup.ps1
2. Manuelle GitHub-Schritte:    SETUP.md → Abschnitt 4
3. Erste Spec erstellen:        @Spec Agent aufrufen
```
