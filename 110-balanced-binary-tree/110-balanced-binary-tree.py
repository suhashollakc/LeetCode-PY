# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def tree_height(tree):
        if tree is None:
            return 0
        left_height = tree_height(tree.left)
        right_height = tree_height(tree.right)
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height,right_height) + 1
    
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return tree_height(root) != -1
        
        