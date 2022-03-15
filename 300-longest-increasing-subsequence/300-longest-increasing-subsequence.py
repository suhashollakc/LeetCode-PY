class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Imp -> Dynamic Programming -> Longest and sequence -> solution depends on the solution of a dynamic numebr of sub problems
        n = len(nums)
        dp = [1] *n
        best = 0
        #dp[i] = LIC ending in nums[i]
        
        for i in range(n):
            for j in range(i):
                if nums[j] >= nums[i]: #not increasing, skip
                    continue
                
                dp[i] = max(dp[i],dp[j]+1)
            best = max(best,dp[i])
        
        return best