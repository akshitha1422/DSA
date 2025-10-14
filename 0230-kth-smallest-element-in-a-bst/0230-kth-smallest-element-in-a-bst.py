# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st=[]
        def helper(node):
            if not node:
                return
            helper(node.left)
            st.append(node.val)
            helper(node.right)
        helper(root)
        return st[k-1]