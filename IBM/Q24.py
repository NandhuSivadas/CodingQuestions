def sol(a,b):
    sa=set(a)
    sb=set(b)
    if sa & sb:
        return True
    else:
        return False

    

a="hello"
b="hi"
print(sol(a,b))