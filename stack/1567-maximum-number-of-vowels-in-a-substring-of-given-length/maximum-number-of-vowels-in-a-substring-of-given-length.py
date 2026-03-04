class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        q={'a','e','i','o','u'}
        count=0
        for i in range(k):
            if s[i] in q:
                count+=1
        maxcount=count
        for i in range(k,len(s)):
            if s[i] in q:
                count+=1
            if s[i-k] in q:
                count-=1
            maxcount=max(maxcount,count)
        return maxcount
            

        