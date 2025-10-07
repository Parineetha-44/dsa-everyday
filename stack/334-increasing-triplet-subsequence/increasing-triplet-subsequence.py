class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pari=float('inf')
        neetha=float('inf')
        for a in nums:
            if a<=pari:
                pari=a
            elif a<=neetha:
                neetha=a
            else:
                return True
        return False