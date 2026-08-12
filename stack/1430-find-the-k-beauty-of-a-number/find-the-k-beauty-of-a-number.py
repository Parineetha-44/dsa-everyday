class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        x=str(num)
        c=0
        for i in range(len(x)-k+1):
            p=x[i:i+k]
            val=int(p)
            if val!=0 and (num%val)==0:
                c+=1
        return c
            

                