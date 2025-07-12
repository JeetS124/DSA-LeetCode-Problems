# LeetCode Problem-217
# https://leetcode.com/problems/contains-duplicate/

# Input:
nums = [1, 2, 3, 1]


# Approach-1 --> Brute Force-Check Every pair
def duplicate_value(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    else:
        return False


res = duplicate_value(nums)
print(res)


# Approach-2 --> Use Set:
def duplicate_value_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


res = duplicate_value_set(nums)
print(res)
