class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)

        for i in range(n//2):
        	j=n-1-i
        	for k in range(n):
        		tmp=matrix[i][k]
        		matrix[i][k]=matrix[j][k]
        		matrix[j][k]=tmp
       	
       	for i in range(n):
       		for j in range(i+1,n):
       			tmp=matrix[i][j]
       			matrix[i][j]=matrix[j][i]
       			matrix[j][i]=tmp

       	#return matrix


print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))