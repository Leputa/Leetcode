class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points=[0]*10001
        for num in nums:
        	points[num]+=num
        return self.rob(points)
    def rob(self,points):
    	dp=[0]*len(points)
    	dp[1]=points[1]
    	for i in range(2,len(points)):
    		dp[i]=max(dp[i-2]+points[i],dp[i-1])
    	return dp[len(points)-1]

print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))