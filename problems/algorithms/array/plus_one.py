"""
Title: 66. Plus One
Difficulty: Easy
Tags: [Array, Math]
URL: https://leetcode.com/problems/plus-one/
"""
from typing import List


# noinspection PyMethodMayBeStatic
class Solution:
    """Solution"""

    def plus_one_by_forloop(self, digits: List[int]) -> List[int]:
        """

        :param digits:
        :return:
        """
        if not digits:
            return [1]
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if digits[i] == 10:
                digits[i] = 0
            else:
                carry = 0
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits

    def plus_one_by_recursion(self, digits: List[int]) -> List[int]:
        """

        :param digits:
        :return:
        """
        if not digits:
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plus_one_by_recursion(digits=digits[0:-1])
            return digits
