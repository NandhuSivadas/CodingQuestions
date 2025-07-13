nums1 = [1,3]
nums2 = [2]
nums1.append(nums2)
nums1.sort()
if (len(nums1)%2)-1!=0:
    k=(len(nums1)-1)/2
    print(k)
else:
     k=(len(nums1)-1)/2
     print((nums1[k]+nums1[k+1]))/2
    
