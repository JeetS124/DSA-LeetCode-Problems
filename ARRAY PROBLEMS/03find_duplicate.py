# Leetcode Problem-442 Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/


# Input:
nums = [4, 3, 2, 7, 8, 2, 3, 1]


# Approach-1 --> Use Hashmap of Hashset
def find_duplicate(nums):
    seen = set()
    duplicates = []
    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates


# res = find_duplicate(nums)
# print(res)


# Approach-2 --> Use the Given Constraints (In-Place Marking)
# Since each number is between 1 and n, you can use the array itself to mark visits.

# Core Idea:
# For each number num, map it to index abs(num)-1

# If nums[index] is positive, make it negative (mark it visited)

# If nums[index] is already negative, then it's a duplicate.


def find_duplicates(nums):
    duplicates = []

    for num in nums:
        index = abs(num) - 1

        if nums[index] < 0:
            duplicates.append(abs(num))
        else:
            nums[index] *= -1
    return duplicates


res = find_duplicates(nums)
print(res)
