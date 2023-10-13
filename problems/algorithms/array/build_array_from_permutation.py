"""
Title: 1920. Build Array from Permutation
Difficulty: Easy
Tags: [Array, Simulation]
URL: https://leetcode.com/problems/build-array-from-permutation/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def build_array(self, nums: List[int]) -> List[int]:
        """

        :param nums:
        :return:
        """
        return [nums[nums[index]] for index in range(len(nums))]
