class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={'a','e','i','o','u'}
        n=len(words)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+(1 if words[i][0] in vowels and words[i][-1] in vowels else 0)
        res=[]
        for l,r in queries:
            count=prefix[r+1]-prefix[l]
            res.append(count)
        return res

        #Time limit exceeded
        # vowels={'a','e','i','o','u'}
        # res=[]
        # for r1,r2 in queries:
        #     count=0
        #     for word in words[r1:r2+1]:
        #         if word[0] in vowels and word[-1] in vowels:
        #             count+=1
        #     res.append(count)
        # return res