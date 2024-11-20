import pytest

def make_a_pile(n):
    return [n + 2*i for i in range(n)]

def test_make_a_pile():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
    assert make_a_pile(0) == []
    assert make_a_pile(-5) == []