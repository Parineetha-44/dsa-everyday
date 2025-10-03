class Solution:
    def removeStars(self, s: str) -> str:
        pari=[]
        for i in range(len(s)):
            if s[i].isalpha():
                pari.append(s[i])
            if s[i]=="*":
                pari.pop()
        return "".join(pari)
        