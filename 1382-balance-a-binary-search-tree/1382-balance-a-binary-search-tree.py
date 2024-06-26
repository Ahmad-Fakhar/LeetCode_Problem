class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inOrderTraversal(node):
            if not node:
                return []
            return inOrderTraversal(node.left) + [node.val] + inOrderTraversal(node.right)
        
        def sortedArrayToBST(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])
            return root
        
        # Perform in-order traversal to get nodes in sorted order
        sorted_nodes = inOrderTraversal(root)
        # Construct a balanced BST from the sorted nodes
        return sortedArrayToBST(sorted_nodes)
