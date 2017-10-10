class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries)==0:
        	return 0
        if len(timeSeries)==1:
        	return duration
        ans=duration
        pre=timeSeries[0]+duration
        for i in range(1,len(timeSeries)):
        	if (timeSeries[i]>=pre):
        		ans+=duration
        		pre=timeSeries[i]+duration
        	else:
        		ans+=(timeSeries[i]-timeSeries[i-1])
        		pre=timeSeries[i]+duration
        return ans
print(Solution().findPoisonedDuration([1,4], 2))
