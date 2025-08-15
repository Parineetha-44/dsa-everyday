class Solution:
    def longestPalindrome(self, s: str) -> str:
        long=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                small=s[i:j+1]
                if small==small[::-1] and len(small)>len(long):
                    long=small
        return long
    
            
        