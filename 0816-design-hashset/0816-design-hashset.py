class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyHashSet:

    def __init__(self):
        self.head=None

    def add(self, key: int) -> None:
        nn=Node(key)
        if self.head==None:
            self.head=nn
            return
        n=self.head
        while n!=None:
            if n.val==key:
                return 
            if n.next==None:
                break
            n=n.next
        n.next=nn

    def remove(self, key: int) -> None:
        n=self.head
        if n==None:
            return
        if n.val==key:
            self.head=n.next
            return
        prev=n
        n=n.next
        while n!=None:
            if n.val==key:
                prev.next=n.next
                return
            prev=n
            n=n.next

    def contains(self, key: int) -> bool:
        n=self.head
        while n!=None:
            if n.val==key:
                return True
            n=n.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)