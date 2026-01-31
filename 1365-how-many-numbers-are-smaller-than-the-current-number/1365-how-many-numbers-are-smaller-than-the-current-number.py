class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        st=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            st.append(count)
            count=0
        return st