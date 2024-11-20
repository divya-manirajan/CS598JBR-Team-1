import pytest
from Task_46_solution import fib4

def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 54
    assert fib4(10) == 104
    assert fib4(11) == 208
    assert fib4(12) == 386
    assert fib4(13) == 752
    assert fib4(14) == 1474
    assert fib4(15) == 2918
    assert fib4(16) == 5794
    assert fib4(17) == 11538
    assert fib4(18) == 23014
    assert fib4(19) == 45962
    assert fib4(20) == 91926