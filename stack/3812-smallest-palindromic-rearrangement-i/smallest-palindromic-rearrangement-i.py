class Solution:
    def smallestPalindrome(self, s: str) -> str:
        s = sorted(s)
        pari = []
        mid = ""

        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                pari.append(s[i])
                i += 2
            else:
                mid = s[i]
                i += 1

        pari = "".join(pari)
        return pari + mid + pari[::-1]