# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if right < left:
                return None
            p = (left+right) // 2
            node = TreeNode(nums[p])
            node.left = helper(left, p-1)
            node.right = helper(p+1, right)
            return node
        return helper(0, len(nums)-1)