from typing import List

class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        dp = [[[0] * K for j in range(len(A))] for i in range(len(A))]
        
        for i in range(len(A)):
            for j in range(i, len(A)):
                dp[i][j][0] = sum(A[i:j+1])/(j-i+1)

        for k in range(1, K):
            for i in range(len(A)):
                for j in range(i+k-1, len(A)):
                    for s in range(i, j):
                        dp[i][j][k] = max(dp[i][j][k], dp[i][s][k-1] + sum(A[s+1:j+1])/(j-s))


        return dp[0][len(A)-1][K-1]


if __name__ == "__main__":
    print(Solution().largestSumOfAverages(A=[1], K=1))
