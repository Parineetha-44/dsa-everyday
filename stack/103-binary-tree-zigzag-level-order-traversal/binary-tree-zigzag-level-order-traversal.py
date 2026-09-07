# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pari=deque([root])
        result=[]
        c=False
        if not root:
            return []
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
            if c:
                level.reverse()
            result.append(level)
            c=not c
        return result

        
        