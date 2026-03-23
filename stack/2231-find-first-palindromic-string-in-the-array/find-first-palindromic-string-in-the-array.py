class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        i=0
        j=""
        for i in range(len(words)):
            if words[i]==words[i][::-1]:
                j=words[i]
                break
        return j


                
        