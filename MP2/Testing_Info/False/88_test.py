import pytest
from Task_88_solution import sort_array

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_even_sum():
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

def test_sort_array_odd_sum():
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]

def test_sort_array_even_sum_hardcoded():
    assert sort_array([2, 1]) == [1, 2]

def test_sort_array_odd_sum_hardcoded():
    assert sort_array([15, 42, 87, 32 ,11, 0]) == [0, 11, 15, 32, 42, 87]

def test_sort_array_even_sum_hardcoded_2():
    assert sort_array([21, 14, 23, 11]) == [23, 21, 14, 11]