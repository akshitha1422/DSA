# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left_ht=dfs(node.left)
            right_ht=dfs(node.right)
            if left_ht==-1 or right_ht==-1:
                return -1
            if abs(left_ht-right_ht)>1:
                return -1
            return 1+max(left_ht,right_ht)
        return dfs(root)!=-1