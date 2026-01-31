class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        let=sorted(heights)
        left=0
        right=0
        count=0
        while left<len(heights) and right<len(let):
            if heights[left]!=let[right]:
                count+=1
            left+=1
            right+=1
        return count
        