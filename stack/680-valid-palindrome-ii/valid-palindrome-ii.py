class Solution:
    def validPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=[p for p in s if p.isalpha()]
        i=0
        j=len(a)-1
        while i<j:
            if a[i]!=a[j]:
                l,r=i+1,j
                veena=True
                while l<r:
                    if a[l]!=a[r]:
                        veena=False
                        break
                    l+=1
                    r-=1
                l,r=i,j-1
                pari=True
                while l<r:
                    if a[l]!=a[r]:
                        pari=False
                        break
                    l+=1
                    r-=1
                return pari or veena
            i+=1
            j-=1
        return True
                    

        