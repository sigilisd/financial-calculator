import pytest
from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax


def test_calculate_simple_interest_correct():
    assert calculate_simple_interest(1000, 5, 2) == 100.0
    assert calculate_simple_interest(500, 10, 3) == 150.0


def test_calculate_simple_interest_zero():
    assert calculate_simple_interest(0, 5, 2) == 0.0
    assert calculate_simple_interest(1000, 0, 2) == 0.0
    assert calculate_simple_interest(1000, 5, 0) == 0.0


def test_calculate_simple_interest_negative():
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(-1000, 5, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(1000, -5, 2)
    with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
        calculate_simple_interest(1000, 5, -2)


def test_calculate_compound_interest_correct():
    assert abs(calculate_compound_interest(1000, 5, 2, 1) - 1102.5) < 0.1
    assert abs(calculate_compound_interest(1000, 10, 1, 2) - 1102.5) < 0.1


def test_calculate_compound_interest_zero():
    assert calculate_compound_interest(0, 5, 2, 1) == 0.0
    assert calculate_compound_interest(1000, 0, 2, 1) == 1000.0
    assert calculate_compound_interest(1000, 5, 0, 1) == 1000.0


def test_calculate_compound_interest_negative():
    with pytest.raises(ValueError):
        calculate_compound_interest(-1000, 5, 2, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, -5, 2, 1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, -2, 1)


def test_calculate_compound_interest_invalid_n():
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, 0)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, -1)
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, 1.5)


def test_calculate_tax_correct():
    assert calculate_tax(1000, 20) == 200.0
    assert calculate_tax(500, 10) == 50.0


def test_calculate_tax_zero():
    assert calculate_tax(0, 20) == 0.0
    assert calculate_tax(1000, 0) == 0.0


def test_calculate_tax_invalid_rate():
    with pytest.raises(ValueError):
        calculate_tax(1000, -1)
    with pytest.raises(ValueError):
        calculate_tax(1000, 101)

