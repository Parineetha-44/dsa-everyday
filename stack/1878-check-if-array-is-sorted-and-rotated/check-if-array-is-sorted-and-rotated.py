class Solution:
    def check(self, nums: List[int]) -> bool:
        p=len(nums)
        count=0
        for i in range(p):
            if nums[i]>nums[(i+1)%p]:
                count+=1
        if count>1:
            return False
        return True
        