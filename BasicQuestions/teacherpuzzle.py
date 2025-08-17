# n="I love programming in Python"
# m=0
# res=0
# for i in n.split():
#     w=len(i)
#     if w>m:
#         res=i
#         m=w

# print(res)


n =input()
res = max(n.split(), key=len)
print(res)