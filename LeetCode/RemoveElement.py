nums =  [0,1,2,2,3,0,4,2]
val = 2
j=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[j]=nums[i]
        j+=1

print(j)