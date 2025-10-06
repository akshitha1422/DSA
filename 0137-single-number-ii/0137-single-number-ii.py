class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in range(32):
            bit_sum=sum((num>>i)&1 for num in nums)
            res|=(bit_sum%3)<<i
        if res>=2**31:
            res-=2**32
        return res