class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        if m==0:
        	return 0
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]
        for i in range(m):
        	for j in range(n):
        		if i==0 and j==0:
        			dp[i][j]=grid[0][0]
        		elif i==0:
        			dp[i][j]=grid[i][j]+dp[i][j-1]
        		elif j==0:
        			dp[i][j]=grid[i][j]+dp[i-1][j]
        		else:
        			dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]


print(Solution().minPathSum([[1,3,1],[1,5,1]]))