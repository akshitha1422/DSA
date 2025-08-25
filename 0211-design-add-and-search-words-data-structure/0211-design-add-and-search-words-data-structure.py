class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        if not word:
            return
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True

    def search(self, word: str) -> bool:
        def helper(node,dep):
            if dep==len(word):
                return node.is_end
            ch=word[dep]
            if ch=='.':
                for child in node.children.values():
                    if helper(child,dep+1):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return helper(node.children[ch],dep+1)
        return helper(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)