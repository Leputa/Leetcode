class Solution:
	#试了一下，这道题的应该意思是只有p包含正则语言，s只是普通字符串
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s==None or p==None:
        	return False
        dp=[[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0]=True

        for j in range(1,len(p)+1):
        	if p[j-1]=='*':
        		if (dp[0][j-1]==True) or (j>1 and dp[0][j-2]==True):  #dp[0][1]在p[0]=='*'时没有意义，填为True
        			dp[0][j]=True                                     #dp[0][j-2]==True,此时'*'取乘0

        for i in range(1,len(s)+1):
        	for j in range(1,len(p)+1):
        		if s[i-1]==p[j-1] or p[j-1]=='.':
        			dp[i][j]=dp[i-1][j-1]
        		if p[j-1]=='*':
        			if p[j-2]!=s[i-1] and p[j-2]!='.':
        				dp[i][j]=dp[i][j-2]
        			else:
        				dp[i][j]=dp[i][j-1] or dp[i][j-2] or dp[i-1][j]
        				#dp[i][j-1]  '*'取乘1
        				#dp[i][j-2]  '*'取乘0 
        				#dp[i-1][j]  s[i-1]和p[j]若能匹配，记此时'*'为乘t;则只要'*'取乘(t+1),s[i]和p[j]一定能匹配
        return dp[len(s)][len(p)]


