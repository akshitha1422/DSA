# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        st=[]
        for l in lists:
            head=l
            while head:
                st.append(head.val)
                head=head.next
        st.sort()
        dummy=ListNode(0)
        tail=dummy
        for s in st:
            tail.next=ListNode(s)
            tail=tail.next
        return dummy.next