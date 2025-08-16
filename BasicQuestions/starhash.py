def val(s):
    s,h=0,0
    for i in string:
        if i=="*":
            s+=1
        else:
            h+=1
    
    if s>h:
        return 1
    elif s<h:
        return -1
    else:
        return 0




string="###***"
print(val(string))














