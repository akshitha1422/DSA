class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st={}
        for i,n in enumerate(nums):
            if (target-n) in st:
                return [st[target-n],i]
            else:
                st[n]=i
        
     # st=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             st.append(i)
        #             st.append(j)
        # return st