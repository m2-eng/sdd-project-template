# Review-Dokument – PROJ-SYS-010 / PROJ-SYS-011 / PROJ-TC-006–008

**Datum**: 2026-05-16  
**Reviewer**: Review-Agent (review-mode)  
**Scope**: PROJ-SYS-010, PROJ-SYS-011, PROJ-TC-006, PROJ-TC-007, PROJ-TC-008  
**Geprüfte Dateien**:
- `.github/workflows/release.yml`
- `tests/unit/test_release_pipeline.py`
- `spec/aspice-compliance.md`
- `.github/instructions/workflow.instructions.md`
- `.github/instructions/review.instructions.md`
- `.github/project.config.md`

---

## 1 – Spec-Abgleich

### PROJ-SYS-010 – Review-Dokumente committed und als ZIP veröffentlicht

Statement (Given/When/Then):
- **Given**: Review-Bericht unter `docs/review/YYYY-MM-DD_[Spec-ID]_review.md` erstellt
- **When**: neue Baseline (`baseline/vX.Y`) wird veröffentlicht
- **Then**: alle Review-Dokumente aus `docs/review/` sind committed und als `review-reports-vX.Y.zip` dem GitHub Release angehängt

| Spec-ID | AC | Status | Abweichung |
|---------|----|--------|------------|
| PROJ-SYS-010 | AC1: `docs/review/*.md` werden in ZIP gepackt | ✅ | – |
| PROJ-SYS-010 | AC2: Leeres `docs/review/` bricht Release nicht ab | ✅ | – |
| PROJ-SYS-010 | AC3: ZIP-Name ist `review-reports-vX.Y.zip` (versioniert) | ✅ | – |
| PROJ-TC-006 | release.yml enthält ZIP-Schritt mit Muster `review-reports-` | ✅ | – |
| PROJ-TC-007 | Guard für leeres `docs/review/` (find-basierte Prüfung) | ✅ | – |
| PROJ-TC-008 | ZIP-Dateiname enthält versionierten `review-reports-`-Präfix | ✅ | – |

**Belege:**

- AC1 → `release.yml:67`: `zip -j "review-reports-${VERSION}.zip" docs/review/*.md`
- AC2 → `release.yml:66`: `if find docs/review -name "*.md" -maxdepth 1 | grep -q .; then`
  – Wenn `docs/review/` leer oder nicht vorhanden ist, gibt `find | grep -q .` Exit 1 zurück → ZIP-Block wird übersprungen ✅
- AC3 → `release.yml:67–68`: `VERSION="${TAG#baseline/}"` → für Tag `baseline/v1.0` ergibt sich `review-reports-v1.0.zip` ✅
- TC-006 → `re.search(r"zip\b.*review-reports-", content)` matcht `release.yml:67` ✅
- TC-007 → `re.search(r"find\s+docs/review", content)` matcht `release.yml:66` ✅
- TC-008 → Regex mit Alternation matcht `review-reports-${VERSION}` (VERS in VERSION) ✅

### PROJ-SYS-011 – SUP.4 Joint Review Placeholder

| Spec-ID | AC | Status | Abweichung |
|---------|----|--------|------------|
| PROJ-SYS-011 | Placeholder-Node vorhanden; Statement = TODO (kein AC implementierbar) | ✅ | – |

**Beleg**: `spec/aspice-compliance.md:133` – UID, Status Draft, Rationale verweist auf PROJ-SYS-010 ✅

---

## 2 – Traceability

| Annotation | Datei:Zeile | Status |
|------------|-------------|--------|
| `# @spec: PROJ-SYS-010` | `release.yml:64` (Shell-Kommentar im `run:`-Block) | ✅ |
| `# @spec: PROJ-TC-006` | `tests/unit/test_release_pipeline.py:92` | ✅ |
| `# @spec: PROJ-TC-007` | `tests/unit/test_release_pipeline.py:104` | ✅ |
| `# @spec: PROJ-TC-008` | `tests/unit/test_release_pipeline.py:116` | ✅ |
| `**Relations**: PROJ-SYS-010` | `spec/aspice-compliance.md:338` (PROJ-TC-006) | ✅ |
| `**Relations**: PROJ-SYS-010` | `spec/aspice-compliance.md:356` (PROJ-TC-007) | ✅ |
| `**Relations**: PROJ-SYS-010` | `spec/aspice-compliance.md:374` (PROJ-TC-008) | ✅ |
| `**Relations**: PROJ-SYS-011` | `spec/aspice-compliance.md:150` (PROJ-SYS-010) | ✅ |

**Traceability-Lücken**: Eine (siehe Befund B1 unten).

**Hinweis**: Die `@spec: PROJ-SYS-010`-Annotation liegt bei `release.yml:64` innerhalb eines YAML-`run:`-Blocks als Shell-Kommentar. `validate_specs.py` scannt `.yml`-Dateien mit Regex auf Dateiinhalt (`ANNOTATION_DIRS = [... ".github" ...]`, `ANNOTATION_EXTENSIONS = {... ".yml" ...}`) – die Annotation ist maschinell auswertbar. Kein Handlungsbedarf.

---

## 3 – State-of-the-Art

| Datei:Zeile | Muster | Bewertung |
|-------------|--------|-----------|
| `release.yml:67` | `zip -j` (junks paths – keine Verzeichnisstruktur im ZIP) | ℹ️ Kein Spec-Verstoß; Spec schreibt Struktur nicht vor. Flat-ZIP ist für Review-Reports ausreichend. |
| `release.yml:75–77` | `$COVERAGE_ARG` und `$REVIEW_ARG` unquoted in `gh release create` | ℹ️ Werte kommen aus kontrollierten Templates; git-Tagnamen können keine Shell-Sonderzeichen enthalten, die den Trigger `baseline/v*` passieren. Kein akutes Risiko, aber Quote-Hygiene ist Best Practice. Kein Spec-Verstoß. |

