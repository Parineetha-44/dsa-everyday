class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        j=1
        while True:
            x=j
            r=True
            for i in range(len(nums)):
                x+=nums[i]
                if x<1:
                    r=False
                    break
            if r:
                return j
            j+=1
