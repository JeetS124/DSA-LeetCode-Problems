# Leetcode Problem-1:
# https://leetcode.com/problems/two-sum/description/

# nums = [2, 7, 11, 15]
nums = [3, 2, 4]
target = 6
target = 6

# Approach-1 --> Brute Force


def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


res = two_sum(nums, target)
print(res)

# Approach-1 --> Using Hashmap (Optimal):


def two_sum_hashmap(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]

        num_to_index[num] = i
