class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        length=0
        freq={}
        for r in range(n):
            if nums[r] in freq:
                freq[nums[r]]+=1
            else:
                freq[nums[r]]=1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
            length=max(length,r-l+1)
        return length
        