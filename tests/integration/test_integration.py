from __future__ import annotations

from pathlib import Path

import pytest

from app.data.loader import load_multiple_csv_files, read_vulnerability_csv
from app.data.validators import DuplicateVulnerabilityError
from app.services.prioritization_service import PrioritizationEngine


def test_csv_loader_and_engine_integration() -> None:
    path = Path(__file__).resolve().parents[2] / "data" / "sample_vulnerabilities.csv"
    vulnerabilities = read_vulnerability_csv(path)
    assert len(vulnerabilities) == 10

    engine = PrioritizationEngine(budget=15.0)
    outcome = engine.analyze(vulnerabilities, budget=15.0)
    assert len(outcome.ranked_vulnerabilities) == 10
    assert outcome.remediation_plan.total_cost <= 15.0


def test_multiple_csv_inputs_are_supported(tmp_path: Path) -> None:
    path = Path(__file__).resolve().parents[2] / "data" / "sample_vulnerabilities.csv"
    second = tmp_path / "additional_vulnerabilities.csv"
    second.write_text(
        "vuln_id,title,severity,exploitability,asset_criticality,remediation_cost,category,affected_asset\n"
        "CVE-2024-2001,Secondary issue,6.0,5.0,7.0,2,Test,Host\n",
        encoding="utf-8",
    )

    combined = load_multiple_csv_files([path, second])
    assert len(combined) == 11

    with pytest.raises(DuplicateVulnerabilityError):
        load_multiple_csv_files([path, path])
