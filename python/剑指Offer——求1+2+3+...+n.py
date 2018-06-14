# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n == 1:
            return 1
        return self.Sum_Solution(n-1) + n

print(Solution().Sum_Solution(3))