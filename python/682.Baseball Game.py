class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans=[]
        for i in ops:
        	if(i=='D'):
        		ans.append(ans[len(ans)-1]*2)
        	elif(i=='C'):
        		ans.pop()
        	elif(i=='+'):
        		ans.append(ans[len(ans)-1]+ans[len(ans)-2])
        	else:
        		ans.append(int(i))
        sum=0
        for i in ans:
        	sum+=i
        return sum

print(Solution().calPoints(["5","2","C","D","+"]))