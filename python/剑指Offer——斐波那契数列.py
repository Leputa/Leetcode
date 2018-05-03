# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n==1:
            return 1
        F = [0]*(n+1)
        F[1] = 1

        for i in range(2,n+1):
            F[i] = F[i-1]+F[i-2]

        return F[n]


print(Solution().Fibonacci(3))