# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        p=[(root,root.val)]
        x=0
        while p:
            node,x=p.pop()
            if node.left is None and node.right is None:
                if x==targetSum:
                    return True
            if node.left:
                p.append((node.left,x+node.left.val))
            if node.right:
                p.append((node.right,x+node.right.val))
        return False