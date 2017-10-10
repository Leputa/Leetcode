class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        sum=0
        i=1
        while i<=n+1:
        	sum+=i
        	if(sum>n):
        		break
        	if(sum==n):
        		cnt+=1
        		break
        	i+=1
        	cnt+=1
        return cnt

print(Solution().arrangeCoins(1804289383))
