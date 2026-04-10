class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i=0
        x=letters[0]
        for i in range(len(letters)):
            if letters[i]>target:
                x=letters[i]
                return x
        return x

        
                
