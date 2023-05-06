"""
Title: 27. Remove Element
Difficulty: Easy
Tags: [Array, Two Pointers]
URL: https://leetcode.com/problems/remove-element/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def remove_element(self, nums: List[int], val: int) -> int:
        """

        :param nums:
        :param val:
        :return:
        """
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
