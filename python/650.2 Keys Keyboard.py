class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==1):
        	return 0
        if(n==2):
        	return 2

        seive=[0]*(n+1)
        for i in range(2,n+1):
        	seive[i]=1
        d=2
        while(d**2<=n):
        	if(seive[i]==1):
        		tmp=d**2
        		while(tmp<=n):
        			seive[tmp]=0
        			tmp+=d
        	d+=1


        dp=[2147483647]*(n+1)
        dp[2]=2

        for i in range(3,n+1):
        	if(seive[i]==1):
        		dp[i]=i
        		continue
        	for j in range(i-1,1,-1):
        		if(i%j==0):
        			dp[i]=self.getMin(dp[j]+i//j,dp[i])
       	return dp[i]

    def getMin(self,a,b):
    	if(a<=b):
    		return a
    	else:
    		return b

print(Solution().minSteps(156))