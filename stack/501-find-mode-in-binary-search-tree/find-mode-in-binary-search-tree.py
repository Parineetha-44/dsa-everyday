# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        freq={}
        ans=[]
        p=[root]
        while p:
            node=p.pop()
            if node.val in freq:
                freq[node.val]+=1
            else:
                freq[node.val]=1
            if node.left:
                p.append(node.left)
            if node.right:
                p.append(node.right)
        maxf=0
        for x in freq:
            if freq[x]>maxf:
                maxf=freq[x]
        for x in freq:
            if freq[x]==maxf:
                ans.append(x)            
           
        return ans

        