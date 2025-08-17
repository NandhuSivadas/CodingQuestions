# Last Element of Each Window
# Input: arr = [4, 5, 6, 7, 8], k = 2
# Output: [5, 6, 7, 8]

def sol(arr,k):
    res=[]
    for i in range(k-1,len(arr)):
        res.append(arr[i])
    return res


arr = [4, 5, 6, 7, 8]
k = 2
print(sol(arr,k))