<!-- @spec: PROJ-SYS-001 -->
<!-- @spec: PROJ-SYS-007 -->

## SDD – Kernregeln

### Spec-Gate
Generiere niemals Code ohne eine gültige Spec-ID. Fehlt eine passende Spezifikation: stoppe und weise explizit darauf hin.

### Traceability
Jede generierte Funktion trägt einen Verweis auf ihre Spec-ID als Kommentar: `@spec: PROJ-[CODE]-NNN`.

### Spec-first bei Unklarheit
Ist eine Spec unvollständig oder widersprüchlich: zuerst klären, nicht improvisieren.

### Minimalismus
Nur spezifikationskonformer, minimaler Code. Keine ungefragten Features, Optimierungen oder Refactorings.

### Proaktives Feedback
Kritische Anmerkungen und sinnvolle Ergänzungsvorschläge sind ausdrücklich erwünscht. Eigenständige Umsetzung ohne explizite Spec und Bestätigung des Users: nie.

### Sicherheit
Niemals unsicheren Code generieren. Keine externen Abhängigkeiten ohne Spezifikation. Bei unklarem sicheren Ansatz: nachfragen.

---

### DON'T DO

- **Nie UIDs erfinden** – IDs immer aus `project.config.md` entnehmen; fehlt ein passender Code → nachfragen.
- **Nie Phasen überspringen** – kein `impl-mode` ohne bestätigten Plan und fehlschlagende Tests; kein `plan-mode` ohne bestätigte Spec.
- **Nie Spec-Status ändern** – `Draft → Active` oder `Active → Outdated` nur auf explizite Anfrage, nie automatisch.
- **Nie Architekturentscheidungen stillschweigend treffen** – bei unklaren Design- oder Technologiefragen immer nachfragen.

---

*Detailregeln: `workflow.instructions.md` (Phasen) · `specification.instructions.md` (Format) · `project.config.md` (IDs)*
