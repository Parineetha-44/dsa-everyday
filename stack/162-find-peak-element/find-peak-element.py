class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max=nums[0]
        pos=0
        for i in range(len(nums)):
            if nums[i]>max:
                max=nums[i]
                pos=i
        return pos
        