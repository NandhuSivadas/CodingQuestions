def merge():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3

    p1 = m - 1  # Last actual element in nums1
    p2 = n - 1  # Last element in nums2
    k = m + n - 1  # Last index in nums1

    # Merge from the end
    while p1 >= 0 and p2 >= 0:
        if nums2[p2] > nums1[p1]:
            nums1[k] = nums2[p2]
            p2 -= 1
        else:
            nums1[k] = nums1[p1]
            p1 -= 1
        k -= 1

    # Copy remaining elements from nums2, if any
    while p2 >= 0:
        nums1[k] = nums2[p2]
        p2 -= 1
        k -= 1

    print(nums1)

merge()