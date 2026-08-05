class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        sum=0
        for i in range(k):
            sum+=arr[i]
        avg=sum/k
        if avg>=threshold:
            count+=1
        for i in range(k,len(arr)):
            sum+=arr[i]
            sum-=arr[i-k]
            avg=sum/k
            if avg>=threshold:
                count+=1
        return count