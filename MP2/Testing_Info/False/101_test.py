import pytest
from Task_101_solution import words_string

def test_words_string():
    # Check some simple cases
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("Hi, my name") == ["Hi", "my", "name"]
    assert words_string("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

    # Check some edge cases that are easy to work out by hand.
    assert words_string("") == []
    assert words_string("ahmed     , gamal") == ["ahmed", "gamal"]