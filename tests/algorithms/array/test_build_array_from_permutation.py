"""
Test case for build_array_from_permutation.py
"""
import pytest

from problems.algorithms.array.build_array_from_permutation import Solution

ARG_NAMES = ("nums", "expected")
ARG_VALUES = [
    ([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3]),
    ([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3]),
    ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_build_array(nums, expected):
    """
    Test build_array() method
    """
    sol = Solution()
    assert sol.build_array(nums) == expected
