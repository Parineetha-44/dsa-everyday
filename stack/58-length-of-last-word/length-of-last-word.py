class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        word=s.split()
        if not word:
            return 0
        return len(word[-1])
        