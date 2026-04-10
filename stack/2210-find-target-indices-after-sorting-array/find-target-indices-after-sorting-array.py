class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        pari=[]
        for i in range(len(nums)):
            if nums[i]==target:
                pari.append(i)
        return pari
        