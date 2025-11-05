class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st=defaultdict(list)
        for s in strs:
            res=tuple(sorted(s))
            st[res].append(s)
        return list(st.values())