class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            min=i
            for j in range(i,len(nums)):
                if nums[j]<nums[min]:
                    min=j
            nums[i],nums[min]=nums[min],nums[i]

        