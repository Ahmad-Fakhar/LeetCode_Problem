# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
            
            parent = nodes[parent_val]
            child = nodes[child_val]
            
            if is_left:
                parent.left = child
            else:
                parent.right = child
            
            children.add(child_val)
        
        # The root node is the one that is never a child
        root_val = (set(nodes.keys()) - children).pop()
        return nodes[root_val]