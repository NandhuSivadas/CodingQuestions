triangleToy = [
    [2, 2, 1],
    [3, 3, 3],
    [3, 4, 5],
    [1, 1, 3]
]
re=[]
for i in triangleToy:
    a,b,c=sorted(i)
    if a+b>c:
        if a==b and a==c and b==c:
            re.append("Equilateral")
        elif a==b or a==c or b==c:
            re.append("Iso")
        else:
            re.append("none")
    else:
        re.append("none")

print(re)