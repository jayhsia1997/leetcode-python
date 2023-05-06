"""
Test cases for remove_duplicates.py
"""
import pytest

from problems.algorithms.array.remove_duplicates import Solution


@pytest.mark.parametrize(
    argnames=("nums", "expected"),
    argvalues=[
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
        ([1, 2, 3, 4, 5], 5),
        ([1, 1, 1, 1, 1], 1),
        ([], 0),
    ]
)
def test_remove_duplicates(nums, expected):
    sol = Solution()
    assert sol.remove_duplicates(nums) == expected
