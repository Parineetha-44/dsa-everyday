"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        pari=[root]
        c=0
        while pari:
            level=[]
            for i in range(len(pari)):
                node=pari.pop(0)
                for children in node.children:
                    level.append(children)
            pari = level
            c+=1
        return c
                
                
        