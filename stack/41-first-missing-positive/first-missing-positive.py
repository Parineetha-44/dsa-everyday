class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            x=nums[i]
            if 1<=x<=n and nums[x-1]!=x:
                nums[x-1],nums[i]=nums[i],nums[x-1]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1

        