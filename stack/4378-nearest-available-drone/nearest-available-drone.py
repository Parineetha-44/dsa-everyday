class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        c=float('inf')
        minii=-1
        for i in range(len(drones)):
            x=0
            for j in range(len(drones[i])-1):
                x+=abs(drones[i][j]-target[j])
            if x<=drones[i][2]:
                if x<c or c==-1:
                    c=x
                    minii=i
                
        return minii