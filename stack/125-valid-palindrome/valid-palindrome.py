class Solution:
    def isPalindrome(self, s: str) -> bool:
        p=""
        for c in s:
            if c.isalnum():
                p+=c.lower()
        l=0
        r=len(p)-1
        while r>=l:
            if p[r]==p[l]:
                l+=1
                r-=1
            else:
                return False
        return True