---
description: Aktiviert Testebenen (Unit / Integration / Qualification) gemäß ASPICE SWE.5/6
---

# Testebenen aktivieren (SWE.5 / SWE.6)

Dieser Prompt aktiviert die strukturierten Testebenen für das Projekt.
Führe die folgenden Schritte durch:

## Schritt 1 – pytest.ini erweitern

Ergänze `pytest.ini` um separate Testpfade und Marker:

```ini
[pytest]
testpaths = tests/unit tests/integration tests/qualification
markers =
    unit: Unit-Test (ASPICE SWE.4)
    integration: Integrationstest (ASPICE SWE.5)
    qualification: Qualifikationstest (ASPICE SWE.6)
```

## Schritt 2 – conftest.py erweitern

Registriere die neuen Marker in `tests/conftest.py`:

```python
config.addinivalue_line("markers", "unit: Unit-Test (ASPICE SWE.4)")
config.addinivalue_line("markers", "integration: Integrationstest (ASPICE SWE.5)")
config.addinivalue_line("markers", "qualification: Qualifikationstest (ASPICE SWE.6)")
```

## Schritt 3 – TC-Codes in project.config.md eintragen

Die Codes `TC-U`, `TC-I`, `TC-Q` sind bereits in `specification.instructions.md`
(Abschnitt 7) definiert. Zähler in `project.config.md` prüfen:

| Code | Bedeutung | Nächste freie ID |
|------|-----------|-----------------|
| `TC-U` | Unit-Testfall | `PROJ-TC-U-001` |
| `TC-I` | Integrationstest | `PROJ-TC-I-001` |
| `TC-Q` | Qualifikationstest | `PROJ-TC-Q-001` |

## Schritt 4 – PROJ-SYS-008 auf Active setzen

In `spec/PROJ-SYS-008-aspice-swe5-swe6-testlevels.md`:
- `**Status**: Draft` → `**Status**: Active`
- Normtext aus lizenzierter ASPICE PAM einfügen (SWE.5 BP 1–6, SWE.6 BP 1–6)

## Schritt 5 – CHANGELOG.md aktualisieren

```markdown
## [Unreleased]

### Neue Anforderungen
- PROJ-SYS-008: ASPICE SWE.5/6 – Integrations- und Qualifikationstests aktiviert
```

## Schritt 6 – Ersten TC-Node erstellen

Beispiel für einen Unit-Testfall:

```markdown
### Funktion gibt korrektes Ergebnis zurück

**UID**: PROJ-TC-U-001 \
**Status**: Draft \
**Relations**: PROJ-BE-001

**Statement**: Given die Eingabe gültig ist,
When `process_data()` aufgerufen wird,
Then wird das erwartete Ergebnis zurückgegeben.
```

Test-Datei: `tests/unit/test_PROJ_TC_U_001.py`
