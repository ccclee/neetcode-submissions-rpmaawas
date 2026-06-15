# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        overallmax = float("-inf")

        def locaMaxPath(node):

            if not node:
                return 0

            left = locaMaxPath(node.left)
            right = locaMaxPath(node.right)
            currmax = max(node.val, node.val+ right , node.val+ left)

            nonlocal overallmax
            overallmax = max(overallmax, currmax, node.val+ right+ left)
            return currmax

        locaMaxPath(root)
        return overallmax
        