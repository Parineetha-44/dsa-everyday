class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        zero=0
        odd=0
        p=0
        c=0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                odd+=1
                zero=0
            while odd==k:
                zero+=1
                if nums[p]%2!=0:
                    odd-=1
                p+=1
            c+=zero
        return c