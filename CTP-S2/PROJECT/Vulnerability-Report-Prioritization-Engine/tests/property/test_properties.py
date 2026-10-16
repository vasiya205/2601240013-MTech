from __future__ import annotations

from hypothesis import given, strategies as st

from app.models.vulnerability import Vulnerability


@st.composite
def vulnerability_strategy(draw):
    return Vulnerability(
        vuln_id=f"V{draw(st.integers(min_value=1, max_value=1000)):03d}",
        title=draw(st.text(min_size=1, max_size=20)),
        severity=draw(st.floats(min_value=0, max_value=10, allow_nan=False, allow_infinity=False)),
        exploitability=draw(st.floats(min_value=0, max_value=10, allow_nan=False, allow_infinity=False)),
        asset_criticality=draw(st.floats(min_value=0, max_value=10, allow_nan=False, allow_infinity=False)),
        remediation_cost=draw(st.integers(min_value=1, max_value=20)),
    )


@given(vulnerability_strategy())
def test_generated_vulnerability_has_valid_range(vuln: Vulnerability) -> None:
    assert 0.0 <= vuln.risk_score <= 10.0
    assert vuln.remediation_cost > 0
    assert vuln.title
