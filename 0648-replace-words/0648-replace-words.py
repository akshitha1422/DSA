class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  

class Solution:
    def __init__(self):
        self.root=TrieNode()
        self.is_end=False

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True

    def shortest(self,word):
        node=self.root
        prefix=''
        for ch in word:
            if ch not in node.children:
                break
            prefix+=ch
            node=node.children[ch]
            if node.is_end:
                return prefix
        return word

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for root in dictionary:
            self.insert(root)
        words=sentence.split()
        replace=[self.shortest(word) for word in words]
        return ' '.join(replace)
