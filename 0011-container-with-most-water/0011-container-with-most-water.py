class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val=0
        left=0
        right=len(height)-1
        while left<right:
            content=(right-left)*min(height[left],height[right])
            max_val=max(content,max_val)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_val