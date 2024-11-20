import pytest
from Task_81_solution import numerical_letter_grade

def test_numerical_letter_grade():
    grades = [4.0, 3.8, 3.2, 2.8, 2.2, 1.8, 1.2, 0.8, 0.2, 0.0]
    expected_output = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    assert numerical_letter_grade(grades) == expected_output

def test_numerical_letter_grade_empty():
    grades = []
    expected_output = []
    assert numerical_letter_grade(grades) == expected_output

def test_numerical_letter_grade_negative():
    grades = [-1.0, -0.5]
    expected_output = ["E", "E"]
    assert numerical_letter_grade(grades) == expected_output