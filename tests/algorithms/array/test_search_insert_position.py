"""
Test cases for search_insert_position.py
"""
import pytest

from problems.algorithms.array.search_insert_position import Solution


@pytest.mark.parametrize(
    argnames=("nums", "target", "expected"),
    argvalues=[
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
        ([1], 1, 0),
        ([1], 2, 1)
    ]
)
def test_search_insert(nums, target, expected):
    sol = Solution()
    assert sol.search_insert(nums, target) == expected
