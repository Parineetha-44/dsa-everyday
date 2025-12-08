class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1,n+1):
            for b in range(1,n+1):
                p=a**2+b**2
                r=int(p**0.5)
                if r*r==p and r<=n:
                    count+=1
        return count