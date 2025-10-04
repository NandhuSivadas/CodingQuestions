# ## Q3: Palindrome from Substring Concatenation
# Problem Statement
# You are given two strings, a and b. 
# Determine if it is possible to create a palindrome by concatenating a non-empty substring from a and a non-empty substring from b. 
# The substrings can be concatenated in any order (i.e., substring(a) + substring(b) or substring(b) + substring(a)).

# Input Format
# The first line contains the string a.

# The second line contains the string b.

# Output Format
# Print "true" if a palindrome can be formed, otherwise print "false".

# Constraints
# 1≤length(a),length(b)≤2000

# Strings a and b consist of lowercase English letters.

# Example 1
# Input:

# race
# car
# Output:

# true
# Explanation:
# We can take the substring "race" from a and "car" from b. Concatenating them as "race" + "car" gives "racecar", which is a palindrome.

# Example 2
# Input:

# aba
# bab
# Output:

# true
# Explanation:
# We can take the substring "ab" from a and "a" from b. Concatenating them as "ab" + "a" gives "aba", which is a palindrome.

# Example 3
# Input:

# hello
# world
# Output:

# false
# Explanation:
# No combination of non-empty substrings from "hello" and "world" can form a palindrome.

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def sol(arr):
    res=arr[0]
    for i in range(1,len(arr)):
        res=gcd(res,arr[i])
    
    if res==1:
        return -1
    else:
        return res


arr=[6,12,18]
print(sol(arr))