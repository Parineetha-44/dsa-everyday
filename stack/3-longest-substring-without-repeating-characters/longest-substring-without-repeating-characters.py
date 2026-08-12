class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        l=0
        length=0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]]=1
            while freq[s[r]]>1:
                freq[s[l]]-=1
                l+=1
            length=max(length,r-l+1)
        return length