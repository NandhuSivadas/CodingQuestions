# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

# You may assume that:


# There is exactly one solution, and
# You may not use the same element twice.

def twoSum(nums, target):
    seen = {}   # dictionary to store num -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

 