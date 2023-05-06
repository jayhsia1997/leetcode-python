"""
Test cases for remove_element.py
"""
import pytest

from problems.algorithms.array.remove_element import Solution


@pytest.mark.parametrize(
    argnames=("nums", "val", "expected"),
    argvalues=[
        ([3, 2, 2, 3], 3, 2),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ([1], 1, 0),
        ([1, 1, 1, 1, 1], 1, 0),
        ([], 0, 0),
    ]
)
def test_remove_element(nums, val, expected):
    sol = Solution()
    assert sol.remove_element(nums, val) == expected
