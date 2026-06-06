class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq={}
        ans=0
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for x in freq:
            if x+1 in freq:
                ans=max(ans,freq[x]+freq[x+1])
        return ans