class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        length=len(temperatures)
        stack=[]
        ans=[0]*length
        for i in range(length):
        	while(len(stack)!=0 and temperatures[i]>temperatures[stack[-1]]):
        		idx=stack.pop()
        		ans[idx]=i-idx
        	stack.append(i)
        return ans











print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))