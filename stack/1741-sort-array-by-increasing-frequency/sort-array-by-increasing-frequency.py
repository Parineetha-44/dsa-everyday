class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        pari={}
        for x in nums:
            if x in pari:
                pari[x]+=1
            else:
                pari[x]=1
        nums.sort(key=lambda x: (pari[x], -x))
        return nums