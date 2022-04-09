# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        node1 = self.searchBST(root.right, val)
        node2 = self.searchBST(root.left, val)
        if node1 or node2:
            return node1 or node2
        else:
            return None                