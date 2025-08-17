# Sum of Each Window
# Input: arr = [1, 2, 3, 4, 5], k = 2
# # Output: [3, 5, 7, 9]

def sol(arr,k):
    sum1=sum(arr[:k])
    res=[]
    res.append(sum1)
    for i in range(k,len(arr)):
        sum1+=arr[i]-arr[i-k]
        res.append(sum1)
    return res

arr = [1, 2, 3, 4, 5]
k = 2    
print(sol(arr,k))