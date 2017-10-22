
public class _486_Predict_the_Winner {
    public boolean PredictTheWinner(int[] nums) {
        int len=nums.length;
        int[][]dp=new int[len][len];//dp是一个闭区间
        for(int i=0;i<len;i++)
        	dp[i][i]=nums[i];
        
        for(int i=len-2;i>=0;--i)
        	for(int j=i+1;j<len;++j)
        		dp[i][j]=Integer.max(dp[j][j]-dp[i][j-1], dp[i][i]-dp[i+1][j]);
        		
        if(dp[0][len-1]>=0)
        	return true;
        else
        	return false;
    }
}
