#https://leetcode.com/problems/subtree-of-another-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIdentical(self, node, subNode):
        if node is None and subNode is None:
            return True
        if node is None or subNode is None:
            return False
        if node.val != subNode.val:
            return False
        return self.isIdentical(node.left, subNode.left) and self.isIdentical(node.right, subNode.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None:
            return False
        if self.isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

