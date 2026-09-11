# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        p=[root]
        while p:
            node=p.pop()
            temp=node.left
            node.left=node.right
            node.right=temp
            if node.left:
                p.append(node.left)
            if node.right:
                p.append(node.right)
        return root
    
