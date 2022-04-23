def deleteNode(root, key):
    if not root:
        return None
    if key > root.val:
        root.right = deleteNode(root.right, key)
    if key < root.val:
        root.left = deleteNode(root.left, key)
    else:  # когда равны
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        tmp = root
        root = root.right
        while root.left:
            root = root.left
        tmp.val = root.val
        root = None
        return tmp

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  # когда равны
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            tmp = root
            root = root.right
            while root.left:
                root = root.left
            tmp.val = root.val
            root = None
            return tmp




class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:  # когда равны
            if not root.right and not root.left:
                return None
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            root.val = tmp.val
            root.right = self.deleteNode(root.right, root.val)
        return root
        Input


[5, 3, 6, 2, 4, null, 7]
7
Output
[3, 2, 4]
Expected
[5, 3, 6, 2, 4]


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val = temp.val
            root.right = self.deleteNode(root.right, root.val)
        return root


class Solution:
    def helper(self, root, path):
        if root is None:
            return None
        path.append(str(root.val))
        number = "".join(path)
        print(path)
        self.s += int(number)
        print(self.s)
        self.helper(root.left, path)
        self.helper(root.right, path)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.s = 0

        self.helper(root, [])
        return self.s


class Solution:
    def helper(self, root, path):
        if root is None:
            return None
        path.append(str(root.val))
        number = "".join(path)
        print(path)
        if not root.left and not root.right:
            self.s += int(number)
            print(self.s)
        self.helper(root.left, path[:])
        self.helper(root.right, path[:])

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.s = 0

        self.helper(root, [])
        return self.s


int
Solution(const
Node * root) {
    static
int
res = 0;
static
string
s = "";
if (root == nullptr)
return 0;
if (!root->left & & !root->right) {
s += to_string(root->value);
res += stoi(s);
return res;
}
s += to_string(root->value);
string
sbl = s;
if (root->left)
Solution(root->left);
if (root->right) {
s = sbl;
Solution(root->right);
}
return res;
}

def maxPathSum(root):
    res = root.val

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        leftMax = max(0, dfs(root.left))
        rightMax = max(0, dfs(root.right))
        # случай с разветвлением
        res = max(res, leftMax + rightMax + root.val)
        # случай без разветвления
        return max(leftMax, rightMax) + root.val

    dfs(root)
    return res




