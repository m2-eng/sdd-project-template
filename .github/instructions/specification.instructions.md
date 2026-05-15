---
applyTo: "spec/**"
---

# Spezifikations-Richtlinien (StrictDoc Markdown)

Specs im `spec/`-Ordner sind StrictDoc-Markdown-Dokumente (`.md`).
StrictDoc liest diese Dateien, erkennt Requirement-Nodes und baut eine
automatische Traceability-Matrix. Das Format ist gleichzeitig lesbares Markdown
und maschinenauswertbare Spezifikation.

---

## 1. Dateistruktur

```
spec/PROJ-[CODE]-NNN-kurzer-titel.md
```

Jede Spec-Datei folgt diesem Aufbau:

| Element | Markdown | Bedeutung |
|---------|----------|-----------|
| Dokumenttitel | `# Überschrift` (H1) | Pflicht, erste Zeile der Datei |
| Sektion | `## Überschrift` (H2) | Gliederung ohne UID = reiner Textabschnitt |
| Requirement-Node | `### Überschrift` (H3) | Wird zu Requirement-Node, wenn `**UID**:` folgt |
| Freitext | Normaler Absatz | Kein UID = kein Requirement, nur Dokument-Inhalt |

---

## 2. Requirement-Node-Syntax

### 2.1 Vollständiges Beispiel

```markdown
### Eingabe wird beim Aufruf verarbeitet

**UID**: PROJ-BE-001 \
**Status**: Draft \
**Relations**: PROJ-SYS-001

**Statement**: Given das System bereit ist und eine gültige Eingabe vorliegt,
When der Verarbeitungsprozess gestartet wird, Then liefert die Funktion das
erwartete Ergebnis innerhalb von 500 ms zurück.

**Rationale**: Kernfunktion des Systems – ohne diesen Schritt ist kein weiterer
Anwendungsfall möglich.
```

### 2.2 Minimales Beispiel (ohne Relations, ohne Rationale)

```markdown
### Berechtigung wird beim Start angefordert

**UID**: PROJ-UI-001 \
**Status**: Draft

**Statement**: Given die App wird erstmalig geöffnet, When eine Systemberechtigung
benötigt wird, Then fordert die App diese Berechtigung vom Betriebssystem an.
```

---

## 3. Felder und ihre Regeln

| Feld | Pflicht | Wert | Hinweis |
|------|---------|------|---------|
| **UID** | Ja | `PROJ-[CODE]-NNN` | Eindeutig über alle Dateien hinweg; CODE aus Subsystem-Tabelle (Abschnitt 7) |
| **Status** | Empfohlen | `Draft`, `Active`, `Outdated` | Gültige Werte – Details in Abschnitt 8 |
| **Relations** | Optional | UID des Parent-Requirements | Nur einfache Parent-Relations (siehe Abschnitt 5) |
| **Statement** | Ja | Given/When/Then-Text | Inhalt des Requirements |
| **Rationale** | Empfohlen | Freitext | Warum existiert dieses Requirement? Entfällt der Grund, kann auch das Feature entfallen. |

Das H3-Heading (`### Titel`) wird zum **TITLE** des Requirement-Nodes.
Wenn kein `**UID**:` auf das Heading folgt, bleibt es eine gewöhnliche Sektion.

---

## 4. Syntax-Regeln (Pflicht – Verstöße erzeugen Parser-Fehler)

### Regel 1: Backslash am Ende aller Meta-Felder außer dem letzten

Alle Meta-Felder (UID, Status, Relations) außer dem **letzten** Meta-Feld enden
mit ` \` (Leerzeichen + Backslash). Das letzte Meta-Feld hat kein `\`.

```markdown
### Beispiel mit allen Meta-Feldern

**UID**: PROJ-BE-001 \        ← nicht letztes Meta-Feld → \
**Status**: Draft \        ← nicht letztes Meta-Feld → \
**Relations**: PROJ-SYS-001    ← letztes Meta-Feld → kein \

**Statement**: ...
```

```markdown
### Beispiel ohne Relations

**UID**: PROJ-BE-001 \        ← nicht letztes Meta-Feld → \
**Status**: Draft          ← letztes Meta-Feld → kein \

**Statement**: ...
```

```markdown
### Beispiel mit nur UID

**UID**: PROJ-BE-001          ← einziges / letztes Meta-Feld → kein \

**Statement**: ...
```

### Regel 2: Pflichtleerzeile zwischen Meta-Block und Content-Block

Zwischen dem letzten Meta-Feld und `**Statement**:` muss genau eine Leerzeile
stehen. Kein Leerzeile = Parse-Fehler.

### Regel 3: Keine leeren Felder

Ein Feld muss entweder vollständig mit Wert vorhanden sein oder komplett fehlen.
`**Status**:` ohne Wert ist ungültig. Platzhalter: `TBD` oder `TBC`.

### Regel 4: Genau eine Leerzeile zwischen Requirement-Nodes

Kein Leerzeile oder mehr als eine Leerzeile zwischen zwei Nodes führt zu
unerwartetem Verhalten.

### Regel 5: Datei endet mit Newline

Jede `.md`-Datei muss mit einem Zeilenumbruch enden.

### Regel 6: H1 genau einmal, am Dateianfang

Die `# Überschrift` (H1) ist der Dokumenttitel. Sie muss die erste Zeile sein
und darf nur einmal pro Datei vorkommen.

