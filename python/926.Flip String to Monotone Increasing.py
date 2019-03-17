class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        dp = [[0, 0] for i in range(len(S))] #pos_0记录该位置为0的flip数量， pos_1记录该位置1的flip数量
        
        if S[0] == "0":
            dp[0][1] = 1
        else:
            dp[0][0] = 1
        
        for i in range(1, len(S)):
            if S[i] == "0":
                dp[i][0] = dp[i-1][0] 
                dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1
            else:
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])
                dp[i][0] = dp[i-1][0] + 1
                
        return min(dp[len(S)-1][0], dp[len(S)-1][1])





