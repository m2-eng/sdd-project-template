---
applyTo: "**"
---
<!-- @spec: PROJ-SYS-004 -->

# Review-Richtlinien (review-mode)

Diese Datei definiert was bei einem Review systematisch geprüft wird.
Sie gilt in allen Phasen, wird aber aktiv nur im review-mode angewendet.

## 1 – Spec-Abgleich (Pflicht)

Für jeden AC eines Requirement-Nodes:
- Ist die Anforderung implementiert?
- Ist die Implementierung vollständig (kein Teilfehler)?
- Weicht die Implementierung inhaltlich von der Spec ab?

## 2 – Traceability (Pflicht)

- Jede öffentliche Funktion in `src/` hat `@spec: PROJ-[CODE]-NNN`
- Jede Testfunktion in `tests/` hat `@spec: PROJ-TC-NNN`
- Keine Annotation → Traceability-Lücke → explizit auflisten

## 3 – State-of-the-Art (Pflicht)

Veraltete Muster und Technologien identifizieren:
- Deprecated APIs oder Bibliotheksversionen
- Veraltete Patterns (z.B. Callback-Hell statt async/await, veraltete Klassenkonventionen)
- Framework-spezifische Anti-Patterns (z.B. direkte DOM-Mutation in React, fehlende Typisierung in TypeScript)
- Abweichungen vom aktuellen Projektstandard (laut `project.config.md` – Tooling-Entscheidungen)

Befund melden: `| [Datei:Zeile] | [veraltetes Muster] | [empfohlene Alternative] |`

## 4 – Lizenzkonflikte (Pflicht bei neuen Abhängigkeiten)

Bei jeder neuen externen Abhängigkeit prüfen:
- Lizenz des Packages (MIT, Apache-2.0, GPL-3.0, LGPL, ...)?
- Lizenzkonflikt mit Projektlizenz (aus `LICENSE`-Datei im Root)?
- Copyleft-Risiko: GPL/AGPL in kommerziellen oder proprietären Projekten
- Transitive Abhängigkeiten mit problematischen Lizenzen

Befund melden: `| Package | Version | Lizenz | Konfliktrisiko | Empfehlung |`

## 5 – Security (Pflicht)

Kritische OWASP-Top-10-Muster prüfen:
- Injection (SQL, Command, LDAP)
- Unsichere Deserialisierung
- Hartcodierte Credentials oder Secrets
- Fehlende Input-Validierung an Systemgrenzen
- Unsichere Abhängigkeiten (bekannte CVEs)

## Ausgabe-Pflicht

Jeder Befund muss mit Datei + Zeilennummer oder Spec-ID belegt sein.
Keine ungefundenen Wertungen.

## DON'T DO

- Kein "sieht gut aus" ohne vollständigen Abgleich
- Keine Dateiänderungen – review-mode ist read-only
- Keine Empfehlungen jenseits der Spec-Anforderungen als "fehlend" markieren
