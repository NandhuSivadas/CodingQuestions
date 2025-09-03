# Question 6
# An English lecture at HackerElementary School is aimed at teaching students the letters of the alphabet.

# The students are provided with a string word that consists of lowercase English letters.

# In one move:

# They can choose any index i.
# Let the character at that index be c.
# Then, the first occurrence of c to the left of i and the first occurrence of c to the right of i are deleted (if they exist).
# The operation can still be carried out even if only one of them exists.
# The process repeats until no more deletions can be made.

# Task
# Find the minimum number of moves the students need to perform in order to get a word of minimal length.

# Example
# Example 1
# Input:  word = "baabacaa"
# Optimal sequence of moves:

# Choose index 0 → "baabacaa" → character = b Delete the next b (index 3) → "aabacaa"
# Choose index 1 → "aabacaa" → character = a Delete leftmost and rightmost a around index 1 → "bacaa"
# Choose index 3 → "bacaa" → character = a Delete leftmost and rightmost a around index 3 → "ba"
# No further reduction possible.

# Output: 3
# Example 2
# Input:  word = "abc"
# Output: 0
# Explanation: No character has duplicates on both sides, so no deletions are possible.
# Example 3
# Input:  word = "aaaa"
# Output: 1
# Explanation:
# - Choose index 1 → delete one `a` to the left and one `a` to the right → "aa".
# No more deletions possible. Minimal moves = 1.




def sol(word):
    from collections import defaultdict

    stack=defaultdict(list)
    m=0
    for i,c in enumerate(word):
        if stack[c]:
            stack[c].pop()
            m+=1
        else:
            stack[c].append(i)

    for c in stack:
        if len(stack[c])>1:
            m+=1
    
    return m

print(sol("baabacaa"))  # Expected 3
print(sol("abc"))       # Expected 0
print(sol("aaaa"))      # Expected 1
print(sol("abba"))      # Expected 2
print(sol("aabaa"))     # Expected 2
