# LeetCode #283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/


def move_zeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_index = 0  # Pointer for the position of the next zero to move
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_index] = nums[i]
            zero_index += 1
    # Fill the rest of the array with zeros
    for i in range(zero_index, len(nums)):
        nums[i] = 0


# Example usage:
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    print(nums)  # Output: [1, 3, 12, 0, 0]
    # Example usage:
    nums = [0, 0, 1]
    move_zeroes(nums)
    print(nums)  # Output: [1, 0, 0]

    nums = [1, 2, 3]
    move_zeroes(nums)
    print(nums)  # Output: [1, 2, 3]

    nums = [0, 0, 0]
    move_zeroes(nums)
    print(nums)  # Output: [0, 0, 0]
    nums = []
