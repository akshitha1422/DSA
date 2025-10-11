class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left=[]
        middle=[]
        right=[]
        for n in nums:
            if n<pivot:
                left.append(n)
            elif n==pivot:
                middle.append(n)
            else:
                right.append(n)
        return left+middle+right