class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x=click[0]
        y=click[1]
        if(board[x][y]=='M'):
        	board[x][y]='X'
        	return board
        
        tag=[]
        for i in range(len(board)):
        	tmprow=[]
        	for j in range(len(board[0])):
        		tmprow.append(0)
        	tag.append(tmprow)

        num=self.getAroundMine(board,x,y)
        if (num!=0):
        	board[x][y]=str(num)
        	return board
        else:
        	board[x][y]='B'
        	tag[x][y]=1
        	self.DFS(board,tag,x,y)
        	return board

    def DFS(self,board,tag,x,y):
    	for i in range(-1,2):
    		for j in range(-1,2):
    			nx=x+i
    			ny=y+j
    			if (nx>=0 and ny>=0 and nx<len(board) and ny<len(board[0]) and tag[nx][ny]==0):
    				num=self.getAroundMine(board,nx,ny)
    				if(num!=0):
    					board[nx][ny]=str(num)
    					tag[nx][ny]=1
    				else:
    					board[nx][ny]='B'
    					tag[nx][ny]=1
    					self.DFS(board,tag,nx,ny)

    def getAroundMine(self,board,x,y):
    	num=0
    	for i in range(-1,2):
    		for j in range(-1,2):
    			nx=x+i
    			ny=y+j
    			if(nx>=0 and ny>=0 and nx<len(board) and ny<len(board[0])):
    				if(board[nx][ny]=='M'):
    					num+=1
    	return num





print(Solution().updateBoard([['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'M', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
	,[3,0]))