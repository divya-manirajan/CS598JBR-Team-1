import pytest
from Task_52_solution import below_threshold  # replace 'your_module' with the actual module name

def test_below_threshold_all_below():
    assert below_threshold([1, 2, 3], 5)

def test_below_threshold_some_above():
    assert not below_threshold([1, 2, 5], 4)

def test_below_threshold_all_above():
    assert not below_threshold([5, 6, 7], 4)

def test_below_threshold_empty_list():
    assert below_threshold([], 4)