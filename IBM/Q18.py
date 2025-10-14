# Problem Statement
# Given an integer array nums, determine the number of ways to split (or "slice") 
# the array into two non-empty parts such that the sum of the left part is strictly greater than the sum of the right part.
# Input

# nums: a list of integers.
# Output
# Return an integer representing the number of valid ways to slice the array.

# Example
# Input:
# nums = [10, 4, -8, 7]

# Output:
# 2

# Explanation:
# Possible splits:

# [10] | [4, -8, 7] → left = 10, right = 3 → ✅

# [10, 4] | [-8, 7] → left = 14, right = -1 → ✅

# [10, 4, -8] | [7] → left = 6, right = 7 → ❌


# Total valid splits = 2.


def sol(num):
    t=sum(num)
    l=0
    r=0
    c=0
    for i in num:
        l+=i
        r=t-l
        if l>r:
            c+=1
        
    return c

num= [10, 4, -8, 7]

print(sol(num))

