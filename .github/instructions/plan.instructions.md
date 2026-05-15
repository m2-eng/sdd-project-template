---
applyTo: "spec/**"
---
<!-- @spec: PROJ-SYS-002 -->

# Plan-Richtlinien (plan-mode)

## Zweck dieser Datei

Diese Datei definiert die Regeln für die Ableitung technischer Pläne aus Spec-Dateien.
Sie gilt ergänzend zu `specification.instructions.md` wenn Spec-Dateien im plan-mode gelesen werden.

## TC-Ableitung aus ACs

Für jeden Acceptance Criterion (AC) wird genau **ein** TC-Node abgeleitet.
Ausnahme: Ein AC mit mehreren Pfaden (Happy Path / Error Path) bekommt je einen TC-Node.

Benennungsregel für abgeleitete TC-IDs im Plan (noch nicht vergeben):
```
TC-Vorschlag: PROJ-TC-NNN  ← aus project.config.md, Zähler noch nicht erhöhen
```
Der Zähler wird erst erhöht wenn der TC-Node in spec/ angelegt wird (durch spec-agent, test-mode).

## Outdated-Erkennung

Ein Spec-Node ist Outdated-Kandidat wenn:
- er durch einen neueren Node ersetzt wird (Relations: `replaces`)
- seine Vorbedingung durch Architekturänderungen nicht mehr erreichbar ist
- kein aktiver TC-Node mehr auf ihn verweist

## DON'T DO

- Keine Architekturentscheidungen dokumentieren ohne sie als offen zu markieren
- Keine TC-IDs vergeben (Zähler hochzählen) – das macht erst der test-agent
- Keine Implementierungsdetails im Plan
