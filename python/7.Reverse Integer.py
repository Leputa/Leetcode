import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        list=[]
        tag=0
        if x<0:
        	tag=1
        	x=-x
        while x!=0:
        	list.append(x%10)
        	x/=10
        list=list[::-1]

        ans=0
        for i in range(len(list)):
        	ans+=list[i]*math.pow(10,i)
        ans=int(ans)
        if ans > 2147483647 :
            return 0
        if tag==1:
        	ans=-ans
        return ans



