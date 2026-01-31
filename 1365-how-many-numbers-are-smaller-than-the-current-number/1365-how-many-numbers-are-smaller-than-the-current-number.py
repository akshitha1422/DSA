class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums=sorted(nums)
        st=[]
        for n in nums:
            i=sorted_nums.index(n)
            st.append(i)
        return st

        # st=[]
        # for i in range(len(nums)):
        #     count=0
        #     for j in range(len(nums)):
        #         if nums[j]<nums[i]:
        #             count+=1
        #     st.append(count)
        # return st