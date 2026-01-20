class Solution:
    def isHappy(self, n: int) -> bool:
        while n!=4 and n!=1:
            y=0
            p=n
            while p>0:
                x=p%10
                p=p//10
                y+=x**2
            n=y
        if n==1:
            return True
        else:
            return False
        


        