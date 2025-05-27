# LeetCode Problem 1137: Tribonacci Number
from functools import lru_cache

# https://leetcode.com/problems/tribonacci-number/
# Given n, return the value of Tn, where Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn = Tn-1 + Tn-2 + Tn-3 for n > 2.
# The Tribonacci sequence is similar to the Fibonacci sequence, but it sums the last three numbers instead of the last two.
# Example:
# Input: n = 4
# Output: 4
# Input: n = 25
# Output: 1389537


class Solution:
    @lru_cache(maxsize=None)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return (
                self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
            )
