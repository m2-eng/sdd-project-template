# ASPICE SWE.1 – Software Requirements Analysis

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an den Software-Anforderungsprozess
gemäß ASPICE SWE.1. Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

## Anforderung

### Software-Anforderungen werden systematisch erfasst und rückverfolgt

**UID**: PROJ-SYS-001 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SWE.1, BP 1–8]

**Rationale**: Der SDD-Workflow erfüllt SWE.1 durch:
- Spec-Dateien in `spec/` (StrictDoc-Markdown, maschinenauswertbar)
- Eindeutige UIDs (`PROJ-[CODE]-NNN`) für jeden Requirement-Node
- `@spec`-Annotationen in `src/` und `tests/` für bidirektionale Traceability
- GitHub Issues mit `needs-statement`-Template als formaler Eingangskanal
- Workflow-Phasen `spec-mode` und `plan-mode` strukturieren Erfassung und Ableitung
