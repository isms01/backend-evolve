# LeetCode Problem 509: Fibonacci Number
from functools import lru_cache

# https://leetcode.com/problems/fibonacci-number/
# The Fibonacci sequence is defined as follows:
# F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.
# Example:
# Input: n = 4
# Output: 3
# Input: n = 10
# Output: 55


class Solution:
    @lru_cache(maxsize=None)
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)
