class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pari=0
        for i in range(len(nums)):
            pari=pari^nums[i]
        return pari
        