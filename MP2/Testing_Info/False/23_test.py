import pytest
from Task_23_solution import strlen

def test_strlen_empty_string():
    assert strlen('') == 0

def test_strlen_single_character_string():
    assert strlen('x') == 1

def test_strlen_multiple_character_string():
    assert strlen('asdasnakj') == 9

# Add more tests here