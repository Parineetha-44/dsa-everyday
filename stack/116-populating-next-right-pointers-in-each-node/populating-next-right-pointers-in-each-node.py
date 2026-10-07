"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        pari=deque([root])
        if root==None:
            return None
        while pari:
            n=len(pari)
            for i in range(n):
                node=pari.popleft()
                if i<n-1:
                    node.next=pari[0]
                if node.left:
                    pari.append(node.left)
                if node.right:
                    pari.append(node.right)
        return root




