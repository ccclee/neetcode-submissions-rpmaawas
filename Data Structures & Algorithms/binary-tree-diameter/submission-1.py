# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        currmax = 0

        def dfs(node):
            nonlocal currmax
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            currmax = max(currmax, left+right)

            return max(right, left)+1
        
        dfs(root)

        return currmax
            