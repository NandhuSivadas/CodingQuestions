s=input("Enter:")
h=0
t=0
for i in s:
    if i=="*":
        t+=1
    elif i=="#":
        h+=1

if t==h:
    print(0)
elif(t>h):
    print(t-h)
else:
    print(h-t)