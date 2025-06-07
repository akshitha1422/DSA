class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val=max(candies)
        after=[]
        ans=[]
        for i in range(len(candies)):
            new=candies[i]+extraCandies
            after.append(new)
        for i in range(len(after)):
            if after[i]>=max_val:
                ans.append(True)
            else:
                ans.append(False)
        return ans