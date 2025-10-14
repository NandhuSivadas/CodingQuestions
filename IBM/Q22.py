
# 🔢 IBM Coding Question: Closed Paths in Digits
# Problem Statement
# Some numbers are formed with "closed paths." The digits 0, 4, 6, and 9 each have 1 closed path, and the digit 8 has 2 closed paths. None of the other digits (1, 2, 3, 5, 7) have any closed paths.

# Given a number, determine the total number of closed paths in all of its digits combined.

# Function Description
# Complete the function closedPaths which takes the following argument:

# number (integer): An integer containing the digits to analyze.

# Returns:

# integer: The total number of closed paths in the given number.

def sol(n):
    c=0
    for i in n:
        if i in "0469":
            c+=1
        elif i=="8":
            c+=2
    return c



n="98604"
print(sol(n))