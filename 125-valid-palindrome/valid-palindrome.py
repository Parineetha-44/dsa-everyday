class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered=""
        for ch in s:
            if ch.isalnum():
                filtered+=ch.lower()
        if filtered==filtered[::-1]:
            return True
        else:
            return False
        