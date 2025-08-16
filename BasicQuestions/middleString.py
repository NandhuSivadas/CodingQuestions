def middleString(s, n):
    middle = (len(s) - 1) // 2   
    return s[middle:middle+n]

s = "have123fun"
n = 5
print(middleString(s, n)) 
