class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        result=0
        for i in range(32):
        	count=0
        	mask=1<<i
        	for j in range(length):
        		if (nums[j]&mask):
        			count+=1            #统计在某一位上有多少个1
        	if (count%3==1):
        		result|=mask
       	return self.convert(result)

    def convert(self,x):                #python有点坑....
    	if x>=2**31:
    		x-=2**32
    	return x

print(Solution().singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2]))