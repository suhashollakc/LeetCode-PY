class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Boundary Index Binary Search
        left, right = 0,len(arr) - 1
        peak = -1
        
        while left <= right:
            mid = (left+right)//2
            if mid == len(arr)-1 or arr[mid] > arr[mid+1]:
                peak = mid
                right = mid - 1
            else:
                left = mid + 1
        return peak