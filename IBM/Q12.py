
# Count Distinct Pairs with Target Difference

# Problem Statement
# A number of bids are received for a project. Given an array of project costs and a target value,
#  determine the number of **distinct pairs** of project costs where their **absolute difference** is equal to the target value.
#   Two pairs are distinct if they differ in at least one value.

# Function Description

# Complete the function `countPairs` which has the following parameters:

# projectCosts` (an array of integers): The costs of the projects.
# target` (an integer): The target absolute difference.

# Returns:
# An integer representing the number of distinct pairs in `projectCosts` with an absolute difference equal to `target`.

# 

#Sample Input and Output

#Sample Input:

#  `projectCosts = [1, 3, 5]`
#  `target = 2`

#Sample Output:

# * `2`

# **Explanation:**

# There are two pairs that satisfy the condition:
# 1.  The pair **(1, 3)** has an absolute difference of $|1 - 3| = 2$.
# 2.  The pair **(3, 5)** has an absolute difference of $|3 - 5| = 2$.

# Therefore, the total count of such distinct pairs is 2.

def sol(cost, t):
    Pcost=set(cost)
    c=0
    for i in Pcost:
        if (i+t) in Pcost:
            c+=1
    return c


print(sol([1, 3, 5], 2))          # Output: 2 → (1,3), (3,5)
print(sol([1, 5, 3, 4, 2], 2))    # Output: 3 → (1,3), (3,5), (2,4)
print(sol([1, 1, 1, 2], 1))       # Output: 1 → (1,2)
print(sol([8, 12, 16, 4, 0], 4))  # Output: 4 → (0,4), (4,8), (8,12), (12,16)