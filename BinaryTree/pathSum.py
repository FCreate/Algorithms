# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target, res):
        if root:
            if root.left is None and root.right is None and root.val == target:
                res.append(True)
            if root.left:
                self.dfs(root.left, target - root.val, res)
            if root.right:
                self.dfs(root.right, target - root.val, res)
        return res

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        return any(self.dfs(root, targetSum, res))
