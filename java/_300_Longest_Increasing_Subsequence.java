
public class _300_Longest_Increasing_Subsequence {
    public int lengthOfLIS(int[] nums) {
        int length=nums.length;
        if (length==0)
        	return 0;
        int dp[]=new int[length];
        
        for (int i=0;i<length;i++)
        	dp[i]=1;
        
        for (int i=1;i<length;i++) {
        	int j=i-1;
        	int max=Integer.MIN_VALUE;
        	int tag=-1;
        	while(j>=0) {
        		if (nums[j]<nums[i]) {
        			if (dp[j]>max) {
        				max=dp[j];
        				tag=j;
        			}
        		}
        		--j;
        	}
        	if(tag!=-1)
        		dp[i]+=max;
        }
        
        int max=Integer.MIN_VALUE;
        for (int i:dp) 
        	if (i>max)
        		max=i;
        return max;	
    }
}
