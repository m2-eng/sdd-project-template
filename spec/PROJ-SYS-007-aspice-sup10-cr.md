# ASPICE SUP.10 – Change Request Management

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an das Change-Request-Management
gemäß ASPICE SUP.10. Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

## Anforderung

### Änderungsanforderungen werden formal erfasst, bewertet, freigegeben und rückverfolgt

**UID**: PROJ-SYS-007 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.10, BP 1–5]

**Rationale**: Der SDD-Workflow erfüllt SUP.10 durch:
- GitHub Issues mit `needs-statement`-Template als formaler CR-Eingangskanal
- CR-Status-Lifecycle via Labels: `cr-open` → `cr-assessed` → `cr-approved` → `cr-implemented`
- `setup-labels.ps1`: legt die 4 CR-Labels einmalig im Repository an
- Issue-Nummer wird in der Spec referenziert (`Rationale: GitHub: #NNN`)
- `spec-mode`: aus dem Issue wird eine formale Spec mit ACs abgeleitet
- `refactor-mode`: Feature-Drift oder Spec-Abweichungen starten neuen CR-Zyklus
