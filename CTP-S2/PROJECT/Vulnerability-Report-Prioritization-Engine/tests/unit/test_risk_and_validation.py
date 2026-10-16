from __future__ import annotations

import pytest

from app.data.validators import CSVValidationError, DuplicateVulnerabilityError, ValidationError, validate_record
from app.models.vulnerability import Vulnerability
from app.strategies.base import calculate_risk_score


def test_risk_calculation_matches_formula() -> None:
    vuln = Vulnerability(
        vuln_id="V001",
        title="Test issue",
        severity=9.0,
        exploitability=8.0,
        asset_criticality=10.0,
        remediation_cost=5,
    )
    assert calculate_risk_score(vuln) == 8.95


def test_risk_is_bounded_between_zero_and_ten() -> None:
    vuln = Vulnerability("V002", "Test", 10.0, 10.0, 10.0, 3)
    assert 0.0 <= vuln.risk_score <= 10.0


def test_validate_record_accepts_valid_input() -> None:
    record = {
        "vuln_id": "V123",
        "title": "Sample issue",
        "severity": "8.0",
        "exploitability": "7.5",
        "asset_criticality": "9.0",
        "remediation_cost": "3",
        "category": "Injection",
        "affected_asset": "API",
    }
    cleaned = validate_record(record)
    assert cleaned["vuln_id"] == "V123"
    assert cleaned["severity"] == 8.0


def test_validation_rejects_bad_ranges() -> None:
    with pytest.raises(ValidationError):
        validate_record({
            "vuln_id": "V444",
            "title": "Bad range",
            "severity": "11",
            "exploitability": "2",
            "asset_criticality": "4",
            "remediation_cost": "5",
            "category": "Test",
            "affected_asset": "Host",
        })


def test_validation_rejects_empty_id() -> None:
    with pytest.raises(ValidationError):
        validate_record({
            "vuln_id": "",
            "title": "Issue",
            "severity": "5",
            "exploitability": "5",
            "asset_criticality": "5",
            "remediation_cost": "1",
            "category": "Test",
            "affected_asset": "Host",
        })


def test_validation_rejects_missing_columns() -> None:
    with pytest.raises(CSVValidationError):
        from app.data.validators import validate_required_columns
        validate_required_columns(["vuln_id", "title"])


def test_duplicate_error_raised() -> None:
    with pytest.raises(DuplicateVulnerabilityError):
        from app.data.validators import ensure_unique_ids
        ensure_unique_ids([{"vuln_id": "V001"}, {"vuln_id": "V001"}])
