from typing import List
from collections import Counter

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        ret = 0
        dp = [Counter() for i in A]
        for i in range(1, len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                dp[i][delta] = dp[j][delta] + 1
                ret = max(dp[i][delta], ret)
        return ret + 1


                


        

if __name__ == "__main__":
    print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))

