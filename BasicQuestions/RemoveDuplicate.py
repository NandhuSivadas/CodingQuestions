def RemoveDuplicate(n):
    c = []
    for i in n:
        if i not in c:
            c.append(i)
    print(c)

n = [1, 2, 2, 11, 11, 11, 15, 6]
RemoveDuplicate(n)
