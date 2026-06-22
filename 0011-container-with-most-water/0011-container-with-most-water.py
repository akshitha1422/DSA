class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        res=0
        i=0
        while left<right:
            wd=right-left
            ht=min(height[left],height[right])
            vol=wd*ht
            res=max(res,vol)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res