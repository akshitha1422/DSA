class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(hbool):
            l,r=0,len(nums)-1
            result=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    result=mid
                    if hbool:
                        r=mid-1
                    else:
                        l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return result
        return [binary_search(True),binary_search(False)]