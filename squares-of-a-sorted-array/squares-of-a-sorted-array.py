class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            arr.append(abs(num * num))
        
        return sorted(arr)