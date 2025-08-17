n=int(input("Enter:"))
def sol(n):
    s=sum(int(d) for d in str(n))
    if n%s==0:
        return True
    else:
        return False
    
print(sol(n))
