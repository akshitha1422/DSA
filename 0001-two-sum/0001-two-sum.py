class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st={}
        for i,num in enumerate(nums):
            need=target-num
            if need in st:
                return [st[need],i]
            st[num]=i

        # st=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             st.append(i)
        #             st.append(j)
        # return st