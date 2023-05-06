"""
Title: 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Tags: [Array, Two Pointers]
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def remove_duplicates(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            # print(f"i: {i}, j: {j}, nums: {nums}")
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1
