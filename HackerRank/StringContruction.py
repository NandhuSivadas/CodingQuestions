def stringConstruction(s):
    # Write your code here
    p=''
    c=0
    for i in s:
        if i not in p:
            p+=i
            c+=1
    return c
        