class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pari=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==pari:
                count+=1
            else:
                count-=1
                if count==0:
                    pari=nums[i]
                    count=1
        return pari

