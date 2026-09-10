# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s=[]
        t=[]
        s.append(p)
        t.append(q)
        
        while s and t:
            node1=s.pop()
            node2=t.pop()
            if node1 is None and node2 is None:
               continue
            if node1 is None or node2 is None:
                return False
            if node1.val!=node2.val:
                return False
            s.append(node1.left)
            t.append(node2.left)
            s.append(node1.right)
            t.append(node2.right)
        return True

        