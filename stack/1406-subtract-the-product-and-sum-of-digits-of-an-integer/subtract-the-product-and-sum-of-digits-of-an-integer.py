class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        pro=1
        while n>0:
            x=n%10
            sum+=x
            pro*=x
            n=n//10
        return pro-sum 

        