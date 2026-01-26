class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        pari=[]
        n=len(nums)
        lost=found=-1
        freq=[0]*(n+1)
        for x in nums:
            freq[x]+=1
        for i in range(1,n+1):
            if freq[i]==2:
                found=i
            elif freq[i]==0:
                lost=i
        pari.append(found)
        pari.append(lost)
        return pari
    

        