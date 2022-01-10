class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = nums[0]
        
        for i in range(1, len(nums)): 
            nums[i] = nums[i] * (nums[i] + nums[i-1])
            m = max(nums[i],m)
        return m 