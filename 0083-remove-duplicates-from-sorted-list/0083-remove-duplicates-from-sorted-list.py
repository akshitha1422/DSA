# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy=ListNode(0)
        # dummy.next=head
        prev=None
        curr=head
        st=[]
        while curr:
            if curr.val in st:
                prev.next=curr.next
            else:
                st.append(curr.val)
                prev=curr
            curr=curr.next
        return head