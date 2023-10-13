"""
Title: 1512. Number of Good Pairs
Difficulty: Easy
Tags: [Array, Hash Table, Math, Counting]
URL: https://leetcode.com/problems/number-of-good-pairs/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def num_identical_pairs(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        return sum([c*(c-1)//2 for c in count.values()])
