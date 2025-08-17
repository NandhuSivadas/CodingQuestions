# Maximum Sum Subarray of Size K

# Input: arr = [2, 1, 5, 1, 3, 2], k = 3

# Output: 9 (subarray [5,1,3])

def sol(arr,k):
    sum1=sum(arr[:k])
    csum=sum1
    for i in range(k,len(arr)):
        csum+=arr[i]-arr[i-k]
        sum1=max(csum,sum1)
    return sum1

arr=[2, 1, 5, 1, 3, 2]
k=3
print(sol(arr,k))