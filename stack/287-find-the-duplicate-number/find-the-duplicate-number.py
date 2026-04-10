class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        i=0
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        for x in freq:
            if freq[x]>1:
                return x
        