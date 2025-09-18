def sol(a):
    l,mid,r=0,0,len(a)-1
    while mid<=r:
        if a[mid]==0:
            a[mid],a[l]=a[l],a[mid]
            l+=1
            mid+=1
        elif a[mid]==2:
            a[mid],a[r]=a[r],a[mid]
            r-=1
        else:
            mid+=1
    return a
    
a= [0, 1, 2, 0, 1, 2]
print(sol(a))