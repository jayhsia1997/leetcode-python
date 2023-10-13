"""
Test cases for concatenation_of_array.py
"""
import pytest
from copy import deepcopy

from problems.algorithms.array.concatenation_of_array import Solution

ARG_NAMES = ("nums", "expected")
ARG_VALUES = [
    ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
    ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
    ([1], [1, 1]),
    ([], []),
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=deepcopy(ARG_VALUES)
)
def test_get_concatenation(nums, expected):
    """
    Test get_concatenation() method
    """
    sol = Solution()
    assert sol.get_concatenation(nums) == expected
