class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        区间dp
        dp[i][j]: [piles[i],...piles[j]]区间内Alex最多可以多赢的分数
        dp[i][i+j] = max(piles[i] - dp[i+1][i+j], piles[i+j] - dp[i][i+j-1])
        """
        dp = [[0] * len(piles) for _ in range(len(piles))]
        for i in range(len(piles)):
            dp[i][i] = piles[i]
        for j in range(1, len(piles)):
            for i in range(len(piles)-j):
                dp[i][i+j] = max(piles[i] - dp[i+1][i+j], piles[i+j] - dp[i][i+j-1])
        if dp[0][len(piles)-1] > 0:
            return True
        else:
            return False