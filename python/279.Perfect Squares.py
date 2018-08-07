import math

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            s = int(math.sqrt(i))
            while (s > 1):
                dp[i] = min(dp[i - s**2] + 1, dp[i])
                s -= 1
        return dp[n]

if __name__ == '__main__':
    print(Solution().numSquares(3081))