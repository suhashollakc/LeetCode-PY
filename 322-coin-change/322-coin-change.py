from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #DP problem
        # dp[i] = min(1+dp[i-coin]) for coin in coins
        # 1+ because we are picking one coin and dp[i-coin] means we have to make up the remaining value
        
        if amount == 0: return 0
        dp = [inf] *(amount+1)
        dp[0] = 0
        
        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i-coin] +1, dp[i])
        
        return dp[-1] if dp[-1] < inf else -1
            