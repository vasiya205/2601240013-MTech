import pytest
from hypothesis import given, strategies as st
import math

# Target function to test
def calculate_square_root(x: float) -> float:
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

# --- Pytest Unit Tests ---
def test_calculate_square_root_valid():
    assert calculate_square_root(4.0) == 2.0
    assert calculate_square_root(0.0) == 0.0

def test_calculate_square_root_negative():
    with pytest.raises(ValueError):
        calculate_square_root(-1.5)

# --- Hypothesis Property-Based Tests ---
@given(st.floats(min_value=0.0, max_value=1e6))
def test_calculate_square_root_properties(x):
    result = calculate_square_root(x)
    assert result >= 0.0
    assert abs((result * result) - x) < 1e-5
