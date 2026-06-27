# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        seenNull = False
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    if seenNull:
                        return False
                    queue.append(node.left)
                else :
                    seenNull = True
                if node.right:
                    if seenNull:
                        return False
                    queue.append(node.right)
                else :
                    seenNull = True
        return True
        