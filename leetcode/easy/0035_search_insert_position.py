def search_insert(nums, target):
    """
    LeetCode #35: Search Insert Position
    https://leetcode.com/problems/search-insert-position/
    Given a sorted array of distinct integers and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.
    You must write an algorithm with O(log n) runtime complexity.
    :param nums: List[int] - A sorted list of distinct integers.
    :param target: int - The target value to search for.
    :return: int - The index of the target value or the index where it would be inserted.
    """
    st_idx = 0
    end_idx = len(nums)
    while st_idx < end_idx:
        mid_idx = (st_idx + end_idx) // 2
        if target < nums[mid_idx]:
            end_idx = mid_idx
        elif target > nums[mid_idx]:
            st_idx = mid_idx + 1
        else:
            return mid_idx
    return st_idx
