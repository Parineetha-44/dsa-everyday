class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t='1'+s+'1'
        ones=s.count('1')
        ans=ones
        i=1
        while i<len(t)-1:
            if t[i]=='1':
                j=i
                while j<len(t)-1 and t[j]=='1':
                    j+=1
                if t[i-1]=='0' and t[j]=='0':
                    l=i-1
                    while l>=0 and t[l]=='0':
                        l-=1
                    left=i-l-1
                    r=j
                    while r<len(t) and t[r]=='0':
                        r+=1
                    right=r-j
                    ans=max(ans,ones+left+right)
                i=j
            else:
                i+=1
        return min(len(s),ans)