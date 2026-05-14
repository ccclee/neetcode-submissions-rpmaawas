# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def good(node, currmax):
            if not node:
                return 0
            add = int(node.val >= currmax) 
            currmax = max(currmax, node.val)
            return  add + good(node.left, currmax) + good(node.right, currmax)
        
        return good(root, root.val)
