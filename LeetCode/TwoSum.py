class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)):

                count=nums[i]+nums[j]
                if count==target:
                    return i,j
                count=0