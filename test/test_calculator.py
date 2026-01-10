import pytest
from app.calculator import add, substraction, divide


@pytest.mark.regression
def test_add():
    assert add(2, 3) == 5


@pytest.mark.regression
def test_substraction():
    assert substraction(5, 2) == 3

@pytest.mark.regression
def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="divide by 0"):
        divide(10, 0)
