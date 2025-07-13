from collections import Counter

def majorityElement(nums):
        
        count = Counter(nums)
        most = count.most_common(1)[0][0] 
        return most
        

nums=[1,1,1,2,2,3,3,3,3,4,5,6]
print(majorityElement(nums))