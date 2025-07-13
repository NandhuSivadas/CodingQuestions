def removeStars(s):
        c=[]
        for i in s:
            if i!='*':
                c.append(i)
            else:
                c.pop()
        return "".join(c)

s = "leet**cod*e"
print(removeStars(s))