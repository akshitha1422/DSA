class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def __init__(self):
        self.root=TrieNode()
        self.nodes={}
    
    def insert(self,word):
        node=self.root
        for ch in reversed(word):
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        self.nodes[word]=node

    def minimumLengthEncoding(self, words: List[str]) -> int:
        words=list(set(words))
        words.sort(key=lambda w: -len(w))

        res=0

        for word in words:
            self.insert(word)
    
        for word,node in self.nodes.items():
            if not node.children:
                res+=len(word)+1
        return res