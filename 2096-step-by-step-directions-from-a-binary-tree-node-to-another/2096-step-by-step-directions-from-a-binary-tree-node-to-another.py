# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        queue = deque([(root, None)])
        parents = {root: None}
        start_node = None
        dest_node = None

        while queue:
            node, parent = queue.popleft()
            if node:
                parents[node] = parent
                if node.val == startValue:
                    start_node = node
                if node.val == destValue:
                    dest_node = node
                queue.append((node.left, node))
                queue.append((node.right, node))
        
        # Step 2: Find the path from the start node to the root
        start_to_root = []
        current = start_node
        while current:
            parent = parents[current]
            if parent:
                if parent.left == current:
                    start_to_root.append('L')
                elif parent.right == current:
                    start_to_root.append('R')
            current = parent
        start_to_root.reverse()
        
        # Step 3: Find the path from the destination node to the root
        dest_to_root = []
        current = dest_node
        while current:
            parent = parents[current]
            if parent:
                if parent.left == current:
                    dest_to_root.append('L')
                elif parent.right == current:
                    dest_to_root.append('R')
            current = parent
        dest_to_root.reverse()
        
        # Step 4: Find the common ancestor and construct the path
        i = 0
        while i < len(start_to_root) and i < len(dest_to_root) and start_to_root[i] == dest_to_root[i]:
            i += 1

        up_moves = len(start_to_root) - i
        down_moves = ''.join(dest_to_root[i:])

        return 'U' * up_moves + down_moves