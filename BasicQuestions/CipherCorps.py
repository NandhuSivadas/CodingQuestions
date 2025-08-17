
def sol(n):
    for i in n:
        if n.count(i)==1:
            return i

n=input()
print(sol(n))