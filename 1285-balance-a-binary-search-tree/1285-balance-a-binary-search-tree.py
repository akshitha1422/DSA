# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.st=[]
        def helper(node):
            if node:
                helper(node.left)
                self.st.append(node.val)
                helper(node.right)

        def combine(arr):
            if not arr:
                return None
            if len(arr)==1:
                return TreeNode(arr[0])
            mid=len(arr)//2

            left=arr[:mid]
            now=arr[mid]
            right=arr[mid+1:]

            root=TreeNode(now)

            root.left=combine(left)
            root.right=combine(right)

            return root
        helper(root)
        return combine(self.st)