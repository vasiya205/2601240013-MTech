from __future__ import annotations

from pathlib import Path

import pytest

from app.data.loader import read_vulnerability_csv
from app.services.prioritization_service import PrioritizationEngine


@pytest.mark.parametrize("budget", [5, 10, 20])
def test_end_to_end_prioritization_for_common_budgets(budget: int) -> None:
    path = Path(__file__).resolve().parents[2] / "data" / "sample_vulnerabilities.csv"
    vulnerabilities = read_vulnerability_csv(path)
    engine = PrioritizationEngine(budget=budget)
    outcome = engine.analyze(vulnerabilities, budget=budget)
    assert outcome.total_risk > 0
    assert len(outcome.ranked_vulnerabilities) == len(vulnerabilities)
    assert outcome.remediation_plan.total_cost <= budget
