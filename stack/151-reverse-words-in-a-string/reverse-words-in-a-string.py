class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        p=reversed(words)
        return " ".join(p)
