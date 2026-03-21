class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        j=n
        while i<=j:
            mid=(i+j)//2
            coins=(mid*(mid+1))//2
            if coins==n:
                return mid
            elif coins<n:
                i=mid+1
            else:
                j=mid-1
        return j
        