def sol(n):
    c=1
    ch=[]
    for i in n:
        if i in 'aeiouAEIOU':
            ch.append(str(c))
            c+=1
            if c>9:
                c=1
        else:
            ch.append(i)
    return "".join(ch)[::-1]

print(sol("Language"))