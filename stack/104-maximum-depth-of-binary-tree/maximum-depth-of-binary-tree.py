# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pari=deque([root])
        ans=[]
        if not root:
            return 0
        while pari:
            leng=len(pari)
            level=[]
            for i in range(leng):
                node=pari.popleft()
                level.append(node.val)
                if node.left:
                    pari.append(node.left)
                if node.right:
                    pari.append(node.right)
            ans.append(level)
        return len(ans)      

