# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        :type root: TreeNode
        :rType: List[str]
        """
        
        def construct_paths(root, path):
            if root:
                path = path + str(root.val)
                if not root.left and not root.right: # if reach a left
                    paths.append(path) #update paths
                else:
                    path += '->' #extend the current path
                    construct_paths(root.left,path)
                    construct_paths(root.right,path)
        paths = []
        construct_paths(root,'')
        return paths
    
    