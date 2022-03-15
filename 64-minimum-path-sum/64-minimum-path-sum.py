class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        cur_sum = 0
        for c in range(n):
            cur_sum = cur_sum + grid[0][c]
            dp[0][c] = cur_sum
        
        cur_sum = 0
        for r in range(m):
            cur_sum = cur_sum + grid[r][0]
            dp[r][0] = cur_sum
        
        #dp[r][c] = min path to sum to reach (r,c)
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
                
        return dp[-1][-1]