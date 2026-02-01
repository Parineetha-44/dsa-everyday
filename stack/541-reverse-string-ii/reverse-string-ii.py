class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p=list(s)
        for i in range(0,len(p),2*k):
            p[i:i+k]=p[i:i+k][::-1]
        return "".join(p)

