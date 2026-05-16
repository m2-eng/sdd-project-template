# @spec: PROJ-SYS-003
"""
Tests für Release-Pipeline-Robustheit (PROJ-SYS-003, SWE.4).
Red-Phase: PROJ-TC-002 bis PROJ-TC-005 schlagen fehl, bis release.yml gefixt ist.
PROJ-TC-001 besteht – dokumentiert bekanntes pytest-Exit-Code-Verhalten.
"""

import re
import subprocess
import sys
from pathlib import Path

import allure
import pytest

REPO_ROOT = Path(__file__).parents[2]
RELEASE_YML = REPO_ROOT / ".github" / "workflows" / "release.yml"


@pytest.mark.spec("PROJ-TC-001")
@allure.link("PROJ-TC-001", name="PROJ-TC-001")
@allure.title("[PROJ-TC-001] – pytest gibt Exit Code 5 zurück wenn keine Tests vorhanden")
def test_PROJ_TC_001_pytest_exits_with_code_5_on_empty_testdir(tmp_path):
    # @spec: PROJ-TC-001
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "--co",
            "-q",
            "--override-ini=addopts=",
            str(tmp_path),
        ],
        capture_output=True,
    )
    assert result.returncode == 5


@pytest.mark.spec("PROJ-TC-002")
@allure.link("PROJ-TC-002", name="PROJ-TC-002")
@allure.title("[PROJ-TC-002] – release.yml enthält Guard für leeres allure-results-Verzeichnis")
def test_PROJ_TC_002_release_yml_has_guard_for_empty_allure_results():
    # @spec: PROJ-TC-002
    content = RELEASE_YML.read_text(encoding="utf-8")
    assert "ls -A" in content, (
        "release.yml muss einen Guard für leeres allure-results/ enthalten "
        "(erwartet: 'ls -A' zur Prüfung ob Verzeichnis Dateien enthält)"
    )


@pytest.mark.spec("PROJ-TC-003")
@allure.link("PROJ-TC-003", name="PROJ-TC-003")
@allure.title("[PROJ-TC-003] – release.yml übergibt coverage.xml konditional an gh release create")
def test_PROJ_TC_003_release_yml_has_conditional_coverage_xml():
    # @spec: PROJ-TC-003
    content = RELEASE_YML.read_text(encoding="utf-8")
    assert re.search(r"\[ -f [\"']?.*coverage\.xml", content) is not None, (
        "release.yml muss coverage.xml konditional übergeben "
        "(erwartet: '[ -f ... coverage.xml' als Existenzprüfung vor Übergabe)"
    )


@pytest.mark.spec("PROJ-TC-004")
@allure.link("PROJ-TC-004", name="PROJ-TC-004")
@allure.title("[PROJ-TC-004] – release.yml installiert allure-commandline mit expliziter Versionsnummer")
def test_PROJ_TC_004_release_yml_allure_commandline_version_pinned():
    # @spec: PROJ-TC-004
    content = RELEASE_YML.read_text(encoding="utf-8")
    assert re.search(r"allure-commandline@\d+\.\d+\.\d+", content) is not None, (
        "release.yml muss allure-commandline mit fixierter Version installieren "
        "(erwartet: 'allure-commandline@X.Y.Z', z.B. allure-commandline@2.41.0)"
    )


@pytest.mark.spec("PROJ-TC-005")
@allure.link("PROJ-TC-005", name="PROJ-TC-005")
@allure.title("[PROJ-TC-005] – release.yml behandelt Exit Code 5 von pytest explizit")
def test_PROJ_TC_005_release_yml_handles_pytest_exit_code_5():
    # @spec: PROJ-TC-005
    content = RELEASE_YML.read_text(encoding="utf-8")
    assert "$? -eq 5" in content, (
        "release.yml muss Exit Code 5 von pytest explizit behandeln "
        "(erwartet: '|| [ $? -eq 5 ]' im Run-tests-Step)"
    )
