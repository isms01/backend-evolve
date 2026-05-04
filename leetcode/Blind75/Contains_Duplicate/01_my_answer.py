from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j,num in enumerate(nums):
                if i==j:
                    continue
                if nums[i] == num:
                    return True
        return False