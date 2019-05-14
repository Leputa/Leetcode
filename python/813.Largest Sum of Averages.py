from typing import List

# class Solution:
#     def largestSumOfAverages(self, A: List[int], K: int) -> float:
#         dp = [[[0] * K for j in range(len(A))] for i in range(len(A))]
        
#         for i in range(len(A)):
#             for j in range(i, len(A)):
#                 dp[i][j][0] = sum(A[i:j+1])/(j-i+1)

#         for k in range(1, K):
#             for i in range(len(A)):
#                 for j in range(i+k-1, len(A)):
#                     for s in range(i, j):
#                         dp[i][j][k] = max(dp[i][j][k], dp[i][s][k-1] + sum(A[s+1:j+1])/(j-s))


#         return dp[0][len(A)-1][K-1]

# 上述解法超时


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # 前j个数分成k-1组，剩余n-j个数分成一组，
        dp = [[0]*(K+1) for i in range(len(A)+1)]

        cur = 0
        for i in range(1, len(A)+1):
            cur += A[i-1]
            dp[i][1] = cur / i

        for k in range(2, K+1):
            for i in range(1, len(A)+1):
                cur = 0  # 剩余的[j, j+1, ... i]
                for j in range(i, 0, -1):
                    cur += A[j-1]
                    dp[i][k] = max(dp[i][k], dp[j-1][k-1] + cur / (i-j+1))
        return dp[len(A)][K]




if __name__ == "__main__":
    print(Solution().largestSumOfAverages(A=[1,2,3,4,5,6,7], K=4))
