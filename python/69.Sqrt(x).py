class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
        	return None
        i=0
        j=x
        while i<=j:
        	mid=(i+j)//2
        	if(mid*mid==x):
        		return mid
        	elif(mid*mid<x):
        		i=mid+1
        	else:
        		j=mid-1
        return i

