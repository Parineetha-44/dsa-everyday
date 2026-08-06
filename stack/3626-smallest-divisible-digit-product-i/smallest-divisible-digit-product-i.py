class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i=n
        while i>=n:
            x=1
            temp=i
            while temp>0:
                r=temp%10
                x*=r
                temp=temp//10
            if x%t==0:
                return i
            i+=1

