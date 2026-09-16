# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        p=[root]
        val=root.val
        while p:
            node=p.pop()
            if node.val!=val: 
                return False
            if node.left:
                p.append(node.left)
            if node.right:
                p.append(node.right)
        return True
        