class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ans=[]
        if(input==None or len(input)==0):
        	return ans
        if ('+' not in input and '-' not in input and '*' not in input):
        	ans.append(int(input))
        	return ans
        for i in range(len(input)):
        	tag=input[i]
        	if(tag=='+' or tag=='-' or tag=='*'):
        		leftAns=self.diffWaysToCompute(input[:i])
        		leftRight=self.diffWaysToCompute(input[i+1:])
	        	for i in leftAns:
	        		for j in leftRight:
	        			if tag=="+":
	        				ans.append(i+j)
	        			elif tag=="-":
	        				ans.append(i-j)
	        			else:
	        				ans.append(i*j)
        return ans

print(Solution().diffWaysToCompute("2*3-4*5"))