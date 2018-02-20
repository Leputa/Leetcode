
public class _59_Spiral_Matrix_II {
    public int[][] generateMatrix(int n) {
    	if (n==0)
    		return new int[0][0];
    	
        int [][]matrix=new int[n][n];
        int num=1;
        
        int left=0;
        int right=n-1;
        int up=0;
        int down=n-1;
        
        while(left <=right && up<=down){
        	for (int j=left;j<=right;j++){
        		matrix[up][j]=num++;
        	}
        	up++;
        	for (int i=up;i<=down;i++){
        		matrix[i][right]=num++;
        	}
        	right--;
        	for (int j=right;j>=left;j--){
        		matrix[down][j]=num++;
        	}
        	down--;
        	for (int i=down;i>=up;i--){
        		matrix[i][left]=num++;
        	}
        	left++;
        }
        
        return matrix;
    }
}
