# Question 3: Strings
# Consider a string, S, that is a series of characters, each followed by its frequency as an integer. 
# The string is not compressed correctly, so there may be multiple occurrences of the same character.
# A properly compressed string will consist of one instance of each character in alphabetical order ,
# followed by the total count of that character within the string.

# Input:
# S = "a2b3a4c1b2"
# Output:   
# "a6b5c1"
# Explanation:

# a appears twice with counts 2 + 4 = 6 → a6
# b appears twice with counts 3 + 2 = 5 → b5
# c appears once with count 1 → c1
# Sorted alphabetically → "a6b5c1"

from collections import defaultdict
def sol(s):
    d=defaultdict(int)
    for i in range(len(s)):
        k=i+1
        if s[i].isalpha():
            num=0
            while  k<len(s) and s[k].isdigit():
                num=num*10+int(s[k])
                k+=1
            d[s[i]]+=num

    res = ''.join(f"{k}{v}" for k, v in d.items())
    return res


s= "a20b3a4c1b2"
print(sol(s))
