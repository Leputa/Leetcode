class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        S = [0] * (n+1)        # 行安全
        U = [0] * (2*n + 1)    # 记录col + row，即向上的对角线是否安全；从左下到右上:1、2...2*n
        D = [0] * (2*n + 1)    # 记录col - row + (n+1), 即向下的对角是否安全；从左下到右上：2*n、2*n-1...3、2、1
        cnt = 0
        return self.findPosition(cnt, 1, n, S, U, D)

    def findPosition(self, cnt, col, n, S, U, D):
        if col == n + 1:
            cnt += 1
            return cnt
        for row in range(1, n+1):
            if (S[row] == 0 and U[col+row] == 0 and D[col - row + (n + 1)] == 0):
                S[row] = 1
                U[col + row] = 1
                D[col - row + (n + 1)] = 1
                cnt = self.findPosition(cnt, col+1, n, S, U, D)
                S[row] = 0
                U[col + row] = 0
                D[col - row + (n + 1)] = 0
        return cnt


if __name__ == '__main__':
    print(Solution().totalNQueens(4))



 

        