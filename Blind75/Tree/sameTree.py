#https://leetcode.com/problems/same-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, node, nums):
        if node is None:
            nums.append(None)
        else:
            nums.append(node.val)
            self.preOrder(node.left, nums)
            self.preOrder(node.right, nums)
        return nums

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p = self.preOrder(p, [])
        q = self.preOrder(q, [])

        if p == q:
            return True
        return False