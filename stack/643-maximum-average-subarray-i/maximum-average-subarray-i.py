class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current=sum(nums[:k])
        maximum=current
        for i in range(k,len(nums)):
            current+=nums[i]
            current-=nums[i-k]
            maximum=max(current,maximum)
        return maximum/k
        