# Question:
# Given an array of integers arr and a positive integer k,
# find the average of every contiguous subarray of size k and return the list of averages.

# Input: arr = [1, 2, 3, 4, 5], k = 2  
# Output: [1.5, 2.5, 3.5, 4.5]  

# Explanation:  
# Subarrays of size 2 are:  
# [1, 2] → avg = 1.5  
# [2, 3] → avg = 2.5  
# [3, 4] → avg = 3.5  
# [4, 5] → avg = 4.5


def average_subarrays(arr,k):
    res=[]
    s=sum(arr[:k])
    res.append(s/k)
    for i in range(k,len(arr)):
        s+=arr[i]-arr[i-k]
        res.append(s/k)
    
    return res


arr = [2, 4, 6, 8, 10]
k = 3
print(average_subarrays(arr, k))  # Output: [4.0, 6.0, 8.0]
