class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        for i in range(k):
            summ+=nums[i]
        avgg=summ/k
        maxavg=avgg
        for i in range(k,len(nums)):
            summ+=nums[i]
            summ-=nums[i-k]
            avgg=summ/k
            maxavg=max(avgg,maxavg)
        return maxavg

