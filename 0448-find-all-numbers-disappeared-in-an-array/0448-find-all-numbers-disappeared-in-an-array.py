class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        st=[]
        for i in nums:
            idx=abs(i)-1
            nums[idx]=-abs(nums[idx])
        for i in range(len(nums)):
            if nums[i]>0:
                st.append(i+1)
        return st
        # s=set(nums)
        # st=[]
        # for i in range(1,len(nums)+1):
        #     if i not in s:
        #         st.append(i)
        # return st