# s = "Was it a car or a cat I saw"
# s=s.lower()
# c=''
# for i in s:
#     if i.isalnum():
#         c+=i
# if c==c[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')  # Remove spaces first
    i = 0
    j = len(s) - 1          # Now safe to get last index

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

s = "Was it a car or a cat I saw"
print(palindrome(s))
