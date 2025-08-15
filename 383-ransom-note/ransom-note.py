class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count=Counter(ransomNote)
        magazine_count=Counter(magazine)
        for ch,needed in ransom_count.items():
            if magazine_count[ch]<needed:
                return False
        return True
