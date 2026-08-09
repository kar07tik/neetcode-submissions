# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # If both p and q are greater than curr, LCA must be in the right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are smaller than curr, LCA must be in the left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                # We found the split point or one of the nodes equals curr.val
                return curr