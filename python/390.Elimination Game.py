class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
       	return self.leftToRight(n)

    def leftToRight(self,n):
    	if n==1:
    		return 1
    	if n==2:
    		return 2
    	return 2*self.rightToleft(n//2)

    def rightToleft(self,n):
    	if n==1 or n==2:
    		return 1
    	if n%2==1:      #奇数
    		return 2*self.leftToRight(n//2)
    	else:           #偶数
    		return 2*self.leftToRight((n+1)//2)-1