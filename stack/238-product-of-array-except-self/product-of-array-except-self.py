class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pari=[1]*len(nums)
        pr=1
        su=1
        for i in range(len(nums)):
            pari[i]=pr
            pr*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            pari[i]*=su
            su*=nums[i]
        return pari
        

        