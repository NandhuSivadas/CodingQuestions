# Sort an array of 0s, 1s and 2s - Dutch National Flag Problem
# Last Updated : 01 Aug, 2025
# Given an array arr[] consisting of only 0s, 1s, and 2s. 
# The objective is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.

# This problem is the same as the famous "Dutch National Flag problem". The problem was proposed by Edsger Dijkstra. 
# The problem is as follows:

# Given n balls of colour red, white or blue arranged in a line in random order.
#  You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, 
# with the order of the colours being red, white and blue 
# (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: [0, 0, 1, 1, 2, 2] has all 0s first, then all 1s and all 2s in last.

# Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
# Explanation: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2} has all 0s first, then all 1s and all 2s in last.

def sol(a):
    l,mid,r=0,0,len(a)-1
    while mid<=r:
        if a[mid]==0:
            a[mid],a[l]=a[l],a[mid]
            l+=1
            mid+=1
        elif a[mid]==2:
            a[mid],a[r]=a[r],a[mid]
            r-=1
        else:
            mid+=1
    return a
    
a= [0, 1, 2, 0, 1, 2]
print(sol(a))