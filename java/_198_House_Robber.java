
public class _198_House_Robber {
	public int rob(int[] nums) {
		if(nums.length==0)
			return 0;
		int len=nums.length;
		int[] ans=new int[len];
		
		if(len==1)
			return nums[0];
		if(len==2)
			return nums[0]>nums[1]?nums[0]:nums[1];
		
		for (int i=0;i<len;i++) {
			if(i==0)
				ans[0]=nums[i];
			else if (i==1)
				ans[1]=Math.max(ans[0], nums[1]);
			else {
				ans[i]=Math.max(ans[i-1], ans[i-2]+nums[i]);
			}
		}
		
		return ans[len-1]>ans[len-2]?ans[len-1]:ans[len-2];
    }
}
