# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        p=[root]
        sum=0
        while p:
            node=p.pop()
            if node.left:
                if node.left.left is None and node.left.right is None:
                    sum+=node.left.val
                else:
                    p.append(node.left)
            if node.right:
                p.append(node.right)
          
        return sum
        