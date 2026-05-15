---
applyTo: "src/**"
---

# Implementierungs-Richtlinien (impl-mode)

## Traceability – Pflicht

Jede öffentliche Funktion / Methode / Klasse trägt die Spec-Referenz als erste Kommentarzeile:

```python
# @spec: PROJ-BE-001
def process_data(input: bytes) -> dict:
    ...
```

```typescript
// @spec: PROJ-BE-001
export function processData(input: Uint8Array): ProcessedResult {
    ...
}
```

> Kanonische Definition: `specification.instructions.md` Abschnitt 2.3

Interne Hilfsfunktionen ohne eigene AC können auf den übergeordneten Node verweisen.

## Minimalismus

Nur was die Spec fordert. Keine:
- Zusatzfeatures die "naheliegen"
- Vorauseilenden Abstraktionen oder Interfaces
- Optimierungen ohne Messung und Spec-Grundlage

## Abhängigkeiten

Keine neuen externen Packages ohne Spec-Deckung (`PROJ-SYS-NNN` oder `PROJ-BE-NNN`).
Neue Abhängigkeit einzuführen = Architekturentscheidung = plan-mode nötig.

Alle Packages werden ausschließlich in `.venv` installiert – **nie global**:

```powershell
# Korrekt
.venv\Scripts\Activate.ps1
pip install <package>

# Verboten
pip install <package>   ← ohne aktivierte venv
```

## DON'T DO

- Kein Code ohne `@spec:`-Annotation
- Keine Änderungen in `spec/` (dafür: spec-agent)
- Keine Änderungen in `tests/` (dafür: test-agent)
- Keine `TODO`-Kommentare ohne zugehörige offene Spec
- **Kein `pip install` ohne aktivierte `.venv`**
