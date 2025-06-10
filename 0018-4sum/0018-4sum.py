class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        st=[]
        for m in range(len(nums)-3):
            if m>0 and nums[m]==nums[m-1]:
                continue
            for n in range(m+1,len(nums)-2):
                if n>m+1 and nums[n]==nums[n-1]:
                    continue
                i=n+1
                j=len(nums)-1
                while i<j:
                    curr = nums[m] + nums[n] + nums[i] + nums[j]
                    if curr==target:
                        st.append([nums[m],nums[n],nums[i],nums[j]])
                        while i<j and nums[i]==nums[i+1]:
                            i+=1
                        while i<j and nums[j]==nums[j-1]:
                            j-=1
                        i+=1
                        j-=1
                    elif curr<target:
                        i+=1
                    elif curr>target:
                        j-=1
        return st