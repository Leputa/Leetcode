class Solution:
    def toggling_row(self, A: List[List[int]], i) -> None:
        for j in range(len(A[i])):
            A[i][j] = (A[i][j] + 1) % 2
    
    def toggling_col(self, A: List[List[int]], j) -> None:
        for i in range(len(A)):
            A[i][j] = (A[i][j] + 1) % 2

    def is_col_change(self, A: List[List[int]], j) -> bool:
        zero_cnt = 0
        for i in range(len(A)):
            if A[i][j] == 0:
                zero_cnt += 1
        if zero_cnt/len(A) > 0.5:
            return True
        else:
            return False 

    def matrixScore(self, A: List[List[int]]) -> int:
        for i in range(len(A)):
            for j in range(len(A[i])):
                if self.is_col_change(A, j):
                    self.toggling_col(A, j)
                    row_change_fix = False
                if A[i][0] == 0:
                    self.toggling_row(A, i)

        ret = 0
        length = len(A[0])
        for row in A:
            ret += sum([ row[j] * 2**(length - j - 1) for j in range(len(row))])
        return ret

