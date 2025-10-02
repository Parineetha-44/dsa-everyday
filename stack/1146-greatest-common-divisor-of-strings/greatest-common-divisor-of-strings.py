class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ""
        else:
            def gcd(m,n):
                while n!=0:
                    m,n=n,m%n
                return m
            x=gcd(len(str1),len(str2))
        return str1[:x]


        