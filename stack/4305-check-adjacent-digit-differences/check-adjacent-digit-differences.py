class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        i=0
        j=1
        r=list(s)
        x=True
        while j<len(r):
            if abs(ord(r[i])-ord(r[j]))>2:
                x=False
                break
            i+=1
            j+=1
        return x
        
        