class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        for x in freq:
            if freq[x]!=3:
                ans=x
        return ans
        