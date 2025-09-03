def sol(pwd):
    c=0
    for i in range(0,len(pwd),2):
        w=pwd[i:i+2]
        if "1" in w:
            if w.count("1")!=2:
                c+=1
        else:
            if w.count("0")!=2:
                c+=1
    return c


pwd="1001"
print(sol(pwd))