---

## 5. Relations (Parent-Verknüpfungen)

```markdown
**Relations**: PROJ-SYS-001
```

- Verbindet dieses Requirement als **Kind** mit dem Parent `PROJ-SYS-001`
- Beide Nodes müssen eine `**UID**:` haben, sonst ignoriert StrictDoc den Link
- Keine Kreisverweise (A → B → A) – führt zu Validierungsfehler
- **Relation Roles** (`Refines`, `Verifies`, etc.) sind im MD-Modus noch nicht
  unterstützt (experimentell, v0.21.0)
- Mehrere Parents: noch nicht offiziell dokumentiert für MD-Modus – vermeiden
- GitHub-Issue-Referenz: **nicht** als StrictDoc-Relation, sondern im `Rationale`-Feld:
  `Rationale: GitHub: #42` (Freitext, kein maschinenauswertbarer Link)

---

## 6. Vollständiges Spec-Template

```markdown
# [PROJ-[CODE]-NNN] Feature-Titel

## Kontext

[Warum wird dieses Feature benötigt? Welches Problem wird gelöst?]

## Scope

**In-Scope**: [Was implementiert wird]

**Out-of-Scope**: [Was explizit ausgeschlossen ist]

## Anforderungen

### [Kurztitel des ersten Akzeptanzkriteriums]

**UID**: PROJ-[CODE]-NNN \
**Status**: Draft

**Statement**: Given [Vorbedingung], When [Aktion], Then [Erwartetes Ergebnis]

**Rationale**: [Warum ist dieses Requirement notwendig?]

### [Kurztitel des zweiten Akzeptanzkriteriums]

**UID**: PROJ-[CODE]-NNN \
**Status**: Draft \
**Relations**: PROJ-[CODE]-NNN

**Statement**: Given [Vorbedingung], When [Aktion], Then [Erwartetes Ergebnis]

## Abhängigkeiten

[Hängt ab von PROJ-[CODE]-NNN: Begründung. Oder: Keine.]

## Offene Fragen

[Frage 1 (Verantwortlich: ?, Deadline: ?). Oder: Keine.]
```

---

## 7. Namenskonventionen

| Element | Konvention | Beispiel |
|---------|-----------|---------|
| Dateiname | `PROJ-[CODE]-NNN-kurzer-titel.md` | `PROJ-BE-001-feature-title.md` |
| UID | `PROJ-[CODE]-NNN` | `PROJ-BE-001`, `PROJ-SEC-042` |
| Nächste freie ID | Aus `project.config.md` ablesen (pro Code) | |
| H3-Titel | Kurz, beschreibend, kein Nummerierungspräfix | StrictDoc nummeriert selbst |

### Subsystem-Codes

Jedes Requirement gehört genau einem Subsystem-Code. Nicht benötigte Codes
werden im Projekt einfach nicht verwendet.

| Code | Bereich | Wann verwenden |
|------|---------|----------------|
| `SYS` | System / Querschnittsanforderungen | Projektübergreifende Ziele, globale Constraints, NFRs ohne klare Komponente |
| `UI` | User Interface / Frontend | Darstellung, Bedienfluss, Barrierefreiheit |
| `BE` | Backend / Geschäftslogik | Fachliche Kernlogik, Algorithmen, Services |
| `API` | Externe Schnittstellen | REST/gRPC/SDK-Verträge nach außen |
| `DATA` | Datenhaltung / Persistenz | Datenmodell, Migrationen, Storage-Verhalten |
| `INT` | Integration / Middleware | Drittanbieter-Anbindungen, OS-Dienste, Kamera-API |
| `SEC` | Security | Authentifizierung, Autorisierung, Datenschutz, Kryptographie |
| `SAF` | Safety (Funktionale Sicherheit) | Failsafe-Verhalten, ASIL-Anforderungen, sicherheitskritische Abläufe |
| `TC` | Testfälle | Reserviert für TC-Nodes (siehe Abschnitt 10) – kein fachliches Subsystem |

**Nummernraum**: Jeder Code hat seinen eigenen Counter. `PROJ-BE-001` und
`PROJ-SEC-001` sind zwei verschiedene Requirements.

---

## 8. Status-Werte

| Status | Bedeutung |
|--------|-----------|
| `Draft` | Spec in Arbeit, noch nicht implementierbar |
| `Active` | Spec bereit, implementiert und geprüft |
| `Outdated` | Deaktiviert – nicht löschen, Traceability bleibt erhalten |

