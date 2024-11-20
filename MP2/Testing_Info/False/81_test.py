import pytest
from Task_81_solution import numerical_letter_grade

def test_numerical_letter_grade():
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert numerical_letter_grade([1.2]) == ['D+']
    assert numericalletter_grade([0.5]) == ['D-']
    assert numerical_letter_grade([0.0]) == ['E']
    assert numerical_letter_grade([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
    assert numerical_letter_grade([0, 0.7]) == ['E', 'D-']