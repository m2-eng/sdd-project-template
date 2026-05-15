---
applyTo: "tests/**"
---

# Test-Richtlinien (test-mode)

## Test-Stack

| Tool | Zweck | Befehl |
|------|-------|--------|
| `pytest` | Test-Runner | `pytest tests/` |
| `pytest-cov` | Code Coverage | `pytest --cov=src --cov-report=xml --cov-report=html` |
| `allure-pytest` | HTML-Reports + Traceability | `pytest --alluredir=docs/test-reports/allure-results` |

Installation (nur innerhalb aktivierter `.venv` – **Pflicht**):

```powershell
.venv\Scripts\Activate.ps1
pip install pytest pytest-cov allure-pytest
```

---

## Namenskonvention

```
[SCAN-TC-NNN] – [Verhalten bei Szenario]
```

Beispiel: `[SCAN-TC-001] – Barcode-Scan gibt dekodierten Wert zurück`

## Annotationsformat

Jeder Test erhält **drei Annotationen** – Kommentar (SSOT) + pytest-Marker (maschinenauswertbar) + Allure-Link (Report):

```python
import pytest
import allure

@pytest.mark.spec("SCAN-TC-001")
@allure.link("SCAN-TC-001", name="SCAN-TC-001")
@allure.title("[SCAN-TC-001] – Barcode-Scan gibt dekodierten Wert zurück")
def test_SCAN_TC_001_barcode_returns_decoded_value():
    # @spec: SCAN-TC-001
    ...
```

Minimal (ohne Allure, wenn noch nicht installiert):

```python
import pytest

@pytest.mark.spec("SCAN-TC-001")
def test_SCAN_TC_001_barcode_returns_decoded_value():
    # @spec: SCAN-TC-001
    ...
```

Der `pytest.mark.spec`-Marker muss in `conftest.py` registriert werden:

```python
# conftest.py (Projektroot oder tests/)
import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "spec(uid): Links test to a Spec-Node UID (e.g. SCAN-TC-001)"
    )
```

---

## Granularität

- Eine Testfunktion deckt genau **einen** TC-Node ab
- Happy Path und Error Path sind separate Testfunktionen mit eigenen TC-IDs

## Red-Phase

Tests müssen initial **fehlschlagen**. Kein Produktionscode in Testdateien.
Wenn ein Test sofort grün ist ohne Implementierung: Testlogik prüfen.

## DON'T DO

- Kein Test ohne `@spec: SCAN-TC-NNN`-Kommentar
- Kein Test ohne `@pytest.mark.spec('SCAN-TC-NNN')`-Marker
- Kein Test ohne zugehörigen TC-Node in `spec/`
- Kein Produktionscode (kein `import src/...` außer dem zu testenden Modul)
- Keine Tests für Verhalten das nicht in der Spec steht
