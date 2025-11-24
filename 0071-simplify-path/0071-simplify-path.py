class Solution:
    def simplifyPath(self, path: str) -> str:
        while path and path[-1]=='/':
            path=path[:-1]
        st=[]
        path=path.split('/')
        for i in path:
            if i=='' or i=='.':
                pass
            elif i=='..':
                if st:
                    st.pop()
            else:
                st.append(i)
        return '/'+'/'.join(st)