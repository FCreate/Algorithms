#TODO fixme
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

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = self.searchBST(root, key)
        if node is None:
            return root
        else:
            if node.left is None and node.right is None:
                node = None

            elif node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                node = node.right

            return root
