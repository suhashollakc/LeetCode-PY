from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        for _ in range(len(nums) - k):
            heappop(nums)
        
        return nums[0]
            