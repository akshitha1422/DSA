class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        s=''
        st=[]
        for i in range(len(words)):
            if (len(s)+len(words[i]))<=maxWidth:
                s+=words[i]+' '
            else:
                s=s.strip()
                st.append(s)
                s=words[i]+' '
        s=s.strip()
        st.append(s)

        for i in range(len(st)):
            if len(st[i])<maxWidth:
                n=st[i].split()
                if i==len(st)-1 or len(n)==1:
                    st[i]=' '.join(n).ljust(maxWidth)
                else:
                    chars=sum(len(word) for word in n)
                    spaces=maxWidth-chars
                    gaps=len(n)-1
                    if gaps>0:
                        spaces_per_gap=spaces//gaps
                        extra=spaces%gaps
                        result=[]
                        for j in range(len(n)-1):
                            result.append(n[j])
                            result.append(' '*spaces_per_gap)
                            if j<extra:
                                result.append(' ')
                        result.append(n[-1])
                        st[i]=''.join(result)
        return st