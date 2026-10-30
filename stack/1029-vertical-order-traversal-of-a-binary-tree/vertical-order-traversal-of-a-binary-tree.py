# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        p=[(root,0,0)]
        d={}
        while p:
            node,row,col=p.pop(0)
            if col not in d:
                d[col]=[]
            d[col].append((row,node.val))
            if node.left:
                p.append((node.left,row+1,col-1))
            if node.right:
                p.append((node.right,row+1,col+1))
        ans=[]
        for col in sorted(d):
            veena=sorted(d[col])
            a=[]
            for row,val in veena:
                a.append(val)
            ans.append(a)
        return ans