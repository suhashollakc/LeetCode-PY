class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = sorted(nums1 + nums2)
        return median(mergedArray)