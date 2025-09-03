# Given requests as an array of strings, requests, and an integer k, after all requests are received, find the k most recent requests. Report the answer in order of most recent to least recent.

# Example
# Suppose n = 5, requests = ["item1", "item2", "item1", "item3", "item1"], and k = 3.

# Starting from the right and moving left, collecting distinct requests there is "item1" followed by "item3". Then the second instance of "item2" and find "item2". The answer is ["item1", "item3", "item2"].

# Function Description
# Complete the function getLatestRequests in the editor below.

# getLatestRequests takes the following arguments:

# str requests[]: the request ids
# int k: the number of requests to report
# Returns

# str[]: the k most recent requests


def sol(arr,k):
    stack=[]
    for i in arr:
        if i not in stack:
            stack.append(i)
        else:
            stack.remove(i)
            stack.append(i)
    
    return stack[-k:][::-1]


arr = ["item1", "item2", "item1", "item3", "item1"]
k = 3
print(sol(arr,k))