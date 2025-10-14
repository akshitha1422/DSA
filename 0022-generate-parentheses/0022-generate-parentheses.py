class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(curr,openc,closec):
            if len(curr)==2*n:
                res.append(curr)
                return
            if openc<n:
                backtrack(curr+'(',openc+1,closec)
            if closec<openc:
                backtrack(curr+')',openc,closec+1)
        backtrack('',0,0)
        return res