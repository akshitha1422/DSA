class Solution:
    def __init__(self):
        self.items=[]

    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in stones:
            self.add(i)

        while len(self.items)>1:
            x=self.pop()
            y=self.pop()
            if x!=y:
                diff=x-y
                self.add(diff)
        return self.items[0] if self.items else 0

    def add(self,x):
        self.items.append(x)
        self.heapify_up(len(self.items)-1)
    
    def heapify_up(self,idx):
        while idx>0:
            parent=(idx-1)//2
            if self.items[idx]<=self.items[parent]:
                break
            self.items[idx],self.items[parent]=self.items[parent],self.items[idx]
            idx=parent
    
    def heapify_down(self,idx):
        n=len(self.items)
        while True:
            largest=idx
            left=2*idx+1
            right=2*idx+2
            if left<n and self.items[left]>self.items[largest]:
                largest=left
            if right<n and self.items[right]>self.items[largest]:
                largest=right
            if largest==idx:
                break
            self.items[idx],self.items[largest]=self.items[largest],self.items[idx]
            idx=largest
    
    def pop(self):
        if not self.items:
            return
        if len(self.items)==1:
            return self.items.pop()
        root=self.items[0]
        self.items[0]=self.items.pop()
        self.heapify_down(0)
        return root