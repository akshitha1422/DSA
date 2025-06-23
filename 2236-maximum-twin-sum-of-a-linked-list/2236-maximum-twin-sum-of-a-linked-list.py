# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals=[]
        max_val=0
        while head:
            vals.append(head.val)
            head=head.next
        for i in range(len(vals)//2):
            max_val=max(max_val,(vals[i]+vals[len(vals)-i-1]))
        return max_val