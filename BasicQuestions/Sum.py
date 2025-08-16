lst=[9,6,4,2,3,5,7,0,1]
lst.sort()
# c=lst[0]
# for i in range(len(lst)):
#     if lst[i]!=c:
#         print(c)
#     c+=1
n=len(lst)
sum1=(n*(n+1))//2
print(sum1-sum(lst))