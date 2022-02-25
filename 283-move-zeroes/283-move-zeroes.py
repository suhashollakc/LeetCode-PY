class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        slow = 0
        for fast in range(len(nums)):
            if nums[fast]!= 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        
        
        
        
        
        
        # **********************
        # k = None
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         if k is not None:
        #             nums[i],nums[k] = nums[k],nums[i]
        #             k += 1
        #     else:
        #         if k is None:
        #             k = i