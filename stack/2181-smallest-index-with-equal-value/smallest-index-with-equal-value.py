class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        min=0
        for i in range(len(nums)):
            if i%10==nums[i]:
                return i
        return -1        