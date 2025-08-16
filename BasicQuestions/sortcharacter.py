# Answer: Use Counter + sort by value.​
# Test: "tree" → "eert" or "rtee"​

from collections import Counter

def frequency_sort(s):
    k=Counter(s)
    res=''
    for key ,value in k.most_common():
        res+=key*value
    return res

    

print(frequency_sort("tree"))  # "eert" or "rtee"
