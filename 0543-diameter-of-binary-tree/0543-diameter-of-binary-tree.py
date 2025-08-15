# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia=0
        def dfs(node):
            if not node:
                return 0
            left_ht=dfs(node.left)
            right_ht=dfs(node.right)

            curr=left_ht+right_ht
            self.max_dia=max(self.max_dia,curr)

            return 1+max(left_ht,right_ht)
        dfs(root)
        return self.max_dia