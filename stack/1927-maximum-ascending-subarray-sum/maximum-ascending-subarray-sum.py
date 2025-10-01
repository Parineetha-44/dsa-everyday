class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum=nums[0]
        maxs=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum+=nums[i]
            else:
                sum=nums[i]
            
            maxs=max(sum,maxs)

                
        return maxs
        