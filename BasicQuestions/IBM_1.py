def box(nums):
    dict={}
    s=[]
    low=min(nums)
    high=max(nums)

    for i in range(low,high+1):
        s=sum(int(k) for k in str(i))
        if s not in dict:
            dict[s]=1
        else:
            dict[s]+=1
    return dict


nums = [321, 325, 330]
print(box(nums))
