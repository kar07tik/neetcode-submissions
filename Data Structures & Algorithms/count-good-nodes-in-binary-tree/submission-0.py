# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # A node is good if its value is >= the maximum value along its path from root
            res = 1 if node.val >= max_val else 0
            
            # Update max_val for child calls
            max_val = max(max_val, node.val)
            
            # Recurse on left and right children
            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)
            
            return res

        return dfs(root, root.val)