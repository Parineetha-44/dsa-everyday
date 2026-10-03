# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        p=[(root,float(-inf),float(inf))]
        while p:
            node,low,high=p.pop()
            if node.val<=low or node.val>=high:
                return False
            if node.left:
                p.append((node.left,low,node.val))
            if node.right:
                p.append((node.right,node.val,high))
        return True