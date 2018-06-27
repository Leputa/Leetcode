# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.cnt = 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        m = []
        for i in range(rows):
            tmpList = []
            for j in range(cols):
                tmpList.append(self.getSum(i, j))
            m.append(tmpList)

        m_bool = [[0]*cols for i in range(rows)]
        
        self.getCnt(threshold, rows, cols, m, m_bool, 0, 0)

        return self.cnt

    def getCnt(self, threshold, rows, cols, m, m_bool, i, j):
        if m_bool[i][j] == 1:
            return 
        if m[i][j] > threshold:
            return 

        m_bool[i][j] = 1
        self.cnt += 1
        
        if i > 0:
            self.getCnt(threshold, rows, cols, m, m_bool, i-1, j)
        if j > 0:
            self.getCnt(threshold, rows, cols, m, m_bool, i, j-1)
        if i < rows - 1:
            self.getCnt(threshold, rows, cols, m, m_bool, i+1, j)
        if j < cols - 1:
            self.getCnt(threshold, rows, cols, m, m_bool, i, j+1)


    def getSum(self, i, j):
        sum = 0
        while (i!=0):
            sum += i%10
            i = i//10
        while (j!=0):
            sum += j%10
            j = j//10
        return sum
