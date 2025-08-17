# Balanced strings are those that have an equal quantity of ‘L’ and ‘R’ characters. Return the maximum number of balanced strings you can obtain.
# Example 1:
# Input : str = RLRRLLRLRL
# Output : 4
# Explanation:
# s can be split into RL, RRLL, RL, RL, each substring contains the same number of ‘L’ and ‘R

s="RRLRRLLRLRL"
def bal(s):
    countL = 0
    countR = 0
    result = 0
    for i in s:
        if i == 'L':
            countL += 1
        else:
            countR += 1
        if countR == countL:
            result += 1
    return result     

print(bal(s))




