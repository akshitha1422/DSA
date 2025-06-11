class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        fruit=defaultdict(int)
        left=0
        max_val=0
        for right in range(len(fruits)):
            fruit[fruits[right]]+=1
            while len(fruit)>2:
                fruit[fruits[left]]-=1
                if fruit[fruits[left]]==0:
                    del fruit[fruits[left]]
                left+=1
            max_val=max(max_val,right-left+1)
        return max_val