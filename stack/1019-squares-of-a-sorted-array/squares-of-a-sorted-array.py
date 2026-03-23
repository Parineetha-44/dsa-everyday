class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pari=[]
        for i in range(len(nums)):
            pari.append(nums[i]*nums[i])
        return sorted(pari)

        