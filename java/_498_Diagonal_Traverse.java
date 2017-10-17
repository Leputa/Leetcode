
public class _498_Diagonal_Traverse {
	public int[] findDiagonalOrder(int[][] matrix) {
        int M=matrix.length;
        if(M==0)
        	return new int[M];
        int N=matrix[0].length;
        int[]ans=new int[M*N];
        
        int count=0;
        int i=0,j=0;
        int tag=0;
        System.out.println(M+"  "+N);
        while(count<M*N) {
        	ans[count]=matrix[i][j];
        	System.out.println(i+"   "+j);
        	if(tag==0) { //срио
        		if(i>0&&j+1<N) {
        			--i;
        			++j;
        		}
        		else if(i==0&&j+1<N) {
        			++j;
        			tag=1;
        		}
        		else if(i>0&&j+1==N) {
        			++i;
        			tag=1;
        		}
        		else if(i==0&&j+1==N) {
        			++i;
        			tag=1;
        		}
        	}
        	else if(tag==1) {  //вСоб
        		if(i+1<M&&j>0) {
        			++i;
        			--j;
        		}
        		else if(j==0&&i+1<M){
        			++i;
        			tag=0;
        		}
        		else if(i+1==M&&j>0) {
        			++j;
        			tag=0;
        		}
        		else if(i+1==M&&j==0) {
        			++j;
        			tag=0;
        		}
        	}
        	++count;
        }
        return ans;
    }
}
