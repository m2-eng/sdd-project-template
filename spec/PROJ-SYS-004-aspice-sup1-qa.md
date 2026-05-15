# ASPICE SUP.1 – Quality Assurance

## Kontext

Dieser Spec-Node beschreibt die Anforderungen an den Qualitätssicherungsprozess
gemäß ASPICE SUP.1. Der Normtext ist nicht abgedruckt (kommerzielle Lizenz).
Das Projekt fügt den Normtext aus der lizenzierten ASPICE PAM-Version hier ein.

## Anforderung

### Qualitätssicherung wird systematisch durchgeführt und dokumentiert

**UID**: PROJ-SYS-004 \
**Status**: Active

**Statement**: TODO – Normtext hier einfügen: [ASPICE PAM, SUP.1, BP 1–6]

**Rationale**: Der SDD-Workflow erfüllt SUP.1 durch:
- `review-mode`: strukturierter Review gegen Spec (AC-Abgleich, Traceability, State-of-the-Art, Security)
- Review-Dokumente in `docs/review/YYYY-MM-DD_[Spec-ID]_review.md`
- Review Agent prüft jeden AC, dokumentiert Abweichungen tabellarisch
- `review.instructions.md` definiert verpflichtende Prüfpunkte (OWASP, Lizenzkonflikt, State-of-the-Art)
- Keine Implementierung ohne vorherigen Review bei Abweichungen (`refactor-mode`)
