s='babad'
c=''
l=0
r=len(s)-1
while(r>l):
    if s[l]!=s[r]:
        r-=1
        l+=1
    else:
        c+=s[r]
        l+=1
        r-=1
print(c)