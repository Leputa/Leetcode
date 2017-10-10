class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
        	return False;
        low=0
        high=num
        ans=(high+low)//2
        while(low<high):
        	while ans**2!=num and low<high:
        		#print(str(low)+":"+str(high))
        		if(ans**2<num):
        			low=ans+1
        		else:
        			high=ans-1
        		ans=(high+low)//2
        	if ans**2==num :
        		return True
        return False


Solution().isPerfectSquare(17)

