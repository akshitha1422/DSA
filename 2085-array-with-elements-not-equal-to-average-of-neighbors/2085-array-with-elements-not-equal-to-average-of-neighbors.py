class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        left=0
        right=len(nums)-1
        res=[]
        while left<=right:
            if left==right:
                res.append(nums[left])
            else:
                res.append(nums[left])
                res.append(nums[right])
            left+=1
            right-=1
        return res
        # 284/291
        # def dfs(i):
        #     if nums[i]==(nums[i-1]+nums[i+1])/2:
        #         nums[i],nums[i-1]=nums[i-1],nums[i]
        # for i in range(1,len(nums)-1):
        #     dfs(i)
        # return nums