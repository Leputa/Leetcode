class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
        	return True
        bits=[]
        while n!=0:
        	bits.append(n%2)
        	n=n//2
        if(len(bits)==1):
        	return True
        for i in range(len(bits)-1):
        	if bits[i]==bits[i+1]:
        		return False
        return True