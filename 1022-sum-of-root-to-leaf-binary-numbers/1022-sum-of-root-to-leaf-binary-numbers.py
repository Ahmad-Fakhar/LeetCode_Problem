# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, x):
            if not node:
                return 0
            x = (x << 1) + node.val
            if not node.left and not node.right:
                return x
            return dfs(node.left, x) + dfs(node.right, x)
        return dfs(root, 0)