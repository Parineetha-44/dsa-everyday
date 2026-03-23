class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pari=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                pari.append(nums[i])
        for i in range(len(nums)):
            if nums[i]%2!=0:
                pari.append(nums[i])
        return pari