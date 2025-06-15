class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:
            return []
        w=Counter(words)
        wlen=len(words[0])
        total_len=wlen*len(words)
        st=[]

        for i in range(wlen):
            left=i
            right=i
            seen=Counter()
            count=0

            while right+wlen<=len(s):
                wrd=s[right:right+wlen]
                right+=wlen
                if wrd in w:
                    seen[wrd]+=1
                    count+=1
                    while seen[wrd]>w[wrd]:
                        re=s[left:left+wlen]
                        seen[re]-=1
                        count-=1
                        left+=wlen
                    if count==len(words):
                        st.append(left)
                else:
                    seen.clear()
                    count=0
                    left=right
        return st