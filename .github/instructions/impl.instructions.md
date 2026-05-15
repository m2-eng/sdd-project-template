---
applyTo: "src/**"
---

# Implementierungs-Richtlinien (impl-mode)

## Traceability – Pflicht

Jede öffentliche Funktion / Methode / Klasse trägt die Spec-Referenz als erste Kommentarzeile:

```python
# @spec: SCAN-BE-001
def decode_barcode(image: bytes) -> dict:
    ...
```

```typescript
// @spec: SCAN-BE-001
export function decodeBarcode(image: Uint8Array): DecodedResult {
    ...
}
```

Interne Hilfsfunktionen ohne eigene AC können auf den übergeordneten Node verweisen.

## Minimalismus

Nur was die Spec fordert. Keine:
- Zusatzfeatures die "naheliegen"
- Vorauseilenden Abstraktionen oder Interfaces
- Optimierungen ohne Messung und Spec-Grundlage

## Abhängigkeiten

Keine neuen externen Packages ohne Spec-Deckung (`SCAN-SYS-NNN` oder `SCAN-BE-NNN`).
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
