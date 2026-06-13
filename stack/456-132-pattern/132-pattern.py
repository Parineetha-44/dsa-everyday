class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        veena=[]
        sec=float('-inf')
        x=len(nums)
        for i in range(x-1,-1,-1):
            if nums[i]<sec:
                return True
            while veena and nums[i]>veena[-1]:
                sec=veena.pop()
            veena.append(nums[i])
        return False