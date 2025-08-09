# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(head):
            length=0
            curr=head
            while curr:
                length+=1
                curr=curr.next
            return length
        lenA=length(headA)
        lenB=length(headB)
        currA=headA
        currB=headB
        if lenA>lenB:
            for _ in range(lenA-lenB):
                currA=currA.next
        else:
            for _ in range(lenB-lenA):
                currB=currB.next
        while currA and currB:
            if currA==currB:
                return currA
            currA=currA.next
            currB=currB.next
        return None

                



        