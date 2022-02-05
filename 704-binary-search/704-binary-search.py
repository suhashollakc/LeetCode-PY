class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            mid_idx = (lo + hi) // 2
            mid = nums[mid_idx]
            if mid > target : hi = mid_idx - 1
            elif mid < target : lo = mid_idx + 1
            else : return mid_idx
        else:
            return -1