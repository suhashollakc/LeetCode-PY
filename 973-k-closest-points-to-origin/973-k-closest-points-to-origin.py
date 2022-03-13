import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # I will create a heap to store list of points distance from origin
        heap = []
        
        # I want to loop over the points and push distance and point
        for pt in points:
            heapq.heappush(heap,(math.sqrt(pt[0]**2 + pt[1]**2),pt))
        
        res = []
        for _ in range(k):
            _,pt = heapq.heappop(heap)
            res.append(pt)
        return res