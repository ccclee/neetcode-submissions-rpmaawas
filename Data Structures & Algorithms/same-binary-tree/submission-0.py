# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(l,r):
            if not l and not r:
                return 0
            if not l or not r:
                return -1
            if same(l.left, r.left) ==-1:
                return -1
            if same(l.right, r.right) ==-1:
                return -1
            
            if l.val == r.val:
                return 0
            else:
                 return -1
        return same(p,q)!=-1
        


        