class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort(key=lambda x:len(x))
        # pre=''
        # word=strs[0]
        # i=0
        # while i<len(word):
        #     pre+=word[i]
        #     for s in strs:
        #         l=len(pre)
        #         if s[:l]!=pre:
        #             return pre[:-1]
        #     i+=1
        # return pre
        strs.sort()
        first=strs[0]
        last=strs[-1]
        i=0
        while i<len(first) and first[i]==last[i]:
            i+=1
        return first[:i]