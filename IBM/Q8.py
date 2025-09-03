
# Implement a simple prototype service to find the difference between two JSON (JavaScript Object Notation) objects.

# To keep the prototype simple, a JSON will contain only key-value pairs and no nested objects or arrays in it. Given two JSON strings, json1 and json2, find the list of keys for which the values are different. If a key is present in only one of the JSONs, it should not be considered in the result. The list of keys should be sorted in lexicographically ascending order.

# Example
# Suppose json1 = {"hello": "world", "hi": "hello", "you": "me"} and json2 = {"hello": "world", "hi": "hi", "you": "me"}.

# The only common key where the values differ is "hi". Hence the answer is ["hi"].

# Function Description
# Complete the function getJSONDiff in the editor below.

# getJSONDiff has the following parameter(s):

# json1: the first JSON string
# json2: the second JSON string
# Returns string[]: a sorted list of keys that have different associated values in the two JSONs.





def sol(d1,d2):
    lst=[]
    for i,v in d1.items():
        if d1[i]!=d2[i]:
            lst.append(i)

    return lst



d1 = {"hello": "world", "hi": "hello", "you": "he"} 
d2 = {"hello": "world", "hi": "hi", "you": "me"}

print(sol(d1,d2))
