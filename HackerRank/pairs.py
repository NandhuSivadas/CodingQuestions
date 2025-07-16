def pairs(k, arr):
        
    nums = set(arr)
    c = 0
    for num in nums:
        if num + k in nums:
            c += 1
    return c