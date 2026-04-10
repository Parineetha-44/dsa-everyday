class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        i=0
        count=0
        for i in range(len(grid)):
            j=0
            for j in range(len(grid[i])):
                if grid[i][j]<0:
                    count+=1
        return count


        