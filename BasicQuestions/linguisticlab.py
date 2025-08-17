def sol(n):
    res=''
    for i in n:
        if i not in 'aeiou':
            res+=i
    return res


n="love you somuch"
print(sol(n))