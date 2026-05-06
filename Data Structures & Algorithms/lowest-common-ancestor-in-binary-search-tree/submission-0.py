# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def contains(node, target):
            if not node:
                return False
            if node.val == target.val:
                return True
            return contains(node.left, target) or contains(node.right, target)

        res = root
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if contains(node,p) and contains(node,q):
                res = node
            
        return res