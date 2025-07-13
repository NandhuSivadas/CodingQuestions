def rotate(nums, k):
    n = len(nums)
    k %= n

    # Reverse entire list
    nums.reverse()
    print(nums)

    # Reverse first k elements
    nums[:k] = reversed(nums[:k])
    print(nums)

    # Reverse the rest
    nums[k:] = reversed(nums[k:])
    print(nums)

nums = [1, 2, 3, 4, 5, 6, 7]
rotate(nums, 3)
print(nums)
