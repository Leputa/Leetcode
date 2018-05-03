# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here\
        F = [0]*(number+1)
        if number == 1 or number == 2:
            return number
        F[1] = 1
        F[2] = 2
        for i in range(3,number+1):
            F[i] = F[i-1] + F[i-2]
        return F[number]


print(Solution().jumpFloor(4))