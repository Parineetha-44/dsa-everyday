class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        bottle=0
        charger=0
        for i in range(len(nums)):
            if nums[i]>0:
                bottle+=1
            elif nums[i]<0:
                charger+=1
        return max(charger,bottle)
        