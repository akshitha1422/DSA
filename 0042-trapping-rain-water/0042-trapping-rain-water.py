class Solution:
    def trap(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_left=max_right=0
        water=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=max_left:
                    max_left=height[left]
                else:
                    water+=abs(height[left]-max_left)
                left+=1
            else:
                if height[right]>=max_right:
                    max_right=height[right]
                else:
                    water+=abs(height[right]-max_right)
                right-=1
        return water