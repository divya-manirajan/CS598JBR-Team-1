import pytest
from Task_3_solution import below_zero  # replace 'your_module' with the actual module name


def test_below_zero_with_positive_operations():
    operations = [1, 2, 3, 4]
    assert not below_zero(operations)


def test_below_zero_with_negative_operations():
    operations = [-1, -2, -3, -4]
    assert below_zero(operations)


def test_below_zero_with_mix_of_positive_and_negative_operations():
    operations = [1, -2, 3, -4]
    assert not below_zero(operations)


def test_below_zero_with_empty_operations():
    operations = []
    assert not below_zero(operations)