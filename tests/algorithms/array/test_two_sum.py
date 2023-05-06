"""
Test cases for two_sum.py
"""
import pytest

from problems.algorithms.array.two_sum import Solution


@pytest.mark.parametrize(
    argnames=("nums", "target", "expected"),
    argvalues=[
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([2, 5, 10, 14, 19, 20], 39, [4, 5]),
        ([10, 20, 32, 49, 52], 72, [1, 4]),
    ]
)
def test_two_sum(nums, target, expected):
    sol = Solution()
    assert sol.two_sum(nums, target) == expected
