import heapq

# LeetCode 1046: 最後の石の重さ
from typing import List

# https://leetcode.com/problems/last-stone-weight/
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the two heaviest stones and smash them together.
# Suppose the heaviest stone weighs x and the second heaviest stone weighs y. The result of this smash is:
# - If x == y, both stones are destroyed, and the result is 0.
# - If x != y, the heaviest stone is destroyed, and the second heaviest stone weighs x - y.
# At the end of the game, there is at most one stone left.
# Return the weight of the last remaining stone. If there are no stones left, return 0.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if first != second:
                heapq.heappush(max_heap, -(first - second))
        return -max_heap[0] if max_heap else 0
