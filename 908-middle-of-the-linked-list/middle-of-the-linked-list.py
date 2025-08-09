# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            temp=temp.next
            count=count+1
        index=count//2
        curr=head
        for i in range(index):
            curr=curr.next
        return curr


        