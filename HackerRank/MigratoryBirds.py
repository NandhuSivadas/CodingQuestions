def migratoryBirds(arr):
    freq=[0]*len(arr)
    for i in arr:
        freq[i]+=1
    return freq.index(max(freq))
