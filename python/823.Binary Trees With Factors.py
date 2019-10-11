from typing import List

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        kmod = 10**9 + 7
        dp = dict()
        A = sorted(A)
        s = set(A)
        for i, val in enumerate(A):
            dp[val] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in s:
                    dp[val] = (dp[val] + dp[A[j]] * dp[A[i] // A[j]]) % kmod

        return sum(dp.values()) % kmod
            

