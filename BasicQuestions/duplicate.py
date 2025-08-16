Test= [1,2,3,2,4,3] 
lst=[]
seen=set()
for i in Test:
    if i not in seen:
        seen.add(i)
    else:
        lst.append(i)


print(lst)