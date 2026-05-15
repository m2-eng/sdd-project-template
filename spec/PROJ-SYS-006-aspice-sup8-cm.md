# ASPICE SUP.8 – Configuration Management

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an das Konfigurationsmanagement
gemäß ASPICE SUP.8. Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

## Anforderung

### Baselines werden systematisch erstellt, freigegeben und als Artefakte veröffentlicht

**UID**: PROJ-SYS-006 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.8, BP 1–7]

**Rationale**: Der SDD-Workflow erfüllt SUP.8 durch:
- Git-Tag `baseline/vX.Y` als unveränderlicher Baseline-Identifier
- `workflow.instructions.md` Phase 7 (baseline-mode): Checkliste, Naming-Konvention, Freigabeprozess
- `CHANGELOG.md` mit Spec-ID-Referenzen als Versionshistorie
- CD-Pipeline (`release.yml`): erzeugt GitHub Release mit Test-Report, Traceability-Matrix, StrictDoc-Export
- Pre-Release-Kennzeichnung automatisch aus Tag-Suffix (`-alpha.N` / `-beta.N`)
- Git-History + Spec-Dateien = vollständiger Audit-Trail
