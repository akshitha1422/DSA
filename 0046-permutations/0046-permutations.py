class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(arr,rem):
            if not rem:
                res.append(arr[:])
                return
            for i in range(len(rem)):
                num=rem[i]
                arr.append(num)
                backtrack(arr,rem[:i]+rem[i+1:])
                arr.pop()
        backtrack([],nums)
        return res