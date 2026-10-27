# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        if not root1:
            return root2
        if not root2:
            return root1
        p=[root1]
        q=[root2]
        while p and q:
            node1=p.pop()
            node2=q.pop()
            node1.val=node1.val+node2.val
            if node1.left and node2.left:
                p.append(node1.left)
                q.append(node2.left)
            elif not node1.left:
                node1.left=node2.left
            if node1.right and node2.right:
                p.append(node1.right)
                q.append(node2.right)
            elif not node1.right:
                node1.right=node2.right
        return root1

        