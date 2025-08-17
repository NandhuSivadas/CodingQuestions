def intro(n):
    if n==0:
        return 
    print("hello:",n)
    intro(n-1)

n=3
intro(n)