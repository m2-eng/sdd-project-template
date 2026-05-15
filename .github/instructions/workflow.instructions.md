---
applyTo: "**"
---

# SDD Workflow

## Phasen und Rollendefinition

Der SDD-Prozess läuft immer in folgender Reihenfolge:

```
[spec-mode] → [plan-mode] → [test-mode] → [impl-mode] → [review-mode]
                                                                ↓
                                                        [refactor-mode]
                                                                ↓
                                              [spec-mode] ←─── User-Bestätigung
                                              (Zyklus ab plan- oder test-mode neu)
```

Der User kann den aktiven Modus explizit durch Nennung des Modus steuern.
Ohne explizite Nennung: aktiven Modus aus dem Kontext ableiten.

---

### Phase 1 – spec-mode: Spezifikation erstellen

**Trigger**: GitHub Issue mit Label `needs-statement` (Template: `.github/ISSUE_TEMPLATE/needs-statement.md`)
oder User beschreibt ein Feature / eine Anforderung direkt im Chat.

**Eingang prüfen**:
- Liegt ein Needs-Statement-Issue vor? → Abschnitte 1–8 des Templates als Input verwenden
- Direkte Beschreibung? → Fehlende Informationen anhand der Issue-Template-Abschnitte nachfragen

**Meine Aufgaben**:
1. Nächste freie Spec-ID aus `project.config.md` ermitteln und vorschlagen
2. Spec-Datei nach dem Format aus `specification.instructions.md` aufbauen
3. ACs aus der Beschreibung ableiten – fehlende ACs explizit als offen markieren
4. Issue-Nummer in der Spec referenzieren (Relations oder Rationale: `GitHub: #NNN`)
5. Offene Fragen und Unklarheiten explizit auflisten
6. Spec zur Bestätigung vorlegen – **nicht implementieren**
7. Werte für Grenzen, Schwellen, ... explizit anfragen, wenn nicht in der Beschreibung enthalten

**Stopp-Bedingung**: Scope unklar oder widersprüchlich → zuerst klären.

---

### Phase 2 – plan-mode: Technischer Plan

**Trigger**: Spec ist vollständig und vom User bestätigt.

**Meine Aufgaben**:
1. Relevante Spec-IDs auflisten
2. Betroffene Module und Dateien identifizieren
3. Benötigte Tests ableiten (eine Zeile pro AC)
4. Abhängigkeiten, Risiken und Architekturentscheidungen benennen
5. Plan zur Bestätigung vorlegen – **nicht implementieren**
6. Nicht mehr benötigte Specs explizit als "Outdated" markieren.

**Stopp-Bedingung**: Architekturentscheidung unklar → nachfragen.

---

### Phase 3 – test-mode: Tests zuerst

**Trigger**: Technischer Plan ist bestätigt.

**Meine Aufgaben**:
1. Für jeden Testfall (TC-NNN) aus der Spec einen Test schreiben
2. Testnamen-Format: `[Spec-ID] – [Verhalten bei Szenario]`
3. Jeden Test mit Spec-Referenz annotieren: `@spec: PROJ-TC-NNN`
4. Alle Tests müssen zunächst fehlschlagen (Red-Phase)

**Stopp-Bedingung**: Testfall in Spec fehlt oder unklar → Spec zuerst erweitern.

---

### Phase 4 – impl-mode: Implementierung

**Trigger**: Tests existieren und schlagen fehl.

**Meine Aufgaben**:
1. Minimalen Code schreiben, der die Tests grün macht
2. Jede Funktion mit `@spec: PROJ-[CODE]-NNN` dokumentieren
3. Keine Logik über die Spec hinaus generieren
4. Nach Implementierung: alle Tests müssen grün sein

**Stopp-Bedingung**: Anforderung aus Spec unklar → zurück zu spec-mode.

---

### Phase 5 – review-mode: Review gegen Spec

**Trigger**: Implementierung abgeschlossen.

**Meine Aufgaben**:
1. Jeden AC aus der Spec prüfen: implementiert ja/nein?
2. Traceability prüfen: alle Funktionen haben `@spec`-Annotation?
3. Abweichungen zwischen Code und Spec explizit benennen
4. Review-Ergebnis als strukturierte Tabelle ausgeben:

| Spec-ID | AC | Status | Abweichung |
|---------|----|--------|------------|

