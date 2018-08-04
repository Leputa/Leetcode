class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if len(matrix) == 0:
            return ret
        self.rotatematrix(0, 0, 0, len(matrix), len(matrix[0]), matrix, ret, 0)
        return ret

    def rotatematrix(self, tag, row_start, col_start, row_end, col_end, matrix, ret, cnt):

        if cnt == len(matrix) * len(matrix[0]):
            return 
        
        if tag == 0:  #left->right
            for j in range(col_start, col_end):
                ret.append(matrix[row_start][j])
                cnt += 1
            self.rotatematrix(1, row_start+1, col_start, row_end, col_end, matrix, ret, cnt)
        
        elif tag == 1: #up->down
            for i in range(row_start, row_end):
                ret.append(matrix[i][col_end-1])
                cnt += 1
            self.rotatematrix(2, row_start, col_start, row_end, col_end-1, matrix, ret, cnt)

        elif tag == 2: #right->left
            for j in range(col_end-1, col_start-1, -1):
                ret.append(matrix[row_end-1][j])
                cnt += 1
            self.rotatematrix(3, row_start, col_start, row_end-1, col_end, matrix, ret, cnt)

        elif tag == 3: #down->up
            for i in range(row_end-1, row_start-1, -1):
                ret.append(matrix[i][col_start])
                cnt += 1
            self.rotatematrix(0, row_start, col_start+1, row_end, col_end, matrix, ret, cnt)


if __name__ == '__main__':
    solutin = Solution()
    print(solutin.spiralOrder([]))