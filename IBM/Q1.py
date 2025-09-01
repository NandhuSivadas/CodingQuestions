# Question 1: Odd-Even Transform Problem
# The Odd-Even Transform Problem works on an array of integers (both positive, negative, and zero),
#  by taking an integer value n (a whole number) that specifies the number of times the transformation has to be applied.
# On an array of integers, the transformation that n number of times needs to occur:

# Adds 3 (+3) to each odd integer.
# Subtracts 3 (-3) from each even integer.
# Example
# Array: [3, 4, 9], Transformations: 3

# Step-by-step:

# [3, 4, 9]   -> after 1st transform -> [6, 1, 12]
# [6, 1, 12]  -> after 2nd transform -> [3, 4, 9]
# [3, 4, 9]   -> after 3rd transform -> [6, 1, 12]
# Result: [6, 1, 12]

# ✅ Sample Input:
# arr = [3, 4, 9]
# n = 3
# ✅ Sample Output:
# [6, 1, 12]



def sol(arr, n):
    res = []
    for num in arr:
        if num % 2 == 0: 
            res.append(num - 3)
        else: 
            res.append(num + 3)
    return res


arr = [3, 4, 9]
n = 3
print(sol(arr, n))
