class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (matrix==None):
        	return False
        if (len(matrix)==0 or len(matrix[0])==0):
        	return False
        m=len(matrix)
        n=len(matrix[0])
        row=0
        col=n-1
        while(row<m and col>=0):
        	if matrix[row][col]==target:
        		return True
        	elif matrix[row][col]>target:
        		col-=1
        	else:
        		row+=1
        return False



