# John works in a coin factory where each coin has an ID. He has an array 'nums' of size N. In the factory,
# coins are assigned to boxes based on the sum of the digits of their IDs. For example, if the ID of a coin is 321,
#  the sum of its digits is 6 (since 3 + 2 + 1 = 6), so the coin will be placed in box 6.
# John has been given a task to work with coins that have IDs in the range from the smallest number in 'nums',
#  called the low limit, to the largest number in 'nums', called the high limit. For each number in this range (from low-limit to high-limit, inclusive), 
# John needs to calculate the sum of the digits and place the coin in the corresponding box.

def box(nums):
    dict={}
    low=min(nums)
    high=max(nums)
    for i in range(low,high+1):
        s=sum(int(d) for d in str(i))
        if s in dict:
            dict[s]+=1
        else:
            dict[s]=1
    return dict

nums=[152,56,234]   
print(box(nums))