class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        memo={}
        def helper(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if nums1[n-1]==nums2[m-1]:
                memo[(n,m)]=1+helper(n-1,m-1)
            else:
                memo[(n,m)]=max(helper(n-1,m),helper(n,m-1))
            return memo[(n,m)]
        return helper(n,m)