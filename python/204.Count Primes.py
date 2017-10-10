import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n<=2):
        	return 0
        seive=[]
        for i in range(n):
        	seive.append(True)
        for j in range(2,int(math.ceil(math.sqrt(n)))):
        	if(seive[j]==True):
        		for k in range(j*j,n,j):
        			seive[k]=False
        cnt=0
        for i in range(2,n):
        	if (seive[i]==True):
        		cnt+=1
        return cnt	
