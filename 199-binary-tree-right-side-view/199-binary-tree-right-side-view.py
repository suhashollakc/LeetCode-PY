from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        res = []
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue)
            res.append(queue[0].val) #only append the first node we encounter since it's the rightmost
            
            for _ in range(n):
                node = queue.popleft()
                for child in [node.right,node.left]: #we add right child first so it'll pop out if the queue first
                    
                    if child is not None:
                        queue.append(child)
        return res