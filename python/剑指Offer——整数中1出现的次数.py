# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt = 0
        for i in range(n+1):
        	while i!= 0:
        		tmp = i%10
        		if tmp == 1:
        			cnt += 1
        		i = i//10
        return cnt

print(Solution().NumberOf1Between1AndN_Solution(13))