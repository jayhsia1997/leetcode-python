"""
Test cases for number_of_good_pairs.py
"""
import pytest

from problems.algorithms.array.number_of_good_pairs import Solution

ARG_NAMES = ("nums", "expected")
ARG_VALUES = [
    ([1, 2, 3, 1, 1, 3], 4),
    ([1, 1, 1, 1], 6),
    ([1, 2, 3], 0),
    ([1, 1, 2, 2, 3, 1, 3, 1], 8)
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_num_identical_pairs(nums, expected):
    """
    Test num_identical_pairs() method
    """
    sol = Solution()
    assert sol.num_identical_pairs(nums) == expected
