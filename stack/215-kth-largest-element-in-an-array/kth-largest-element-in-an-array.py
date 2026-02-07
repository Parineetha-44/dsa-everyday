import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pari=[]  
        for num in nums:
            negative=-num
            pari.append(negative)
        heapq.heapify(pari)
        count=1
        while count<k:
            heapq.heappop(pari)
            count+=1
        largest= -(heapq.heappop(pari))
        return largest
