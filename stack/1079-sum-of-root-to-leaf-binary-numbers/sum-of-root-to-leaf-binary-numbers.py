# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        p=[(root,0)]
        ans=0
        while p:
            node,num=p.pop()
            num=num*2+node.val
            if not node.left and not node.right:
                ans+=num
            if node.left:
                p.append((node.left,num))
            if node.right:
                p.append((node.right,num))
        return ans

        