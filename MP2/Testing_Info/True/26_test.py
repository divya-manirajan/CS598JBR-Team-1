import pytest
from Task_26_solution import List
from Task_26_solution import remove_duplicates

def test_remove_duplicates_empty_list():
    assert remove_duplicates([]) == []

def test_remove_duplicates_single_element():
    assert remove_duplicates([1]) == [1]

def test_remove_duplicates_multiple_elements():
    assert remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]

def test_remove_duplicates_negative_numbers():
    assert remove_duplicates([-1, -2, -2, -1]) == [-1, -2]

def test_remove_duplicates_mixed_positive_negative_numbers():
    assert remove_duplicates([1, -1, 2, -2, -2, 1]) == [1, -1, 2, -2]