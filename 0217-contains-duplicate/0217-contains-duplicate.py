class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st=set()
        for n in nums:
            if n in st:
                return True
            else:
                st.add(n)
        return False