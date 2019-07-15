# -*- coding:utf-8 -*-
import numpy as np

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

    def Fibonacci_logN(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        output = np.array([[1, 0], [0, 1]])
        base_vec = np.array([1, 0])
        base_matrix = np.array([[1, 1], [1, 0]])
        n = n-2
        while( n != 0):
            if n & 1 == 1:
                output = np.matmul(output, base_matrix)
            n >>= 1
            base_matrix = np.matmul(base_matrix, base_matrix)
        return np.matmul(output, base_vec)[0]

if __name__ == "__main__":
    a = [i for i in range(100)]
    for i in a:
        assert Solution().Fibonacci(i) == Solution().Fibonacci(i)

    print(Solution().Fibonacci(5))