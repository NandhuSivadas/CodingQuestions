s='abcabcbb'
l=0
r=1
m=0
c=1
while r<len(s):
    if s[l]<s[r]:
        c+=1
        if m<c:
            m=c
    else:
        l+=1
    r+=1

print(m)