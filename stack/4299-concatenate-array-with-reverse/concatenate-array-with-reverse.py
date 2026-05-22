class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        x=len(nums)
        pari=[]
        for i in range(x):
            pari.append(nums[i])
        for i in range(x-1,-1,-1):
            pari.append(nums[i])
        return pari
        