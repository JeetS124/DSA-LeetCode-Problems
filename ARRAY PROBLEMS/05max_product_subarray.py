# Leetcode Problem - 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/

# Input:
nums = [2, 3, -2, 4]

# Approach-1 -->


def max_prod_subarray(nums):
    max_prod = float("-inf")

    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            prod *= nums[j]
            max_prod = max(max_prod, prod)
    return max_prod


res = max_prod_subarray(nums)
print(res)


# Approach-2 -->
def max_prod_subarray2(nums):
    curr_max = curr_min = global_max = nums[0]

    for num in nums[1:]:
        if num < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(num, curr_max * num)
        curr_min = min(num, curr_min * num)

        global_max = max(global_max, curr_max)

    return global_max


res = max_prod_subarray2(nums)
print(res)
