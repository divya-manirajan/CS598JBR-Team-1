import pytest
from Task_100_solution import make_a_pile

def test_make_a_pile_simple():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_edge():
    assert make_a_pile(1) == [1]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

def test_make_a_pile_large():
    assert make_a_pile(100) == [x for x in range(1, 201, 2)]