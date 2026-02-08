class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pari={}
        for x in nums:
            if x in pari:
                pari[x]+=1
            else:
                pari[x]=1
        real = list(set(nums))
        real.sort(key=lambda x: pari[x], reverse=True)
        return real[:k]
    
        
    

        