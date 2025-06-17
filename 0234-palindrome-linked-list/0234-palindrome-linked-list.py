# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow
        prev=None
        while curr:
            nn=curr.next
            curr.next=prev
            prev=curr
            curr=nn
        left=head
        right=prev
        while right:
            if left.val!=right.val:
                return False
            right=right.next
            left=left.next
        return True