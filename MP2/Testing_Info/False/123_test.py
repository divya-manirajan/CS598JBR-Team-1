import pytest
from Task_123_solution import get_odd_collatz

def test_get_odd_collatz():
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]
    assert get_odd_collatz(5) == [1, 5]
    assert get_odd_collatz(12) == [1, 3, 5]
    assert get_odd_collatz(1) == [1]