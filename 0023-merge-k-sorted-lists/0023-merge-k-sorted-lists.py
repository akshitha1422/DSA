# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        st=[]
        for i in lists:
            head=i
            while head:
                st.append(head.val)
                head=head.next
        st.sort()
        print(st)
        dummy=ListNode(0)
        tail=dummy
        for i in st:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next