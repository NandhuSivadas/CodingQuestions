def sol(n):
    res = 0
    while n:
        d = n % 10
        fact = 1
        for i in range(1, d+1):
            fact *= i
        res += fact
        n //= 10
    if res==n:
        return True
    else:
        return False

n = int(input())
print(sol(n))
