# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        ans=[]
        if root is None:
            return ans
        pari=deque([root])
    
        while pari:
            n=len(pari)
            maxf=pari[0].val
            for i in range(n):
                node=pari.popleft()
                if node.val>maxf:
                    maxf=node.val
                if node.left:
                    pari.append(node.left)
                if node.right:
                    pari.append(node.right)
            ans.append(maxf)
        return ans


        