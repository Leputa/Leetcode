# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        '''
        i代表剩余人数
        f(1) = 0 
        f(i) = (f(i-1) + m)%i
        '''
        if n == 0 or n == 1:
            return n-1

        # 超过了最大递归深度
        # s = self.LastRemaining_Solution(n-1, m)
        # return (s + m) % n

        s = 0
        for i in range(2, n+1):
            s = (s + m) % i 
        return s







