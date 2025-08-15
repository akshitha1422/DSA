# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        st=[]
        res=[]
        def dfs(node,level):
            if not node:
                return
            if level==len(st):
                st.append([])
            st[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        for i in range(len(st)-1,-1,-1):
            res.append(st[i])
        return res
