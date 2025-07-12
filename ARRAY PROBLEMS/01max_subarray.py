# LeetCode Problem-53
# https://leetcode.com/problems/maximum-subarray/


# Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4,-1,2,1] is the subarray with the largest sum = 6.


# Approach-1 --> Brute Force(Check all subarrays):
# def max_sub_array_brute(nums):
#     max_sum = float("-inf")

#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             current_sum = sum(nums[i : j + 1])
#             max_sum = max(max_sum, current_sum)

#     return max_sum


# res = max_sub_array_brute(nums)
# print(res)

# ------------------------------------
# ------------------------------------

# Input:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# Approach-2 --> Kadane's Algorithem(OPtimal):
def max_subarray_kadane(nums):
    max_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)

    return max_sum


res = max_subarray_kadane(nums)
print(res)
