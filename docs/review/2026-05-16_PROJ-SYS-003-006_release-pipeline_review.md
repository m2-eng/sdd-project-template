# Review-Ergebnis – PROJ-SYS-003 / PROJ-SYS-006 – Release Pipeline – 2026-05-16

**Scope**: GitHub Issue #3 – "Release Automation have to be fixed"  
**Geprüfte Dateien**:
- `.github/workflows/release.yml`
- `pytest.ini`
- `spec/aspice-compliance.md` (PROJ-SYS-003, PROJ-SYS-006)
- `requirements-dev.txt`

---

## 1 – Spec-Abgleich

### PROJ-SYS-003 (SWE.4 – Software Unit Verification)

Rationale-Punkte aus der Spec:

| Rationale-Punkt | Status | Abweichung / Befund |
|---|---|---|
| `pytest` als Test-Runner mit `pytest.ini`-Konfiguration | ✅ | `pytest.ini` vorhanden |
| `pytest-cov` für Code-Coverage (HTML + XML) | ✅ | `pytest.ini:4–7`: alle Coverage-Reports konfiguriert |
| `allure-pytest` für strukturierte Test-Reports | ✅ | `pytest.ini:8`: `--alluredir` konfiguriert |
| `conftest.py` registriert Custom-Marker `@pytest.mark.spec` | ✅ | `tests/conftest.py:3–6` |
| CD-Pipeline veröffentlicht Test-Reports als GitHub-Release-Artefakte | ❌ | Pipeline bricht bei Exit Code 5 ab (kein Test-Run → keine Artefakte). Siehe **BUG-01** |

### PROJ-SYS-006 (SUP.8 – Configuration Management)

Rationale-Punkte aus der Spec:

| Rationale-Punkt | Status | Abweichung / Befund |
|---|---|---|
| Git-Tag `baseline/vX.Y` als Baseline-Identifier | ✅ | `release.yml:7`: Trigger `baseline/v*` |
| CD-Pipeline erzeugt GitHub Release mit Test-Report, Traceability-Matrix, StrictDoc-Export | ❌ | Pipeline bricht vor `gh release create` ab. Artefakt `coverage.xml` fehlt. Siehe **BUG-01**, **BUG-02**, **BUG-03** |
| Pre-Release-Kennzeichnung automatisch aus Tag-Suffix | ✅ | `release.yml:48–50`: `-alpha` / `-beta` → `--prerelease` |
| CHANGELOG als Versionshistorie | ✅ | `CHANGELOG.md` vorhanden (kein Pipeline-Enforcement, Spec fordert kein CI-Gate) |

---

## 2 – Traceability

| Datei | Annotation | Existiert UID? | Status |
|---|---|---|---|
| `.github/workflows/release.yml:1` | `@spec: PROJ-SYS-003` | ✅ (aspice-compliance.md, Zeile ~75) | OK |
| `.github/workflows/release.yml:2` | `@spec: PROJ-SYS-006` | ✅ (aspice-compliance.md, Zeile ~136) | OK |

**Traceability-Lücken**: keine – alle `@spec:`-Annotationen zeigen auf existierende UIDs.

---

## 3 – State-of-the-Art

| Datei:Zeile | Veraltetes / problematisches Muster | Empfohlene Alternative |
|---|---|---|
| `release.yml:33` | `npm install -g allure-commandline` ohne Versions-Pin | Versioniert pinnen, z. B. `npm install -g allure-commandline@2.30.0`, oder festes Docker-Image mit vorinstalliertem Allure |

---

## 4 – Lizenzkonflikte

Projekt-Lizenz: **AGPL-3.0**

