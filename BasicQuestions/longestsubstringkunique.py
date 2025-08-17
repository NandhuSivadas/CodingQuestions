def max_len(s,k):
    first=0
    last=1
    max_seq=0
    while last<=len(s):
        unq=len(set(s[first:last]))
        if unq<k:
            last+=1
        elif unq>k:
            first+=1
        else:
            max_seq=max(max_seq,last-first)   
            last+=1
    return max_seq

s='aabacbebebe'
k=3
print(max_len(s,k))