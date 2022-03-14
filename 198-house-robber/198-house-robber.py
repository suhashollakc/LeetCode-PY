class Solution:
    def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0, 0
        
#         # [rob1,rob2,n,n+1,....]
#         for n in nums:
#             temp = max(n + rob1,rob2)
#             rob1 = rob2
#             rob2 = temp
            
#         return rob2

# DP Solutions
        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return max(nums)
        
        n = len(nums)
        dp = [0]*n
        dp[0] =  nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]