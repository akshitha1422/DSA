class Node:
    def __init__(self,key,value):
        self.val=[key,value]
        self.next=None

class MyHashMap:

    def __init__(self):
        self.head=None

    def put(self, key: int, value: int) -> None:
        if self.head==None:
            self.head=Node(key,value)
            return
        n=self.head
        while n:
            if n.val[0]==key:
                n.val[1]=value
                return
            if n.next==None:
                break
            n=n.next
        n.next=Node(key,value)

    def get(self, key: int) -> int:
        n=self.head
        while n:
            if n.val[0]==key:
                return n.val[1]
            n=n.next
        return -1

    def remove(self, key: int) -> None:
        if not self.head:
            return
        if self.head.val[0]==key:
            self.head=self.head.next
            return
        prev=self.head
        curr=self.head.next
        while curr:
            if curr.val[0]==key:
                prev.next=curr.next
                return
            else:
                prev=curr
            curr=curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)