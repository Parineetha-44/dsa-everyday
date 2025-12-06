class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        count1=0
        count2=0
        pari=list(s)
        for i in range(len(pari)):
            if pari[i]=="a":
                count1+=1
            if pari[i]=="b":
                count2+=1
        return abs(count1-count2)