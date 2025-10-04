def is_palindrome(s):
    return s == s[::-1]

def sol(a, b):
   
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if is_palindrome(a[:i] + b[:j]) or is_palindrome(b[:j] + a[:i]):
                return True
    return False

print(sol("race", "car"))    # True
print(sol("hello", "world")) # False
print(sol("aba", "bab"))     # True
