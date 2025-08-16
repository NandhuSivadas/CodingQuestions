# Write a python code to print the count of valid strings
# and invalid strings from a given list of strings

# A string is considered as valid if it contains combinations
# of alphabetes (in upper case or lower case) with/without
# spaces.

# Define a function to check if a given string is valid or not
# i.e if it contains combination of alphabetes.

# This function will take string as input and return True
# if the string is valid, otherwise will return False.

# Example:

# Input:
# 4
# HelloGood Morning
# abcd123Fghy
# India
# Progoto.c

# Output:
# Count Of Valid String = 2
# Count of Invalid String = 2




def valid(string):
    for c in string:
        if not (c.isalpha() or c.isspace()):
            return False
    return True





n = 3
s = [input() for _ in range(n)]
v, i = 0, 0  
for char in s:
    v, i = 0, 0  
    if valid(char):
        v += 1
    else:
        i += 1

print("Count of valid strings:", v)
print("Count of invalid strings:", i)
