---
applyTo: "spec/**"
---

# Refactor-Richtlinien (refactor-mode)

Diese Datei definiert die Regeln für die Spec-Verfeinerung auf Basis von Review-Ergebnissen.
Sie gilt ergänzend zu `specification.instructions.md` wenn Spec-Nodes angepasst werden.

## Kategorien von Abweichungen

| Kategorie | Bedeutung | Aktion |
|-----------|-----------|--------|
| **Spec zu eng** | Implementierung war pragmatisch sinnvoll, Spec muss nachgezogen werden | Statement erweitern |
| **Spec unklar** | AC ist mehrdeutig, wurde unterschiedlich interpretiert | Statement präzisieren |
| **Feature-Drift** | Implementierung weicht inhaltlich ab | Rückbau ODER neue Spec |
| **Outdated** | Anforderung ist obsolet | Status → `Outdated` |

## Spec-Änderungsregeln

Beim Einpflegen von Änderungen:
- Statement-Änderungen: bestehenden Text ersetzen (kein Kommentar zum Diff)
- Neue ACs aus Refactor: neue Nodes mit nächster freier ID anlegen (Zähler in `project.config.md` erhöhen)
- Outdated-Markierungen: nur `Status: Outdated` setzen – Node nicht löschen
- Rationale aktualisieren wenn sich der Grund geändert hat

## Reihenfolge

1. Erst alle `Outdated`-Markierungen setzen
2. Dann `Spec unklar`-Nodes präzisieren
3. Dann `Spec zu eng`-Nodes erweitern
4. Zuletzt neue Nodes für `Feature-Drift` anlegen (falls bestätigt)

## DON'T DO

- Nicht eigenständig Specs ändern – immer auf User-Bestätigung warten
- Nicht Status `Draft → Active` oder `Active → Outdated` ohne explizite Anweisung
- Nicht Nodes löschen – nur `Outdated` setzen
- Nicht bestehende Relations entfernen ohne Rückfrage
