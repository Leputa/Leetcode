

public class _516_Longest_Palindromic_Subsequence {
	 public int longestPalindromeSubseq(String s) {
	      String p=new StringBuilder(s).reverse() .toString();
	      int length=p.length();
	      int[][]dp=new int[length+1][length+1];
	      for (int i=0;i<length;i++)
	    	  dp[i][0]=0;
	      for (int j=0;j<length;j++)
	    	  dp[0][j]=0;
	      for (int i=1;i<length+1;i++) {
	    	  for (int j=1;j<length+1;j++)
	    		  if(s.charAt(i-1)==p.charAt(j-1))
	    			  dp[i][j]=dp[i-1][j-1]+1;
	    		  else 
	    			  dp[i][j]=Integer.max(dp[i-1][j], dp[i][j-1]);
	      }
	      return dp[length][length];
	 }
}
