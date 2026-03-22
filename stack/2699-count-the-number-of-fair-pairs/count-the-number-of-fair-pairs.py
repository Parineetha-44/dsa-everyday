class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        cl=0
        while i<j:
            if nums[i]+nums[j]<lower:
                cl+=(j-i)
                i+=1
            else:
                j-=1
        i=0
        j=len(nums)-1
        cu=0
        while i<j:
            if nums[i]+nums[j]<=upper:
                cu+=(j-i)
                i+=1
            else:
                j-=1
        return cu-cl
        
            
