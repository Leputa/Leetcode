# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = [1] * len(A)
        for i in range(len(A)):
            if i != 0 :
                B[i] = B[i-1] * A[i-1]
        
        tmp = 1
        for i in range(len(A)-1, -1, -1):
            B[i] *= tmp
            tmp *= A[i]
        return B
