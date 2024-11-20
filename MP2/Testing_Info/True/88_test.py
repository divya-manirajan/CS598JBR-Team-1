import pytest
from Task_88_solution import sort_array  # replace 'your_module' with the name of the module where the function is defined

def test_sort_array_empty():
    assert sort_array([]) == []

def test_sort_array_single_element():
    assert sort_array([5]) == [5]

def test_sort_array_even_sum():
    assert sort_array([5, 2, 1, 4, 3]) == [1, 2, 3, 4, 5]

def test_sort_array_odd_sum():
    assert sort_array([5, 2, 1, 4, 3]) == [5, 4, 3, 2, 1]