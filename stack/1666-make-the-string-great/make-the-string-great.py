class Solution:
    def makeGood(self, s: str) -> str:
        pari=[]
        for c in s:
            if pari and abs(ord(pari[-1]) - ord(c)) == 32:
                pari.pop()
            else:
                pari.append(c)
        return "".join(pari)