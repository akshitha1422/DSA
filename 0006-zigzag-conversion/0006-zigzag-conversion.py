class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s
        rows=['']*numRows
        curr=0
        dirc=-1
        for ch in s:
            rows[curr]+=ch
            if curr==0 or curr==numRows-1:
                dirc*=-1
            curr+=dirc
        return ''.join(rows)