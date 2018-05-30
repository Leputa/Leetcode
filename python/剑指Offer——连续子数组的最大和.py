# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [0]* (len(array) + 1)

        for i in range(len(array)):
        	dp[i+1] = max(array[i], dp[i] + array[i])

        max_sum = -float('inf')
        for i in range(1, len(dp)):
        	if dp[i] > max_sum:
        		max_sum = dp[i]
        return max_sum

print(Solution().FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))