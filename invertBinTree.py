# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # at end of branch?
        if( root == None ):
            return root
        
        # swap left and right nodes
        root.left, root.right = root.right, root.left
        
        # recur on left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
