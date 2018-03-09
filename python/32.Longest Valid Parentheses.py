class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength=0
        stack=[]

        for i in range(len(s)):
        	if s[i]=='(':
        		stack.append(i)
        	else:
        		if len(stack)==0:
        			stack.append(i)
        		else:
        			if s[stack[len(stack)-1]]=='(':
        				stack.pop()
        			else:
        				stack.append(i)

        if len(stack)==0:
        	return len(s)
        right=len(s)-1
        for i in range(len(stack)-1,-1,-1):
        	maxLength=max(maxLength,right-stack[i])
        	if i==0:
        		maxLength=max(maxLength,stack[i])
        	right=stack[i]-1
        	
        return maxLength


print(Solution().longestValidParentheses("())"))
