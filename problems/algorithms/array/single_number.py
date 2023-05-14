"""
Title: 136. Single Number
Difficulty: Easy
Tags: [Array, Bit Manipulation]
URL: https://leetcode.com/problems/single-number/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def single_number_by_set(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        return 2 * sum(set(nums)) - sum(nums)

    def single_number_by_dict(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        d = {}
        for num in nums:
            if num in d:
                d.pop(num)
            else:
                d[num] = 1
        return list(d.keys())[0]

    def single_number_by_bit(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        result = 0
        for num in nums:
            result ^= num
        return result
