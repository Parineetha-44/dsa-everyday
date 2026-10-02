# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        p=[root]
        s=0
        while p:
            node=p.pop()
            if node.left:
                s+=node.left.val
            if node.right:
                s+=node.right.val
            if s==node.val:
                return True
            else:
                return False
        