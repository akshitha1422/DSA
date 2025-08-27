class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word=None

class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()
            node=node.children[ch]
        node.is_end=True
        node.word=word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
        rows=len(board)
        cols=len(board[0])
        res=set()
        def dfs(node,r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            ch=board[r][c]
            if ch not in node.children:
                return
            nxt=node.children[ch]
            if nxt.is_end:
                res.add(nxt.word)
            board[r][c]='#'

            dfs(nxt,r-1,c)
            dfs(nxt,r+1,c)
            dfs(nxt,r,c-1)
            dfs(nxt,r,c+1)
            
            board[r][c]=ch
        for r in range(rows):
            for c in range(cols):
                dfs(self.root,r,c)
        return list(res)