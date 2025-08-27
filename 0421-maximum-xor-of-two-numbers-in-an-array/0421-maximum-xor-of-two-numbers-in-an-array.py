class TrieNode:
    def __init__(self):
        self.children = [None,None]

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,num):
        node=self.root
        for i in range(31,-1,-1):
            bit=(num>>i)&1
            if node.children[bit] is None:
                node.children[bit]=TrieNode()
            node=node.children[bit]

    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)
        res=0
        for num in nums:
            node=self.root
            curr=0
            for n in range(31,-1,-1):
                bit=(num>>n)&1
                opp=1-bit
                if node.children[opp] is not None:
                    curr=(curr<<1)|1
                    node=node.children[opp]
                else:
                    curr=(curr<<1)|0
                    node=node.children[bit]
            res=max(res,curr)
        return res