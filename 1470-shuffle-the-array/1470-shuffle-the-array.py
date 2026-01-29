class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        st=[]
        for i in range(n):
            st.append(nums[i])
            st.append(nums[i+n])
        return st