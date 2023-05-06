"""
Title: 1. Two Sum
Difficulty: Easy
Tags: [Array, Hash Table]
URL: https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    """Solution"""

    def two_sum(self, nums: List[int], target: int) -> List[int]:  # noqa
        """

        :param nums:
        :param target:
        :return:
        """
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[num] = i
        return []
