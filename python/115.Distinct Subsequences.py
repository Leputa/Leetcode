class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if len(s) < len(t):
            return 0

        # dp[i][j]表示从s[0, i]变化到t[0, j]的方法
        dp = [(len(t)+1) * [0] for i in range(len(s)+1)]

        for i in range(len(s)):
            dp[i][0] = 1           #变为空串的方法为1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]

if __name__ == '__main__':
    print(Solution().numDistinct("babgbag", "bag"))