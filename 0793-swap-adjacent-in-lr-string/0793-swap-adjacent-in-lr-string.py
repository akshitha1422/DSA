class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        if start.replace('X','')!=result.replace('X',''):
            return False
        i=0
        j=0
        while i<len(start) and j<len(result):
            while i<len(start) and start[i]=='X':
                i+=1
            while j<len(result) and result[j]=='X':
                j+=1
            if i==len(start) and j==len(result):
                return True
            if i==len(start) or j==len(result):
                return False
            if start[i]!=result[j]:
                return False
            if start[i]=='L' and i<j:
                return False
            if start[i]=='R' and i>j:
                return False
            i+=1
            j+=1
        return True