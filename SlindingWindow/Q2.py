# First Element of Each Window

# Input: arr = [10, 20, 30, 40, 50], k = 3

# Output: [10, 20, 30]

def sol(arr,k):
    res=[]
    sum1=sum(arr[:k])
    csum=sum1
    for i in range(k,len(arr)):
        csum+=arr[i]-arr[i-k]
        res.append(arr[i-k])
        
    return res
        

arr = [10, 20, 30, 40, 50]
k = 3    
print(sol(arr,k))