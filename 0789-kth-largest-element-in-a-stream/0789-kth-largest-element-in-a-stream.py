class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.items=[]
        self.k=k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.items.append(val)
        self.heapify_up(len(self.items)-1)
        if len(self.items)>self.k:
                self.pop()
        return self.items[0]

    def pop(self):
        if not self.items:
            return
        if len(self.items)==1:
            return self.items[0]
        root=self.items[0]
        self.items[0]=self.items.pop()
        self.heapify_down(0)
        return root
    def heapify_up(self,idx):
        while idx>0:
            parent=(idx-1)//2
            if self.items[idx]>=self.items[parent]:
                break
            self.items[idx],self.items[parent]=self.items[parent],self.items[idx]
            idx=parent
    def heapify_down(self,idx):
        n=len(self.items)
        while True:
            smallest=idx
            left=2*idx+1
            right=2*idx+2
            if left<n and self.items[left]<self.items[smallest]:
                smallest=left
            if right<n and self.items[right]<self.items[smallest]:
                smallest=right
            if smallest==idx:
                break
            self.items[idx],self.items[smallest]=self.items[smallest],self.items[idx]
            idx=smallest