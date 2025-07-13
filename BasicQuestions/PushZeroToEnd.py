i=0
c=0
s=[2,0,3,4,6,0,5,0]
while i<len(s):
    if s[i]==0:
        s.pop(i)
        c+=1
    i+=1

for i in range(c):
    s.append(0)

print(s)