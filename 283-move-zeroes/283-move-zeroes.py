class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = None
        for i in range(len(nums)):
            if nums[i] != 0:
                if k is not None:
                    nums[i],nums[k] = nums[k],nums[i]
                    k += 1
            else:
                if k is None:
                    k = i