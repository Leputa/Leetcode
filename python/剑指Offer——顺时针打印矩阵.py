# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix)
        col = len(matrix[0])
        
        ret = [] 
        self.rotateMatrix(matrix,ret,0,row-1,0,col-1,0,0)
        return ret


    def rotateMatrix(self,matrix,ret,row_up,row_down,col_left,col_right,tag,cnt):
        # tag == 0 :从左往右
        # tag == 1 :从上往下
        # tag == 2 :从右往左
        # tag == 3 :从下往上
        if cnt == len(matrix)*len(matrix[0]):
            return 

        if tag == 0:   
            for j in range(col_left,col_right+1):
                cnt += 1
                ret.append(matrix[row_up][j])
            row_up += 1
            tag = 1
        elif tag == 1:
            for i in range(row_up,row_down+1):
                cnt += 1
                ret.append(matrix[i][col_right])
            col_right -= 1
            tag = 2
        elif tag == 2:
            for j in range(col_right, col_left-1, -1):
                cnt += 1
                ret.append(matrix[row_down][j])
            row_down -= 1
            tag = 3
        elif tag == 3:
            for i in range(row_down, row_up-1, -1):
                cnt += 1
                ret.append(matrix[i][col_left])
            col_left += 1
            tag = 0
        
        self.rotateMatrix(matrix,ret,row_up,row_down,col_left,col_right,tag,cnt)


print(Solution().printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))