# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(first, second):
            if not first and not second:
                return True
            if not first or not second:
                return False
            if first.val != second.val:
                return False
            left = same(first.left, second.left)
            if not left:
                return False
            right = same(first.right, second.right)
            if not right:
                return False
            return True
        
        return same(p,q)