import os
from typing import List


# LeetCode Problem: 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
