class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sumOfNums=sum(nums)
        if sumOfNums%2==1:
        	return False
        sumOfNums=sumOfNums//2

        n=len(nums)
        dp=[[0]*(sumOfNums+1) for i in range(n)]

        for i in range(n):
        	dp[i][0]=0
        for j in range(sumOfNums+1):
        	dp[0][j]=0

        for i in range(1,n):
        	for j in range(nums[i],sumOfNums+1):
        		dp[i][j]=max(dp[i-1][j],dp[i-1][j-nums[i]]+nums[i])

       	if (dp[n-1][sumOfNums]==sumOfNums):
       		return True
       	else:
       		return False
         


print(Solution().canPartition([5,1,2,2,2,12]))