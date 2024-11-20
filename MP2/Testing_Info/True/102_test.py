import pytest

def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def test_choose_num():
    assert choose_num(5, 10) == 9
    assert choose_num(10, 5) == -1
    assert choose_num(7, 7) == -1
    assert choose_num(5, 6) == 5