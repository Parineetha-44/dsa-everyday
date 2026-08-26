class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count=[0,0,0] 
        pari=0
        l=0
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            while count[0]>0 and count[1]>0 and count[2]>0:
                pari+=len(s)-i
                count[ord(s[l])-ord('a')]-=1
                l+=1
        return pari
