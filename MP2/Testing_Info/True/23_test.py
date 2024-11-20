import pytest
from Task_23_solution import strlen  # replace 'your_module' with the name of the module where the function is defined

def test_strlen_empty_string():
    assert strlen("") == 0

def test_strlen_single_character():
    assert strlen("a") == 1

def test_strlen_multiple_characters():
    assert strlen("hello world") == 11

def test_strlen_non_string_input():
    with pytest.raises(TypeError):
        strlen(123)