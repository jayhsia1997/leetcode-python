"""
Title: 35. Search Insert Position
Difficulty: Easy
Tags: [Array, Binary Search]
URL: https://leetcode.com/problems/search-insert-position/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def search_insert(self, nums: List[int], target: int) -> int:
        """

        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start


