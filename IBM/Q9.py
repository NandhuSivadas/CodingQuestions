# to find hcf of two numbers

def sol(a,b):
    while b != 0:          # loop runs until second number becomes 0
        a, b = b, a % b    # update a and b
    return a


n1=75
n2=15
print(sol(n1,n2))
