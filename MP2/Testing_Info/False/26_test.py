from Task_26_solution import List
from Task_26_solution import remove_duplicates
import pytest


@pytest.mark.parametrize('numbers, expected', [
    ([], []),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 2, 3, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
])
def test_remove_duplicates(numbers: List[int], expected: List[int]):
    assert remove_duplicates(numbers) == expected