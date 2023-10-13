"""
Test cases for container_with_most_water.py
"""
import pytest

from problems.algorithms.array.container_with_most_water import Solution

ARG_NAMES = ("height", "expected")
ARG_VALUES = [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 1], 2),
    ([1, 3, 2, 1], 3),
    ([1], 0),
    ([], 0),
]


@pytest.mark.parametrize(
    argnames=ARG_NAMES,
    argvalues=ARG_VALUES
)
def test_max_area(height, expected):
    """
    Test max_area() method
    """
    sol = Solution()
    assert sol.max_area(height) == expected
