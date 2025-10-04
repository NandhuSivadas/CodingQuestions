

#  Question: Number of Words on a Given Line

#  Problem Statement

# On a particular page of a notebook, the first two lines contain a certain number of words. 
# A student fills subsequent lines by copying words from the preceding two lines. Specifically:

#    The third line contains words copied from the first and second lines (total words = words on line 1 + words on line 2).
#    The fourth line contains words copied from the second and third lines (total words = words on line 2 + words on line 3).
#    This activity continues until a specified `N`-th line is reached.

# Your task is to calculate and print the number of words on the `N`-th line.

#  Constraints and Validation Rules:

# 1.  The number of words on the first line (`W1`) must be at least 1.
# 2.  The number of words on the second line (`W2`) must be greater than the number of words on the first line (`W1`).

# If any of these constraints are violated, the input is considered "invalid".

#  Input Format

#    The first line contains three space-separated integers: `W1` (words on the first line), `W2` (words on the second line), and `N` (the target line number).

#  Output Format

#    If the input is valid, print a single integer representing the number of words on the `N`-th line.
#    If the input is invalid based on the constraints, print `"Invalid Input"`.

#  Example 1

# Input:

# ```
# 1 2 5
# ```

# Output:

# ```
# 8
# ```

# Explanation:

#    Line 1: 1 word
#    Line 2: 2 words
#    Line 3: 1 + 2 = 3 words
#    Line 4: 2 + 3 = 5 words
#    Line 5: 3 + 5 = 8 words.
#     Therefore, the number of words on line 5 is 8.

#  Example 2

# Input:

# ```
# 3 1 10
# ```

# Output:

# ```
# Invalid Input
# ```

# Explanation:
# The second line's word count (1) is not greater than the first line's word count (3). This violates the constraint, making the input invalid.

    def sol(a,b,n):
        if n==1:
            return a
        if n==2:
            return ba
        for i in range(2,n):
            c=a+b
            a,b=b,c
        return c

    print(sol(1,2,5))

