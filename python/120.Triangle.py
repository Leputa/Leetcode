class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle == None or len(triangle) == 0:
            return 0
        
        dp = [[0]*len(triangle) for i in range(len(triangle))]
        
        dp[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(1,len(triangle)):
            for j in range(1,i):
                dp[i][j] = triangle[i][j] + min(dp[i-1][j],dp[i-1][j-1])

        ret = min(dp[len(triangle)-1])
        return ret

print(Solution().minimumTotal([[2],[3,4],[6,5,7]]))