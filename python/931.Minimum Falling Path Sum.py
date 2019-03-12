class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        width = len(A[0])
        if width == 1:
            return sum([sum(a) for a in A])

        dp = [[0] * width for i in range(len(A))]
        
        for j in range(width):
            dp[0][j] = A[0][j]
        
        for i in range(1, len(A)):
            for j in range(width):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j] + A[i][j], dp[i-1][j+1] + A[i][j])
                elif j == width - 1:
                    dp[i][j] = min(dp[i-1][j] + A[i][j], dp[i-1][j-1] + A[i][j])
                else:
                    dp[i][j] = min(dp[i-1][j-1] + A[i][j], dp[i-1][j] + A[i][j], dp[i-1][j+1] + A[i][j])
        ret = float("inf")
        for j in range(width):
            if dp[len(A)-1][j] < ret:
                ret = dp[len(A)-1][j]
        return ret    



