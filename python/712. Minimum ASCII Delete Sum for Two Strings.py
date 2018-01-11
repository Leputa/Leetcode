class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1=len(s1)+1
        len2=len(s2)+1
        dp=[([0]*len1) for i in range(len2)]
        for j in range(1,len1):
        	dp[0][j]=dp[0][j-1]+ord(s1[j-1])
        for i in range(1,len2):
        	dp[i][0]=dp[i-1][0]+ord(s2[i-1])

        for i in range(1,len2):
        	for j in range(1,len1):
        		if(s2[i-1]==s1[j-1]):
        			dp[i][j]=dp[i-1][j-1]
        		else:
        			dp[i][j]=min(dp[i-1][j]+ord(s2[i-1]),dp[i][j-1]+ord(s1[j-1]))
        return dp[len2-1][len1-1]





print(Solution().minimumDeleteSum("delete","leet"))