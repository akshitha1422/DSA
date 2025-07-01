class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0],x[1]))
        st=[]
        for pep in people:
            st.insert(pep[1],pep)
        return st