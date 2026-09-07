# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pari=deque([root])
        result=[]
        c=1
        if not root:
            return []
        while pari:
            leng=len(pari)
            level=[]
            if c==1:
                for i in range(leng):
                    node=pari.popleft()
                    level.append(node.val)
                    if node.left:
                        pari.append(node.left)
                    if node.right:
                        pari.append(node.right)
                c==0
            if c==0:
                for i in range(leng):
                    node=pari.popleft()
                    level.append(node.val)
                    if node.right:
                        pari.append(node.left)
                    if node.left:
                        pari.append(node.right)
                c==1
            result.append(level)
        return result

        