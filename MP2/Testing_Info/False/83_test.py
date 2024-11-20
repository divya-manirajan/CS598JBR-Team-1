import pytest
from Task_83_solution import starts_one_ends

def test_starts_one_ends():
    assert starts_one_ends(1) == 1
    assert starts_one_ends(2) == 18
    assert starts_one_ends(3) == 180
    assert starts_one_ends(4) == 1800
    assert starts_one_ends(5) == 18000
    assert starts_one_ends(6) == 180000
    assert starts_one_ends(7) == 1800000
    assert starts_one_ends(8) == 18000000
    assert starts_one_ends(9) == 180000000
    assert starts_one_ends(10) == 1800000000