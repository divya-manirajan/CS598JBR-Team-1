import pytest
from Task_86_solution import anti_shuffle  # replace 'your_module' with the name of the module where the function is defined

def test_anti_shuffle():
    assert anti_shuffle("dcba") == "abcd"
    assert anti_shuffle("dcba zmni") == "abcd mniz"
    assert anti_shuffle("") == ""
    assert anti_shuffle("a") == "a"
    assert anti_shuffle("ab") == "ab"
    assert anti_shuffle("abc") == "abc"
    assert anti_shuffle("abcd") == "abcd"