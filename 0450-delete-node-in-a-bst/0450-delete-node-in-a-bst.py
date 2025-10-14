# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_min(node):
            curr=node
            while curr.left:
                curr=curr.left
            return curr
        def del_node(node,key):
            if not node:
                return
            elif node.val<key:
                node.right=del_node(node.right,key)
            elif node.val>key:
                node.left=del_node(node.left,key)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp=find_min(node.right)
                node.val=temp.val
                node.right=del_node(node.right,temp.val)
            return node
        root=del_node(root,key)
        return root
    