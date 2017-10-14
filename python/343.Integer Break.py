class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==2):
        	return 1
        if(n==3):
        	return 2
        ans=1
        while(n>6):
        	n-=3
        	ans*=3
        if(n==6):
        	return ans*9
        if(n==5):
        	return ans*6
        if(n==4):
        	return ans*4
