# ASPICE SUP.2 – Verification

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an den Verifikationsprozess
gemäß ASPICE SUP.2. Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

## Anforderung

### Spec-Abdeckung wird automatisch verifiziert und Lücken werden sichtbar gemacht

**UID**: PROJ-SYS-005 \
**Status**: Draft

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.2, BP 1–5]

**Rationale**: Der SDD-Workflow erfüllt SUP.2 durch:
- `scripts/validate_specs.py`: prüft bidirektionale Traceability
  - Alle aktiven Spec-UIDs in `spec/` müssen durch `@spec:`-Annotationen referenziert sein
  - Alle `@spec:`-Annotationen müssen auf existierende UIDs zeigen
- CI-Workflow (`.github/workflows/ci.yml`): läuft bei jedem Push, bricht mit Exit 1 bei Lücke
- `spec-mode` / `plan-mode` / `impl-mode` als Phasen-Gate: kein Code ohne Spec-ID
- `Spec-Gate` in `copilot-instructions.md`: Copilot verweigert Code ohne gültige Spec-ID
