# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        F = [1]*(number+1)
        F[2] = 2

        for i in range(3,number+1):
            F[i] = F[i-1] + F[i-2]

        return F[number]


