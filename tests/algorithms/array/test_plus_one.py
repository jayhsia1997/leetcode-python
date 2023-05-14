"""
Test cases for plus_one.py
"""
import pytest

from problems.algorithms.array.plus_one import Solution

ARG_NAMES = ("digits", "expected")
ARG_VALUES = [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([0], [1]),
    ([9], [1, 0]),
    ([9, 9], [1, 0, 0])
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_plus_one_by_forloop(digits, expected):
    sol = Solution()
    assert sol.plus_one_by_forloop(digits) == expected


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_plus_one_by_recursion(digits, expected):
    sol = Solution()
    assert sol.plus_one_by_recursion(digits) == expected
