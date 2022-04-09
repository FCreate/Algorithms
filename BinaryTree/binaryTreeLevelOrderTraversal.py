# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#without indicator
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            levelSize = len(q)
            level = []
            for i in range(levelSize):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = Queue()
        depth = 0
        q.put((root, depth))
        res = []

        while not q.empty():
            node, depth = q.get()
            if node:
                if len(res) == depth:
                    res.append([])
                res[-1].append(node.val)
                q.put((node.left, depth + 1))
                q.put((node.right, depth + 1))
        return res

