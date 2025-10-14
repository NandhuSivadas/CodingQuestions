def sol(s):
    
    map = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    words = s.split()
    res = []
    i = 0
    while i<len(words):
        if words[i]=="double":
            res.append(map[words[i+1]]*2)
            i+=2
        elif words[i]=="thriple":
            res.append(map[words[i+1]]*3)
            i+=2
        else:
            res.append(map[words[i]])
            i+=1
    return "".join(res)
    


print(sol("five one zero two four eight zero double three two"))
