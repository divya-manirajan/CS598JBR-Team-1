import pytest
from Task_54_solution import same_chars  # replace 'your_module' with the name of the module containing the 'same_chars' function

def test_same_chars_positive():
    assert same_chars("abc", "cba")

def test_same_chars_negative():
    assert not same_chars("abc", "abcd")

def test_same_chars_empty():
    assert same_chars("", "")

def test_same_chars_single_char():
    assert same_chars("a", "a")

def test_same_chars_different_case():
    assert same_chars("Abc", "cba")