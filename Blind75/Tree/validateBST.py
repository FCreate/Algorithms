#https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder(root, res):
            if root is None:
                return []
            else:
                preorder(root.left, res)
                res.append(root.val)
                preorder(root.right, res)
                return res
        order = preorder(root, [])
        if len(order) == 1:
            return True
        else:
            for i in range(1, len(order)):
                if order[i] - order[i-1] <= 0:
                    return False
            return True