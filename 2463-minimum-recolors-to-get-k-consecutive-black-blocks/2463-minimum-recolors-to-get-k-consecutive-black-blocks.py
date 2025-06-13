class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i=0
        min_val=float('inf')
        for j in range(k,len(blocks)+1):
            window=blocks[i:j]
            whites=window.count('W')
            blacks=window.count('B')
            min_val=min(min_val,whites)
            i+=1
        if min_val==float('inf'):
            return 0
        return min_val