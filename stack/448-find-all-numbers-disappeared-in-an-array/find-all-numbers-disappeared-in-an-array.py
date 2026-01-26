class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        pari=[]
        i=0
        n=len(nums)
        while i<n:
            x=nums[i]
            if 1<=x<=n and nums[x-1]!=nums[i]:
                nums[i],nums[x-1]=nums[x-1],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                pari.append(i+1)
        return pari
        