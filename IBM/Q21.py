#  🔒 IBM Coding Question: Decrypt Message

#  🧩 Problem Statement

# You are given an encrypted message and a key phrase.
# Your task is to decrypt the message using the key phrase.

# The encrypted message and key phrase are strings of lowercase English letters.
# Both strings contain the same number of words.

# Decryption uses a cyclic shift of letters based on the key phrase.

# ---

#  ⚙️ Constraints

#  Only lowercase letters are considered. Uppercase letters are invalid input.
#  Letters repeat in a cycle:

#    After `'z'`, the next letter is `'a'`.
#    Before `'a'`, the previous letter is `'z'`.
#  Only English alphabets are considered.
#  The number of words in the message and the key phrase are the same.

# ---

#  💡 Example

# Input:

# ```
# dnotq
# abcde
# ```

# Output:

# ```
# cmlop
# ```

# Explanation:
# Each letter in the encrypted message is shifted backward by the corresponding letter in the key phrase.

# For example:

#  `'d'` (encrypted) and `'a'` (key) → `'c'` (decrypted)
#  `'n'` and `'b'` → `'m'`
#  `'o'` and `'c'` → `'l'`
#  `'t'` and `'d'` → `'o'`
#  `'q'` and `'e'` → `'p'`

# Hence, the decrypted message is `"cmlop"`.



def sol(word, k):
    r = ''
    for i, j in zip(word, k):
        wn = ord(i) - ord('a')
        kn = ord(j) - ord('a')
        d = (wn - kn - 1) % 26   
        r += chr(d + ord('a'))
    return r

print(sol("dnotq", "abcde"))
