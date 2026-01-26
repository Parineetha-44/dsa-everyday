class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        sum=0
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        for x in freq:
            if freq[x]==1:
                sum+=x
        return sum
        