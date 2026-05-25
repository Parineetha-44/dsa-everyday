class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        for x in freq:
            if freq[x]==1:
                return x