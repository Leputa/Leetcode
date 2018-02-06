class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m=len(board)
        n=len(board[0])
        ans=0
        if m==0 or n==0:
        	return ans
        for i in range(m):
        	for j in range(n):
        		if board[i][j]=='.' or (i>0 and board[i-1][j]=='X') or (j>0 and board[i][j-1]=='X'):
        			continue
       			else:
       				ans+=1
       	return ans