class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans=[]
        for num in range(left,right+1):
        	tmp=num
        	tag=1
        	while(tmp!=0):
        		div=tmp%10
        		if(div==0):
        			tag=0
        			break
        		tmp=tmp//10
        		if num%div!=0:
        			tag=0
        			break
        	if tag==1:
        		ans.append(num)
        return ans

print(Solution().selfDividingNumbers(1,22))