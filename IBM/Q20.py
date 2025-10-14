# 🔒 IBM Coding Question 1: Secure Password Flipping

#  🧩 Problem Statement

# A password string, `pwd`, consists of binary characters (0s and 1s).
# A cyber security expert is trying to determine the minimum number of changes required to make the password secure.

# To do so, the password must be divided into non-overlapping, even-length substrings.
# Each substring can contain only 0s or only 1s, not a mix.
# This ensures that the password is strong and less vulnerable to hacking attacks.

# Find the minimum number of characters that must be flipped in the password string (i.e., changed from `0` to `1` or `1` to `0`) to allow the string to be divided as described.

# > Note: A substring is a contiguous sequence of characters in a string.

# ---

#  🧠 Function Description

# Complete the function `getMinFlips` which takes the following argument:

#  `pwd`: A binary string (`str`) representing the password.

# Returns:
# An integer representing the minimum number of flips required to make the division possible.

# ---

#  💡 Example

# Input:

# ```
# pwd = "1110011000"
# ```

# Output:

# ```
# 3
# ```

# Explanation:
# The final secure string must be divisible into even-length substrings of all 0s or all 1s.

# The example shows the string being split into two valid substrings:

#  First Substring: `"111001"` (Length 6) → Must become all 0s or all 1s.
#  Second Substring: `"1000"` (Length 4) → Must become all 0s or all 1s.

# Since both lengths are even (6 and 4), the division is valid.
# The minimum flips to achieve this secure state is 3.

# The optimal final string is likely `"1111110000"`, which requires 3 flips (flipping the 4th, 5th, and 6th characters from `0, 0, 1` to `1, 1, 1`).

def sol(pwd):
    f=0
    for i in range(0,len(pwd),2):
        pos=pwd[i:i+2]
        if len(pos)==2 and pos[0]!=pos[1]:
            f+=1
    return f

print(sol("111"))


