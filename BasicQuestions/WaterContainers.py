def Water(s):
    l = 0
    r = len(s) - 1
    res = 0
    while l < r:
        area = min(s[l], s[r]) * (r - l)
        res = max(res, area)
        if s[l] <= s[r]:
            l += 1
        else:
            r -= 1
    return res

s = [1, 7, 2, 5, 4, 7, 3, 6]
print(Water(s))
