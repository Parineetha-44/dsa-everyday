# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        p=[(root,False)]
        visited=False
        heights={}
        maxh=0
        while p:
            node,visited=p.pop()
            if node is None:
                continue
            if not visited:
                p.append((node,True))
                if node.left:
                    p.append((node.left,False))
                if node.right:
                    p.append((node.right,False))
            else:
                h1=heights.get(node.left,0)
                h2=heights.get(node.right,0)
                height=h1+h2
                if height>maxh:
                    maxh=height
                heights[node]=1+max(h1,h2)
        return maxh