StrictDoc zeigt diese Werte in den Projektstatistiken aus.
Eigene Werte (z.B. `Bereit`) sind syntaktisch erlaubt, werden aber nicht
gesondert ausgewertet.

---

## 9. Qualitätsgates

Von `Draft` zu `Active`, wenn:

- UID im Format `PROJ-[CODE]-NNN`, eindeutig über alle Dateien
- Alle Statements messbar formuliert (Given/When/Then)
- Rationale vorhanden – beantwortet "Warum?" (Entfällt der Grund, kann das Feature entfallen)
- Scope eindeutig abgegrenzt (In/Out)
- Keine offenen Fragen ohne Verantwortlichen
- Statement-Feld bei jedem Requirement-Node vorhanden

---

## 10. DON'T DO – Häufige Fehler

| Nicht tun | Warum |
|-----------|-------|
| `Relation Roles` verwenden (`Refines:`, `Verifies:`) | Im MD-Modus nicht unterstützt – stiller Parser-Fehler |
| `**Statement**:` weglassen | Pflichtfeld – Node ohne Statement ist in StrictDoc leer |
| Vages Statement ohne Given/When/Then | Nicht testbar → bleibt dauerhaft `Draft` |
| Mehrere Requirements in einen H3-Node | Ein H3 = ein Requirement-Node – sonst verliert StrictDoc die Einzelreferenzierbarkeit |
| Leerzeile zwischen Meta-Block und Statement vergessen | Parse-Fehler (Regel 2) |
| UID ohne Code-Präfix (`PROJ-001` statt `PROJ-BE-001`) | Widerspricht der Konvention; Nummernraum ist pro Code getrennt |

---

## 11. Testfälle (TC-Nodes)

Testfälle werden im MD-Modus als reguläre Requirement-Nodes mit dem reservierten
Code `TC` beschrieben. Damit entsteht eine durchgehende Traceability-Kette:

```
Requirement-Node  (PROJ-BE-001)
    └── TC-Node   (PROJ-TC-001)   ←  Relations: PROJ-BE-001
            └── Testfunktion       ←  @spec: PROJ-TC-001
```

**Was StrictDoc automatisch zeigt**: Requirement → TC-Node (wegen `Relations:`).
**Was manuell verknüpft wird**: TC-Node → Testcode (via `@spec:`-Kommentar für
Code-Reviews und Spec-Traceability).

### TC-Node Syntax

```markdown
### Funktion gibt erwartetes Ergebnis zurück

**UID**: PROJ-TC-001 \
**Status**: Draft \
**Relations**: PROJ-BE-001

**Statement**: Given das System bereit ist und eine gültige Eingabe vorliegt,
When die Verarbeitungsfunktion aufgerufen wird, Then gibt sie das erwartete
Ergebnis im definierten Format innerhalb der Zeitvorgabe zurück.
```

### Testcode-Annotation

```python
# @spec: PROJ-TC-001
def test_function_returns_expected_result():
    ...
```

```typescript
// @spec: PROJ-TC-001
test('Function returns expected result', () => { ... });
```

### Ablageort

TC-Nodes können wahlweise:
- In der **Spec-Datei des Features** stehen – direkt nach dem Requirement-Node
- In einer **eigenen Datei** `PROJ-TC-NNN-kurzer-titel.md` liegen – sinnvoll
  wenn TC-Nodes mehrere Dateien oder Features abdecken

### Einschränkung (MD-Modus)

StrictDoc kann `@spec:`-Kommentare im Quellcode **nicht automatisch** auswerten.
Die Verbindung TC-Node → Testcode ist eine manuelle Konvention. StrictDoc zeigt
nur den Requirement → TC-Node-Link in der Traceability-Matrix.
Vollautomatische Code-Coverage erfordert den nativen `.sdoc`-Modus mit
StrictDoc-spezifischen Source-Code-Markern.

---

## 12. Bekannte Einschränkungen (MD-Modus, StrictDoc v0.21.0, experimentell)

| Einschränkung | Details |
|--------------|---------|
| Kein Custom Grammar | Felder wie TAGS, VERIFICATION, OWNER sind nicht verfügbar |
| Keine Relation Roles | Nur einfache Parent-Relations, keine `Refines`/`Verifies`-Rollen |
| Kein PREFIX für auto-UID | UIDs müssen manuell vergeben werden |
| Keine COMMENT-Felder | COMMENT ist im MD-Modus nicht unterstützt – Rationale verwenden |
| Mehrere Parents unklar | Syntax für mehrere Relations nicht dokumentiert – nur einen Parent |
| Web-Editor Einschränkungen | Manche Web-UI-Features nur für `.sdoc`-Dateien verfügbar |

Diese Punkte sind offen auf dem StrictDoc-Backlog:
https://github.com/strictdoc-project/strictdoc/issues/1321
