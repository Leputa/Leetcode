
public class _661_Image_Smoother {
	public int[][] imageSmoother(int[][] M) {
		if(M.length==1&&M[0].length==1)
			return M;
		
		int [][]ans=new int[M.length][M[0].length];
		
		if(M.length==1) {
			for(int j=0;j<M[0].length;j++)
				if(j==0)
					ans[0][j]=(M[0][j]+M[0][j+1])/2;
				else if(j==M[0].length-1)
					ans[0][j]=(M[0][j]+M[0][j-1])/2;
				else
					ans[0][j]=(M[0][j]+M[0][j-1]+M[0][j+1])/3;
			return ans;
		}
		
		if(M[0].length==1) {
			for(int i=0;i<M.length;i++)
				if(i==0)
					ans[i][0]=(M[i][0]+M[i+1][0])/2;
				else if(i==M.length-1)
					ans[i][0]=(M[i][0]+M[i-1][0])/2;
				else
					ans[i][0]=(M[i][0]+M[i+1][0]+M[i-1][0])/3;
			return ans;
		}

		for (int i=0;i<M.length;i++) {
			for(int j=0;j<M[0].length;j++) {
				if(i==0) {
					if(j==0)
						ans[i][j]=(M[i+1][j]+M[i][j+1]+M[i+1][j+1]+M[i][j])/4;
					else if(j==M[0].length-1)
						ans[i][j]=(M[i+1][j]+M[i][j-1]+M[i+1][j-1]+M[i][j])/4;
					else 
						ans[i][j]=(M[i+1][j]+M[i][j-1]+M[i+1][j-1]+M[i][j]+M[i+1][j+1]+M[i][j+1])/6;
				}
				else if(i==M.length-1) {
					if(j==0)
						ans[i][j]=(M[i-1][j]+M[i][j+1]+M[i-1][j+1]+M[i][j])/4;
					else if(j==M[0].length-1)
						ans[i][j]=(M[i-1][j]+M[i][j-1]+M[i-1][j-1]+M[i][j])/4;
					else 
						ans[i][j]=(M[i-1][j]+M[i][j-1]+M[i-1][j-1]+M[i][j]+M[i-1][j+1]+M[i][j+1])/6;
				}
				else if(j==0) {
					ans[i][j]=(M[i][j]+M[i][j+1]+M[i+1][j]+M[i-1][j]+M[i+1][j+1]+M[i-1][j+1])/6;
				}
				else if(j==M[0].length-1) {
					ans[i][j]=(M[i][j]+M[i][j-1]+M[i+1][j]+M[i-1][j]+M[i+1][j-1]+M[i-1][j-1])/6;
				}
				else 
					ans[i][j]=(M[i][j]+M[i+1][j]+M[i-1][j]+M[i][j-1]+M[i][j+1]+M[i+1][j+1]+M[i+1][j-1]+M[i-1][j+1]+M[i-1][j-1])/9;
			}
		}
		return ans; 
    }
}
