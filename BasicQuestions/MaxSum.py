# Question:
# Given an array of integers and a positive integer k, find the maximum sum of any contiguous subarray of length k.
# Input: arr = [1, 2, 3, 4, 5, 6, 7, 8], k = 3  
# Output: 21  

# Explanation:  
# The contiguous subarrays of length 3 are:  
# [1,2,3] → sum = 6  
# [2,3,4] → sum = 9  
# [3,4,5] → sum = 12  
# [4,5,6] → sum = 15  
# [5,6,7] → sum = 18  
# [6,7,8] → sum = 21 ← maximum sum


def sol(arr,k):
    maxsum=sum(arr[:k])
    csum=maxsum
    for i in range(k,len(arr)):
        csum+=arr[i]-arr[i-k]
        maxsum=max(maxsum,csum)
        
    return maxsum


arr=[1,2,3,4,5,6,7,8]
k=3
print(sol(arr,k))