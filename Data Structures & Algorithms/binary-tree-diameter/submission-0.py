# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # base case: empty node has depth 0
            
            left = depth(node.left)   # depth of left subtree
            right = depth(node.right) # depth of right subtree
            
            # diameter through this node = left depth + right depth
            self.max_diameter = max(self.max_diameter, left + right)
            
            # return depth of tree rooted at this node
            return 1 + max(left, right)
        
        depth(root)
        return self.max_diameter
