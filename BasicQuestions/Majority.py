from collections import Counter
def sol(n):
    d=Counter(n)

    return d.most_common()[0][0]


n= [3, 3, 4, 2, 3, 3, 3]
print(sol(n))