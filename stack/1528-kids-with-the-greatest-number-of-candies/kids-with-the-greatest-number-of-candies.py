class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        pari=[]
        maxC=max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxC:
                pari.append(True)
            else:
                pari.append(False)
        return pari


        