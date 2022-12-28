def search(nums, target):
    """
    Given an array of integers sorted in ascending order, and an integer target, find target in nums.
    If target exists, then return its index. Otherwise, return -1.

    :param nums: array of integers sorted in ascending order
    :param target: the value to search for in nums
    :return: index of target in nums if it exists, else -1
    """
    left = 0
    right = len(nums) - 1
    median = (left + right) // 2

    while right - left > 1:
        if nums[median] < target:
            left = median + 1
            median = (left + right) // 2
        else:
            right = median
            median = (left + right) // 2

    result = -1
    if nums[left] == target:
        result = left
    elif nums[right] == target:
        result = right

    return result
