# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        pari=deque([root])
        while pari:
            n=len(pari)
            for i in range(n):
                node=pari.popleft()
                if i==0:
                    x=node.val
                if node.left:
                    pari.append(node.left)
                if node.right:
                    pari.append(node.right)
        return x

    


        