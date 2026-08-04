class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        pari=[]
        p=1
        x=len(nums)
        minn=min(nums)
        maxx=max(nums)
        for i in range(minn,maxx):
            if i not in nums:
                pari.append(i)
        return pari
        