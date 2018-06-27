# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        m = []
        for i in range(rows):
            tmpList = []
            for j in range(cols):
                tmpList.append(matrix[i*cols + j])
            m.append(tmpList)

        bool_matrix = [[0]*cols for i in range(rows)]

        for i in range(rows):
            for j in range(cols):
                tag = self.getPath(m, path, i, j, bool_matrix, rows, cols)
                if tag == True:
                    return tag
        return False

    def getPath(self, m, path, i, j, bool_matrix, rows, cols):
        if len(path) == 0:
            return True
        if m[i][j] != path[0]:
            return False
        if bool_matrix[i][j] == 1:
            return False

        bool_matrix[i][j] = 1

        tag = 1
        if i > 0:
            tag = 0
            tag_up = self.getPath(m, path[1:], i-1, j, bool_matrix, rows, cols)
            if tag_up == True:
                return tag_up
        if j > 0 :
            tag = 0
            tag_left = self.getPath(m, path[1:], i, j-1, bool_matrix, rows, cols)
            if tag_left == True:
                return tag_left
        if i < rows - 1:
            tag = 0
            tag_down = self.getPath(m, path[1:], i+1, j, bool_matrix, rows, cols)
            if tag_down == True:
                return tag_down
        if j < cols - 1:
            tag = 0
            tag_right = self.getPath(m, path[1:], i, j+1, bool_matrix, rows, cols)
            if tag_right == True:
                return tag_right

        bool_matrix[i][j] = 0

        if tag == 0:
            return False
        else:
            return True

print(Solution().hasPath("A",1,1,"A"))