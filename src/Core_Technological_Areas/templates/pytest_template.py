# Example pytest_template.py
import pytest

def test_example():
    assert 1 + 1 == 2

def test_another_example():
    with pytest.raises(ZeroDivisionError):
        1 / 0
