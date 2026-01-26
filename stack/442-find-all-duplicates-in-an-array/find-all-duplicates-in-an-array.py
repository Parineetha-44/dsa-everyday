class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq={}
        pari=[]
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        for x in freq:
            if freq[x]==2:
                pari.append(x)
        return pari
        