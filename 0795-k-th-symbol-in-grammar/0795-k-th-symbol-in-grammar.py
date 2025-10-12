class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        parent=self.kthGrammar(n-1,(k+1)//2)
        if k%2==1:
            return parent
        else:
            return 1-parent


        # st=['0']
        # for i in range(n):
        #     arr=st[-1]
        #     row=[]
        #     for j in range(len(arr)):
        #         if arr[j]=='0':
        #             row+='01'
        #         else:
        #             row+='10'
        #         st.append(row)
        # return int(st[n][k-1])