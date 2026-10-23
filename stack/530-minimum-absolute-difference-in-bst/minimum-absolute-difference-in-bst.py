# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        p=[root]
        x=[]
        while p:
            node=p.pop()
            x.append(node.val)
            if node.left:
                p.append(node.left)
            if node.right:
                p.append(node.right)
        x.sort()
        ans=float('inf')
        for i in range(len(x)):
            ans=min(abs(x[i]-x[i-1]),ans)

        return ans
        
