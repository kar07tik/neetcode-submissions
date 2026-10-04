# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            # Compute maximum sum obtainable from left and right subtrees
            # Ignore negative sums by taking max with 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)

            # Update the global maximum path sum (including current node as peak)
            res[0] = max(res[0], node.val + left_max + right_max)

            # Return the maximum contribution this node can make to its parent path
            return node.val + max(left_max, right_max)

        dfs(root)
        return res[0]