Keine veralteten APIs, deprecated Patterns oder Framework-Anti-Patterns gefunden.

---

## 4 – Lizenzkonflikte

Keine neuen externen Abhängigkeiten eingeführt. Kein Prüfbedarf.

---

## 5 – Security (OWASP Top 10)

- **A03 (Injection)**: `$REVIEW_ARG` und `$COVERAGE_ARG` werden unquoted an `gh release create` übergeben (`release.yml:75–77`). Werte sind entweder leer oder aus statischen Templates abgeleitet (`review-reports-${VERSION}.zip`). `VERSION` kommt aus `${GITHUB_REF_NAME#baseline/}`, begrenzt durch den Workflow-Trigger `tags: - 'baseline/v*'`. Git-Tagnamen erlauben keine Shell-Metazeichen, die den Trigger passieren würden. Praktisches Risiko: **nicht vorhanden**.
- **A08 (Software and Data Integrity)**: `allure-commandline@2.41.0` bleibt gepinnt (`release.yml:32`) ✅
- Keine hartcodierten Credentials oder Secrets gefunden.
- Keine unsicheren Abhängigkeiten eingeführt.

---

## 6 – Befunde

### B1 – Traceability-Lücke: Querverweis in `review.instructions.md` fehlt

| Feld | Wert |
|------|------|
| **Datei** | `.github/instructions/review.instructions.md` |
| **Erwartet** | Explizite Referenz auf PROJ-SYS-010 (Review-Dokumente committed; CD-Pipeline erzeugt ZIP) |
| **Gefunden** | Kein Treffer für `PROJ-SYS-010` im gesamten Dateiinhalt |
| **Kategorie** | Traceability-Lücke |
| **Auswirkung** | Kein Laufzeit-Fehler; `review.instructions.md` ist ohne Verweis auf die Commit- und ZIP-Pflicht unvollständig als Prozessdokument |

Der Task-Scope listet `review.instructions.md – Querverweis ergänzt` als geänderte Datei. Die Änderung ist im Dateiinhalt nicht auffindbar.

### B2 – Spec-Status PROJ-SYS-010 und PROJ-SYS-011 bleiben Draft

| Feld | Wert |
|------|------|
| **Datei:Zeile** | `spec/aspice-compliance.md:134` (PROJ-SYS-011), `spec/aspice-compliance.md:149` (PROJ-SYS-010) |
| **Befund** | Beide Nodes haben `**Status**: Draft` |
| **Auswirkung** | `validate_specs.py` ohne `--include-draft` ignoriert Draft-Nodes → keine Traceability-Prüfung gegen PROJ-SYS-010/011. Außerdem blockiert Draft-Status den baseline-mode: "Alle im Scope befindlichen Nodes haben `**Status**: Active`" (`workflow.instructions.md`, Phase 7) |
| **Kategorie** | Prozess-Blocker für zukünftige Baseline (kein Code-Defekt) |

---

## 7 – Review-Ergebnis Gesamttabelle

| Spec-ID | AC / Prüfpunkt | Status | Abweichung |
|---------|----------------|--------|------------|
| PROJ-SYS-010 | AC1: `docs/review/*.md` in ZIP gepackt | ✅ | – |
| PROJ-SYS-010 | AC2: Leeres `docs/review/` bricht Release nicht ab | ✅ | – |
| PROJ-SYS-010 | AC3: ZIP-Name `review-reports-vX.Y.zip` (versioniert) | ✅ | – |
| PROJ-SYS-011 | Placeholder vorhanden, kein implementierbarer AC | ✅ | – |
| PROJ-TC-006 | ZIP-Schritt für Review-Berichte in release.yml | ✅ | – |
| PROJ-TC-007 | Guard für leeres `docs/review/` implementiert | ✅ | – |
| PROJ-TC-008 | Versionierter ZIP-Dateiname mit Tag-Referenz | ✅ | – |
| Traceability | `@spec: PROJ-SYS-010` in release.yml | ✅ | – |
| Traceability | `@spec: PROJ-TC-006/007/008` in Testfunktionen | ✅ | – |
| Traceability | `**Relations**: PROJ-SYS-010` in TC-006/007/008 | ✅ | – |
| Traceability | Querverweis PROJ-SYS-010 in review.instructions.md | ❌ | B1: Referenz fehlt |
| Prozess | Spec-Status PROJ-SYS-010 = Active | ❌ | B2: Status ist Draft |
| Prozess | Spec-Status PROJ-SYS-011 = Active | ❌ | B2: Status ist Draft |
| State-of-the-Art | Keine veralteten Patterns | ✅ | – |
| Security | OWASP A03/A08 | ✅ | Kein kritisches Risiko |
| Lizenz | Keine neuen Abhängigkeiten | ✅ | – |

---

## 8 – Empfehlung

**→ refactor-mode** für die beiden offenen Befunde:

| Befund | Aktion |
|--------|--------|
| **B1** | `review.instructions.md` – Abschluss-Schritt um Verweis auf PROJ-SYS-010 ergänzen: Review-Dokument committen → CD-Pipeline erzeugt `review-reports-vX.Y.zip` gemäß PROJ-SYS-010 |
| **B2** | `spec/aspice-compliance.md` – PROJ-SYS-010 und PROJ-SYS-011 auf `**Status**: Active` setzen (nach User-Bestätigung), damit `validate_specs.py` die Traceability prüft und baseline-mode zulässig wird |

Die Implementierung von PROJ-SYS-010 ist vollständig und korrekt. Nach Behebung von B1 und B2 ist kein weiterer Implementierungs-Aufwand erforderlich.
