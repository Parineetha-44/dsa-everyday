class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        j=num
        x=False
        while i<=j:
            mid=(i+j)//2
            if mid*mid==num:
                x=True
                break
            elif mid*mid<num:
                i=mid+1
            else:
                j=mid-1
        return x