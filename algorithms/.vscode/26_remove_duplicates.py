# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


def remove_duplicates(nums):
    seen = 0
    result = []

    for num in nums:
        bit = 1 << num
        bit_is_seen = seen & bit
        if not bit_is_seen:
            result.append(num)
            seen |= bit

    return result

# Example usage:
nums = [1, 2, 3, 2, 4, 5, 6, 1, 3, 4, 5]
result = remove_duplicates(nums)
print(result)