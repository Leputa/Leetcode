class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n==1:
        # 	return 1
        # if n==2:
        # 	return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        if n==1:
        	return 1
        if n==2:
         	return 2
        steps=[]
        steps.append(1)
        steps.append(2)

        for i in range(2,n):
        	steps.append(steps[i-1]+steps[i-2])
        return steps[n-1]
        