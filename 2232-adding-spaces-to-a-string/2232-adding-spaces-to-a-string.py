class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=0
        res=[]
        for j in spaces:
            res.append(s[i:j])
            i=j
        res.append(s[j:])
        return " ".join(res)