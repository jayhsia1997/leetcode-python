"""
Title: 11. Container With Most Water
Difficulty: Medium
Tags: [Array, Two Pointers, Greedy]
URL: https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def max_area(self, height: List[int]) -> int:
        """

        :param height:
        :return:
        """
        left = 0  # 初始化左 index
        right = len(height) - 1  # 初始化右 index
        max_area = 0  # 初始化最大容量
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = width * h if width * h > max_area else max_area

            # 將 index 移向彼此，數字較大保持不變
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
