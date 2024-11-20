import pytest
from Task_36_solution import fizz_buzz  # replace 'your_module' with the name of the module containing the fizz_buzz function

def test_fizz_buzz():
    assert fizz_buzz(0) == 0
    assert fizz_buzz(1) == 0
    assert fizz_buzz(10) == 0
    assert fizz_buzz(11) == 1
    assert fizz_buzz(13) == 1
    assert fizz_buzz(14) == 0
    assert fizz_buzz(20) == 0
    assert fizz_buzz(22) == 0
    assert fizz_buzz(26) == 0
    assert fizz_buzz(39) == 1
    assert fizz_buzz(44) == 0
    assert fizz_buzz(55) == 1
    assert fizz_buzz(60) == 0
    assert fizz_buzz(77) == 1
    assert fizz_buzz(88) == 0
    assert fizz_buzz(100) == 0