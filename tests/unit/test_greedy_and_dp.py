from __future__ import annotations

from app.algorithms.dynamic_programming import dynamic_programming_optimization
from app.algorithms.greedy import greedy_priority_ranking
from app.models.vulnerability import Vulnerability


def test_greedy_ranking_orders_by_risk() -> None:
    vulns = [
        Vulnerability("V1", "Low", 3.0, 2.0, 3.0, 1),
        Vulnerability("V2", "High", 8.0, 9.0, 7.0, 5),
        Vulnerability("V3", "Medium", 6.0, 6.0, 6.0, 2),
    ]
    ranked = greedy_priority_ranking(vulns)
    assert ranked[0].vuln_id == "V2"
    assert ranked[-1].vuln_id == "V1"


def test_dynamic_programming_chooses_best_subset() -> None:
    vulns = [
        Vulnerability("A", "Issue A", 6.0, 9.0, 8.0, 3),
        Vulnerability("B", "Issue B", 7.0, 6.0, 7.0, 4),
        Vulnerability("C", "Issue C", 5.0, 4.0, 5.0, 2),
    ]
    budget = 5
    plan = dynamic_programming_optimization(vulns, budget)
    assert plan.total_cost <= budget
    assert set(item.vuln_id for item in plan.selected).issubset({"A", "B", "C"})


def test_budget_zero_returns_empty_plan() -> None:
    vulns = [Vulnerability("V9", "Issue", 5.0, 5.0, 5.0, 1)]
    plan = dynamic_programming_optimization(vulns, 0)
    assert plan.selected == []
    assert plan.total_cost == 0
