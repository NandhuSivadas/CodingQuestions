nums = [1,2,3,4]
c=[]
k=0
for i in range(len(nums)):
    l=i+1
    r=i-1
    while (l<len(nums)):
        k*=nums[l]
        l+=1
    while (r>-1):
        k*=nums[r]
        r-=1
    c=k
    
print(c)