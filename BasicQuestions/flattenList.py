def flatten_iter(lst):
    stack = lst[::-1]  
    result = []

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1]) 
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4]], 5]
print(flatten_iter(nested))  


def min_length(n):
    L = 1
    while L * (L + 1) // 2 < n:
        L += 1
    if L * (L + 1) // 2 == n:
        return L
    else:
        return L + 1   # need one extra char to adjust

t = int(input())
for _ in range(t):
    n = int(input())
    print(min_length(n))
