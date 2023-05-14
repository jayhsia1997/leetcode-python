"""
Test cases for single_number.py
"""
import pytest

from problems.algorithms.array.single_number import Solution

ARG_NAMES = ("nums", "expected")
ARG_VALUES = [
    ([2, 2, 1], 1),
    ([4, 1, 2, 1, 2], 4),
    ([1], 1)
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_single_number_by_set(nums, expected):
    sol = Solution()
    assert sol.single_number_by_set(nums) == expected


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_single_number_by_dict(nums, expected):
    sol = Solution()
    assert sol.single_number_by_dict(nums) == expected


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_single_number_by_bit(nums, expected):
    sol = Solution()
    assert sol.single_number_by_bit(nums) == expected
