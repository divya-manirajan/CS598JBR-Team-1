import pytest
from Task_101_solution import words_string  # replace 'your_module' with the name of the module containing the words_string function

def test_words_string_empty_input():
    assert words_string("") == []

def test_words_string_single_word():
    assert words_string("hello") == ["hello"]

def test_words_string_multiple_words():
    assert words_string("hello,world") == ["hello", "world"]

def test_words_string_multiple_commas():
    assert words_string("hello,,world") == ["hello", "", "world"]

def test_words_string_leading_and_trailing_spaces():
    assert words_string("   hello, world   ") == ["", "hello", "world", ""]