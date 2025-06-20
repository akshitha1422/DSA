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
        h1=l1
        h2=l2
        num1=0
        num2=0
        exp=0
        while h1!=None:
            n=h1.val
            num1+=n*(10**exp)
            exp+=1
            h1=h1.next
        exp=0
        while h2!=None:
            n=h2.val
            num2+=n*(10**exp)
            exp+=1
            h2=h2.next
        num3=str(num1+num2)
        for i in reversed(num3):
            new.next=ListNode(int(i))
            new=new.next
        return dummy.next