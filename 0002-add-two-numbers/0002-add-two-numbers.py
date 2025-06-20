# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        new=dummy
        prev=None
        num1=0
        num2=0
        exp=0
        while l1!=None:
            num1+=(l1.val)*(10**exp)
            exp+=1
            l1=l1.next
        exp=0
        while l2!=None:
            num2+=(l2.val)*(10**exp)
            exp+=1
            l2=l2.next
        num3=str(num1+num2)
        for i in reversed(num3):
            new.next=ListNode(int(i))
            new=new.next
        return dummy.next