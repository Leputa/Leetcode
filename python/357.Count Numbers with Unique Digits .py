class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
        	return 0
        if n==1:
        	return 10
        dp=[0]*(n+1)
        dp[1]=10
        for i in range(2,n+1):
        	count=9
        	h=9
        	for j in range(i-1):
        		count*=h
        		h-=1
        	dp[i]=dp[i-1]+count
        return dp[n]

print(Solution().countNumbersWithUniqueDigits(5))
