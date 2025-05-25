## 🔸 Technique: Two-Pointer Compaction

**Description**  
Shift non-zero elements to the front while preserving order, then fill the rest with zeroes.

**Use Case**  
- In-place reordering
- Cleanup without resizing

**Used in**  
- LeetCode #283: Move Zeroes  
  [→ Problem](https://leetcode.com/problems/move-zeroes/)  
  [→ View Code](../leetcode/easy/0283_move_zeroes.py)

**Comment**  
Avoids resizing by using a write pointer. Efficient (O(n)) and preserves element order.
