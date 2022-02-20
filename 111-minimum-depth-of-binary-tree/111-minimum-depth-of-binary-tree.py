from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root]) # at least one element in the queue to kick start bfs
        depth = 0 #we start from 0 because popping root will add 1 depth
        
        while len(queue) > 0: #as long as there is element in the queue
            depth += 1
            
            n = len(queue) # no of nodes in current level
            for _ in range(n): #dequeue each node in the current level
                node = queue.popleft()
                if node.left is None and node.right is None: #found leaf node, return early
                    return depth
                for child in [node.left,node.right]:
                    if child is not None:
                        queue.append(child)
                        
        return depth
                
            
        
        