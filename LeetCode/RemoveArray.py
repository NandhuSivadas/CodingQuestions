num = [0,0,1,1,1,2,2,3,3,4]
l=1
r=1
while(r<len(num)):
    if num[r]!=num[r-1]:
        num[l]=num[r]
        l+=1
    r+=1
print(l,num)