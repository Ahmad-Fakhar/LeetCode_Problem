# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def inorder(root,Ans):
            if(root == None):
                return Ans
            inorder(root.left,Ans)
            Ans.append(root.val)
            inorder(root.right,Ans)
        if(root == None):
            return []
        liste = []
        inorder(root,liste)
        print(liste)
        suffix= [ liste[-1]]
        for i in range(len(liste)-2,-1,-1):
            suffix.append(suffix[-1] + liste[i])
        suffix.reverse()
        print(suffix)
        def inorder1(root):
            global i
            if(root == None):
                return
            inorder1(root.left)
            root.val = suffix[0]
            suffix.pop(0)
            print(root.val)
            inorder1(root.right)
        inorder1(root)
        return root