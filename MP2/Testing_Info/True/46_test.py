import pytest
from Task_46_solution import fib4  # replace 'your_module' with the name of the module containing the fib4 function

def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2
    assert fib4(5) == 2
    assert fib4(6) == 6
    assert fib4(7) == 6
    assert fib4(8) == 16
    assert fib4(9) == 16
    assert fib4(10) == 42
    assert fib4(11) == 42
    assert fib4(12) == 104
    assert fib4(13) == 104
    assert fib4(14) == 272
    assert fib4(15) == 272
    assert fib4(16) == 754
    assert fib4(17) == 754
    assert fib4(18) == 2032
    assert fib4(19) == 2032
    assert fib4(20) == 5376