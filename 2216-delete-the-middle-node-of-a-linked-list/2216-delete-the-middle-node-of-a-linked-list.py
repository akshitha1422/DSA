# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        n=head
        while n.next!=slow:
            n=n.next
        n.next=n.next.next
        return head