5. State-of-the-Art, Lizenzkonflikte und Security prüfen (Checkliste: `review.instructions.md`)
6. Review-Dokument in `docs/review/YYYY-MM-DD_[Spec-ID]_review.md` speichern
7. Bei Abweichungen: Übergabe an refactor-mode empfehlen
8. Ohne Abweichungen: "Done" melden

---

### Phase 6 – refactor-mode: Spec-Verfeinerung

**Trigger**: Review-Ergebnisse liegen vor und enthalten Abweichungen.

**Meine Aufgaben**:
1. Review-Befunde lesen und kategorisieren:
   - **Spec zu eng**: Implementierung war sinnvoll, Spec muss nachgezogen werden
   - **Spec unklar**: AC ist mehrdeutig, muss präzisiert werden
   - **Feature-Drift**: Implementierung weicht inhaltlich ab → Rückbau oder neue Spec
   - **Outdated**: Anforderung ist obsolet → Status auf `Outdated` setzen
2. Konkrete Spec-Änderungsvorschläge formulieren (Tabelle: Spec-ID | Befund | Vorschlag)
3. Vorschläge vorlegen – **nicht eigenständig ändern**
4. Nach User-Bestätigung: Übergabe an spec-mode für Einpflegen
5. Neu eingespielte Specs starten den Zyklus ab plan-mode oder test-mode neu

**Stopp-Bedingung**: Keine Abweichungen im Review → refactor-mode nicht nötig.

---

### Phase 7 – baseline-mode: Baseline erstellen

**Trigger**: Review-Zyklus vollständig abgeschlossen – keine offenen Abweichungen.
Oder: Refactor-Zyklus abgeschlossen und anschließendes Review ohne Befunde.

**Ziel (ASPICE SUP.8)**: Freigegebenen Projekt-Stand fixieren.
Git-Tag = unveränderlicher Baseline-Identifier. Änderungen, Traceability und
Prozesshistorie sind über Git-History + Spec nachvollziehbar.
Artifakte (Test-Report, StrictDoc-Export) werden bei Auslieferung automatisch
von der CD-Pipeline am GitHub Release angehängt.

**Baseline-Checkliste (vor Freigabe vollständig prüfen):**

| Punkt | Bedingung |
|-------|-----------|
| Spec-Status | Alle im Scope befindlichen Nodes haben `**Status**: Active` |
| Tests | Alle Tests grün |
| Review | Review-Dokument in `docs/review/` vorhanden, alle Abweichungen geschlossen |
| Traceability | Alle Funktionen in `src/` und Tests in `tests/` tragen `@spec:`-Annotation |

**Baseline-Naming:**
- Format: `vMAJOR.MINOR` (z.B. `v1.0`, `v1.1`) – Pre-Release: `vMAJOR.MINOR-alpha.N` / `vMAJOR.MINOR-beta.N`
- **Major** erhöhen: neue oder geänderte Spec (Scope-Änderung, neues AC)
- **Minor** erhöhen: Korrekturen in Code/Tests ohne Spec-Änderung

**Meine Aufgaben:**
1. Baseline-Checkliste prüfen – bei nicht erfülltem Punkt: blockieren und Grund benennen
2. `CHANGELOG.md`-Eintrag vorbereiten (alle enthaltenen Spec-IDs auflisten)
3. Git-Befehle für Commit + Tag ausgeben: `git commit -m "Baseline vX.Y"` + `git tag baseline/vX.Y`
4. Nach User-Bestätigung: Baseline als abgeschlossen melden – CD-Pipeline übernimmt Artifact-Erzeugung

**Stopp-Bedingung**: Offene Abweichungen im letzten Review oder Tests nicht grün → baseline-mode nicht zulässig.

---

## Spec-Gate (immer aktiv, in allen Modi)

Werde ich gebeten, Code ohne Spec-ID zu schreiben, antworte ich immer:

> „Kein Code ohne Spec. Bitte nenne die Spec-ID oder wir erstellen zuerst eine Spec (spec-mode)."

## Annotationsformat (alle Modi)

Spec-Referenzen im Code folgen immer diesem Format:

```
@spec: PROJ-[CODE]-NNN        ← allgemeine Funktion
@spec: PROJ-TC-NNN            ← Testfunktion (verlinkt TC-Node)
```

UID-Konvention und Subsystem-Codes: `specification.instructions.md`, Abschnitt 7.
## Hinweis zur Vorlage

Diese Datei ist als projektunabhängige Vorlage konzipiert.
Projektkürzel, Ordnerstrukturen und Tooling-spezifische Regeln gehören in eine projektspezifische Erweiterung.
