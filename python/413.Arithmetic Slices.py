class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt=0
        length=len(A)
        if length<3:
        	return 0
        for i in range(length):
        	for j in range(i+3,length+1):
        		if self.isArithmeticSlices(A[i:j]):
        			cnt+=1
        		else:
        			break
        return cnt

    def isArithmeticSlices(self, A):
    	if len(A)<3:
    		return False
    	dis=A[1]-A[0]
    	for i in range(1,len(A)-1):
    		if A[i+1]-A[i]!=dis:
    			return False
    	return True

print(Solution().numberOfArithmeticSlices([1,2,3,4]))