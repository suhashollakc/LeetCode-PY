from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []
        queue = deque([root]) #Atleast one element to start bfs
        left_to_right = True
        while len(queue) > 0: #as long as there are elements in the queue
            n = len(queue) # no of nodes in current level 
            new_level = []
            
            for _ in range(n): #deque each node in the current level
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left,node.right]: #enqueue non-null children
                    if child is not None:
                        queue.append(child)
            if not left_to_right:
                new_level.reverse() #reverse current level
            res.append(new_level)
            left_to_right = not left_to_right #flip flag
        return res