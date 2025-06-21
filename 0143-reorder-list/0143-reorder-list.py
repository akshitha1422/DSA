# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            n=curr.next
            curr.next=prev
            prev=curr
            curr=n
        first,second=head,prev
        while second:
            n=first.next
            m=second.next
            first.next=second
            second.next=n
            first=n
            second=m

