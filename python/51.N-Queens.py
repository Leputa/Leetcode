class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        S = [0] * (n+1)        # 行安全
        U = [0] * (2*n + 1)    # 记录col + row，即向上的对角线是否安全；从左下到右上:1、2...2*n
        D = [0] * (2*n + 1)    # 记录col - row + (n+1), 即向下的对角是否安全；从左下到右上：2*n、2*n-1...3、2、1
        q = [0] * (n+1)
        Q = []
        self.findPosition(q, 1, n, S, U, D, Q)
        return Q

    def findPosition(self, q, col, n, S, U, D, Q):
        if col == n + 1:
            tmpQ = []
            for j in range(1, n+1):
                tmpStr =    '.'*(q[j]-1) + 'Q' + '.'*(n-q[j])
                tmpQ.append(tmpStr)
            Q.append(tmpQ)
            return
            
        for row in range(1, n+1):
            if (S[row] == 0 and U[col+row] == 0 and D[col - row + (n + 1)] == 0):
                q[col] = row
                S[row] = 1
                U[col + row] = 1
                D[col - row + (n + 1)] = 1
                cnt = self.findPosition(q, col+1, n, S, U, D, Q)
                S[row] = 0
                U[col + row] = 0
                D[col - row + (n + 1)] = 0
        return 

if __name__ == '__main__':
    print(Solution().solveNQueens(4))