| Package | Quelle | Lizenz | Konfliktrisiko | Empfehlung |
|---|---|---|---|---|
| `strictdoc` | `requirements-dev.txt` | AGPL-3.0 | Kein Konflikt | – |
| `pytest` | `requirements-dev.txt` | MIT | Kein Konflikt | – |
| `pytest-cov` | `requirements-dev.txt` | MIT | Kein Konflikt | – |
| `allure-pytest` | `requirements-dev.txt` | Apache-2.0 | Kein Konflikt | – |
| `allure-commandline` | `release.yml:33` (npm) | Apache-2.0 | Kein Konflikt | – |

**Befund**: Keine Lizenzkonflikte identifiziert.

---

## 5 – Security (OWASP Top 10)

| Datei:Zeile | Befund | OWASP-Kategorie | Bewertung |
|---|---|---|---|
| `release.yml:33` | `npm install -g allure-commandline` ohne Versions-Pin → unkontrolliertes Update-Risiko | A08:2021 – Software and Data Integrity Failures | Medium – Supply-Chain-Risiko |
| `release.yml:46–54` | `TAG="${GITHUB_REF_NAME}"` – Variable wird in Shell-Kontext gesetzt; in allen Verwendungen korrekt gequotet (`"$TAG"`) | A03:2021 – Injection | ✅ Kein Befund |
| `release.yml:10–11` | `permissions: contents: write` – minimale, notwendige Berechtigung | – | ✅ Kein Befund |
| `release.yml:45` | `GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}` – korrekt als Env-Variable (nicht inline im Shell-Skript interpoliert) | A02:2021 – Cryptographic / Secrets Exposure | ✅ Kein Befund |

---

## Detaillierte Befunde

### BUG-01 ❌ (Kritisch) – Exit Code 5: Kein Test-Collection-Handling

**Datei:Zeile**: `release.yml:30`  
**Spec**: PROJ-SYS-003, PROJ-SYS-006  

```yaml
- name: Run tests
  run: python -m pytest
```

`pytest` gibt Exit Code 5 zurück wenn keine Tests gesammelt werden (`no tests ran`).
Das Template-Projekt hat nur Platzhalter-`README.md` in `tests/unit/`, `tests/integration/`, `tests/qualification/`.
→ Die Pipeline bricht hier ab, bevor irgendein Artefakt erzeugt wird.

**Empfehlung**: Exit Code 5 explizit tolerieren. Optionen:
- `python -m pytest || [ $? -eq 5 ]`
- `pytest --exit-zero` (maskiert aber auch echte Fehler – nicht empfohlen)
- Conditional step mit `continue-on-error: true` und nachgelagerter Auswertung

---

### BUG-02 ❌ (Hoch) – Allure-Generate auf leerem Verzeichnis (Folgefehler)

**Datei:Zeile**: `release.yml:34–35`  
**Spec**: PROJ-SYS-003  

```yaml
- name: Generate Allure report
  run: allure generate docs/test-reports/allure-results -o docs/test-reports/allure-report --clean
```

Wenn pytest mit Exit Code 5 abbricht (BUG-01) oder keine Allure-Ergebnisse erzeugt (leere Test-Suite), ist `docs/test-reports/allure-results/` leer oder nicht vorhanden.
`allure generate` schlägt in diesem Fall fehl (Exit Code != 0).

**Empfehlung**: Guard-Bedingung vor `allure generate`:
```yaml
run: |
  if [ -d docs/test-reports/allure-results ] && [ "$(ls -A docs/test-reports/allure-results)" ]; then
    allure generate docs/test-reports/allure-results -o docs/test-reports/allure-report --clean
  else
    mkdir -p docs/test-reports/allure-report
    echo "No test results found." > docs/test-reports/allure-report/index.html
  fi
```

---

### BUG-03 ❌ (Hoch) – Fehlende Artefakt-Datei `coverage.xml` (Folgefehler)

**Datei:Zeile**: `release.yml:54`  
**Spec**: PROJ-SYS-006  

```yaml
gh release create "$TAG" \
  ...
  docs/test-reports/coverage.xml
```

