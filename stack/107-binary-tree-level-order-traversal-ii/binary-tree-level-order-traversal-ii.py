# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        pari=deque([root])
        ans=[]
        if root is None:
            return ans
        while pari:
            n=len(pari)
            level=[]
            for i in range(n):
                node=pari.popleft()
                level.append(node.val)
                if node.left:
                    pari.append(node.left)
                if node.right:
                    pari.append(node.right)
            ans.append(level)
        return ans[::-1]    

        