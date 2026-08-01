class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(i, j):
            if i == j:
                return nums[i]
            
            take_left = nums[i] - solve(i + 1, j)
            take_right = nums[j] - solve(i, j - 1)
            
            return max(take_left, take_right)
        
        return solve(0, len(nums) - 1) >= 0