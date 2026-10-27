class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        p=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    p.append((i,j))
        c=0
        fresh=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    fresh+=1
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        while p and fresh>0:
            level=[]
            for i in range(len(p)):
                node=p.pop(0)
                r,c1=node
                for dr,dc in directions:
                    nr=dr+r
                    nc=dc+c1
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1
                        level.append((nr,nc))
            p=level
            if p:
                c+=1
        if fresh>0:
            return -1
        return c

                
                
                
