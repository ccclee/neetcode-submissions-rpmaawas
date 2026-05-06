# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def same(a,b):
            if not a and not b:
                return 1
            if not a or not b:
                return 0
            if same(a.left, b.left)== 0:
                return 0
            if same(a.right, b.right)== 0:
                return 0
            if a.val == b.val:
                return 1
            else:
                return 0
        if not root:
            return False
        if not subRoot:
            return True
        if root.val == subRoot.val:
            if same(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)