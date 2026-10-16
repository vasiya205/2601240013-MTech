from __future__ import annotations

import runpy
import sys
import types
from pathlib import Path

from app import PrioritizationEngine
from app.algorithms import dynamic_programming_optimization, greedy_priority_ranking
from app.data.validators import validate_record
from app.models import RemediationPlan, Vulnerability
from app.strategies import WeightedRiskScoringStrategy, calculate_risk_score
from app.strategies.base import PRIORITY_LEVELS, RiskScoringStrategy, apply_scoring
from app.utils.context_manager import CSVResourceManager


class DummyStrategy(RiskScoringStrategy):
    def score(self, vulnerability: Vulnerability) -> float:
        return float(vulnerability.risk_score) + 1.0


def test_vulnerability_metadata_and_plan_helpers() -> None:
    vuln = Vulnerability(
        vuln_id="V909",
        title="Host exploit",
        severity=9.0,
        exploitability=8.0,
        asset_criticality=10.0,
        remediation_cost=5,
    )

    assert vuln.priority_level == "Critical"
    assert "high priority" in vuln.explanation.lower()
    assert PRIORITY_LEVELS(6.0) == "High"
    assert PRIORITY_LEVELS(3.5) == "Low"
    assert apply_scoring([vuln], lambda item: item.risk_score) == [8.95]
    assert calculate_risk_score(vuln) == 8.95

    strategy = DummyStrategy()
    assert strategy.score_many([vuln]) == [9.95]
    assert isinstance(PrioritizationEngine(), PrioritizationEngine)
    assert greedy_priority_ranking([vuln])[0].vuln_id == "V909"
    assert dynamic_programming_optimization([vuln], 10.0).selected == [vuln]
    assert WeightedRiskScoringStrategy().score(vuln) == 8.95

    plan = RemediationPlan([vuln], budget=10.0)
    assert plan.remaining_budget == 5.0
    assert plan.selected_ids == ["V909"]
    assert plan.item_count == 1


def test_csv_resource_manager_handles_file_access(tmp_path: Path) -> None:
    target = tmp_path / "example.csv"
    target.write_text("vuln_id,title\nV1,Test\n", encoding="utf-8")

    with CSVResourceManager(target) as handle:
        assert "V1" in handle.read()

    cleaned = validate_record({
        "vuln_id": "V2",
        "title": "Sample",
        "severity": "4",
        "exploitability": "3",
        "asset_criticality": "5",
        "remediation_cost": "2",
        "category": "Test",
        "affected_asset": "Host",
    })
    assert cleaned["title"] == "Sample"


def test_main_module_entrypoint(monkeypatch) -> None:
    stub = types.ModuleType("app.ui.dashboard")
    stub.run_dashboard = lambda: None
    monkeypatch.setitem(sys.modules, "app.ui.dashboard", stub)
    runpy.run_path(str(Path(__file__).resolve().parents[2] / "app" / "main.py"), run_name="__main__")
