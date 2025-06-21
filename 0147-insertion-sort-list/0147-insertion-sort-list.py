# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=head
        while curr:
            prev=dummy
            while prev.next and prev.next.val<curr.val:
                prev=prev.next
            n=curr.next
            curr.next=prev.next
            prev.next=curr
            curr=n
        return dummy.next