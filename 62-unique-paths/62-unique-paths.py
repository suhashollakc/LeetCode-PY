class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for c in range(n):
            dp[0][c] = 1
        for r in range(m):
            dp[r][0] = 1
            
        #dp[r][c] = number of unique paths to reach (r,c)
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c]= dp[r-1][c] +dp[r][c-1]
        
        return dp[-1][-1]