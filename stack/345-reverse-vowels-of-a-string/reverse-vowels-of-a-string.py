class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        l=list(s)
        left=0
        right=len(l)-1
        while left<right:
            while left<right and l[left] not in vowels:
                left+=1
            while left<right and l[right] not in vowels:
                right-=1
            l[left],l[right]=l[right],l[left]
            left+=1
            right-=1
        
        return "".join(l)


        