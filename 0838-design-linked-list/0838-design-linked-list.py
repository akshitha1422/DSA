class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        n=self.head
        count=0
        while n!=None:
            if count==index:
                return n.val
            n=n.next
            count+=1
        return -1

    def addAtHead(self, val: int) -> None:
        nn=node(val)
        nn.next=self.head
        self.head=nn

    def addAtTail(self, val: int) -> None:
        nn=node(val)
        if self.head==None:
            self.head=nn
            return
        n=self.head
        while n.next!=None:
            n=n.next
        n.next=nn

    def addAtIndex(self, index: int, val: int) -> None:
        nn=node(val)
        if index==0:
            nn.next=self.head
            self.head=nn
            return
        count=0
        prev=None
        n=self.head
        while n!=None:
            if count==index:
                break
            prev=n
            n=n.next
            count+=1
        if count==index:
            nn.next=n
            if prev:
                prev.next=nn

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return 
        n=self.head
        if index==0:
            self.head=self.head.next
            return
        count=0
        prev=None
        curr=self.head
        while curr and curr.next:
            if count==index-1:
                curr.next=curr.next.next
                return
            curr=curr.next
            count+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)