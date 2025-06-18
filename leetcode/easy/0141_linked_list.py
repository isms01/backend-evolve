from typing import Optional


# LeetCode Problem: 141. Linked List Cycle
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head  # pointer to traverse the linked list
        visited = set()
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False
