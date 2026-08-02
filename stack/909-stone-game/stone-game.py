from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def p(i,j):
            if i == j:
                return piles[i]
            left= piles[i]- p(i+1,j)
            right= piles[j]- p(i,j-1)
            return max(left,right)
        return p(0, len(piles) - 1) >= 0