`docs/test-reports/coverage.xml` wird von `pytest-cov` erzeugt. Wenn pytest nicht läuft (BUG-01), existiert die Datei nicht → `gh release create` schlägt fehl.

**Empfehlung**: Datei-Existenz prüfen oder `coverage.xml` in `allure-report.zip` einschließen statt separat anzuhängen.

---

### BUG-04 ⚠️ (Medium – Security) – Kein Versions-Pin für `allure-commandline`

**Datei:Zeile**: `release.yml:33`  

```yaml
- name: Install Allure CLI
  run: npm install -g allure-commandline
```

Kein Versions-Pin → bei jedem Pipeline-Run wird die aktuell neueste Version gezogen.
OWASP A08:2021 (Software and Data Integrity Failures): Unkontrollierte transitive Updates können kompromittierte Versionen einschleusen.

**Empfehlung**: Version pinnen: `npm install -g allure-commandline@2.30.0`

---

### BUG-05 ⚠️ (Medium) – `--cov=src` auf leerem `src/`-Verzeichnis

**Datei:Zeile**: `pytest.ini:4`  

```ini
--cov=src
```

`src/` enthält nur `.gitkeep` – kein Python-Paket. `pytest-cov` gibt `CoverageWarning: No data was collected` aus und kann mit Exit Code != 0 beenden, wenn `src/__init__.py` fehlt und `--cov-fail-under` gesetzt ist (aktuell nicht, aber fragil).

**Empfehlung**: `src/__init__.py` oder Mindest-Platzhaltermodul anlegen, oder Coverage-Warnung explizit suppressen (`--no-cov` bis erstes Modul vorhanden, gesteuert per CI-Variable).

---

## Review-Ergebnis-Tabelle

| Spec-ID | Rationale-Punkt / AC | Status | Abweichung |
|---|---|---|---|
| PROJ-SYS-003 | pytest als Test-Runner mit `pytest.ini` | ✅ | – |
| PROJ-SYS-003 | pytest-cov für Coverage (HTML + XML) | ✅ | – |
| PROJ-SYS-003 | allure-pytest für Test-Reports | ✅ | – |
| PROJ-SYS-003 | conftest.py mit Custom-Marker | ✅ | – |
| PROJ-SYS-003 | CD-Pipeline veröffentlicht Test-Reports als Artefakte | ❌ | BUG-01: Exit Code 5 bricht Pipeline ab. BUG-02: allure generate schlägt fehl. |
| PROJ-SYS-006 | Git-Tag `baseline/vX.Y` als Trigger | ✅ | – |
| PROJ-SYS-006 | GitHub Release mit Test-Report, Traceability, StrictDoc | ❌ | BUG-01, BUG-03: Pipeline bricht vor `gh release create` ab |
| PROJ-SYS-006 | Pre-Release-Kennzeichnung aus Tag-Suffix | ✅ | – |
| PROJ-SYS-006 | CHANGELOG als Versionshistorie | ✅ | – |

**Traceability-Lücken**: keine

**Security**: BUG-04 – `allure-commandline` ohne Versions-Pin (OWASP A08)

**State-of-the-Art**: BUG-04 – kein Version-Pin für npm-Paket

---

## Empfehlung

→ **refactor-mode** mit folgenden priorisierten Befunden:

| Priorität | Bug | Datei:Zeile | Maßnahme |
|---|---|---|---|
| P1 | BUG-01 | `release.yml:30` | Exit Code 5 von pytest tolerieren |
| P1 | BUG-02 | `release.yml:34–35` | Guard-Bedingung vor `allure generate` |
| P1 | BUG-03 | `release.yml:54` | `coverage.xml`-Existenz absichern vor `gh release create` |
| P2 | BUG-04 | `release.yml:33` | `allure-commandline` mit Versions-Pin |
| P2 | BUG-05 | `pytest.ini:4` | `src/__init__.py` oder Coverage-Guard für leeres Template |
