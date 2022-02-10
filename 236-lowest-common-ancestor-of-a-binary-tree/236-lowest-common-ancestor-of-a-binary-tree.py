# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        
        #Case 2
        if root == p or root == q:
            return root
        
        left = Solution.lowestCommonAncestor(self,root.left,p,q)
        right = Solution.lowestCommonAncestor(self,root.right,p,q)
        
        #Case 1
        if left and right:
            return root
        
        
        # At this point , left and right cant be both non null since we checked above 
        # case 4 and 5, report target node or LCA back to parent
        
        if left:
            return left
        if right:
            return right
        
        
        # Case 4
        return None