class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        st=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                st.append(i)
        return st