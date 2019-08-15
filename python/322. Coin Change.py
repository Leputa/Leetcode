from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 or len(coins) == 0:
            return 0

        dp = [[float("inf")] * (amount + 1) for i in range(len(coins))] #dp[m][n]: 使用前m种面额， 表示总额n所需要的最少硬币数目
        
        for i in range(len(coins)):                                     #总面额为0，不需要硬币
            dp[i][0] = 0
        
        for j in range(1, amount + 1):                                  #只使用第0个硬币的情况
            if j >= coins[0]:
                dp[0][j] = min(dp[0][j-coins[0]] + 1, dp[0][j])

        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]

        if dp[-1][-1] == float("inf"):
            return -1
        else:
            return dp[-1][-1]

if __name__ == "__main__":
    print(Solution().coinChange([1, 2, 5], 11))