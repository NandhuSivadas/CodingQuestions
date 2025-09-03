def sol(arr, d):
    c = 0
    for i in range(len(arr) - 2):        # i < j < k
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if (arr[i] + arr[j] + arr[k]) % d == 0:
                    c += 1
    return c


arr = [3, 3, 4, 7, 8]
d = 5
print(sol(arr, d))  # Output: 3
