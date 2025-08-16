# Balanced strings are those that have an equal quantity of ‘L’ and ‘R’ characters. Return the maximum number of balanced strings you can obtain.
# Example 1:
# Input : str = RLRRLLRLRL
# Output : 4
# Explanation:
# s can be split into RL, RRLL, RL, RL, each substring contains the same number of ‘L’ and ‘R

s="RLRRLLRLRL"

def bal(s):
    r,c=0,0
    for i in s:
        if i=='R':
            c+=1
        else:
            c-=1
            if c==0:
                r+=1
    return r
    
print(bal(s))
