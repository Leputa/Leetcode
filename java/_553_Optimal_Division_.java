

public class _553_Optimal_Division_ {
	public String optimalDivision(int[] nums) {
		if(nums.length==1)
			return Integer.toString(nums[0]);
		if(nums.length==2)
			return Integer.toString(nums[0])+"/"+Integer.toString(nums[1]);
		String ans=Integer.toString(nums[0])+"/"+"(";
		
		for (int i=1;i<nums.length-1;i++) {
			ans+=Integer.toString(nums[i])+"/";
			
		}
		
		ans+=Integer.toString(nums[nums.length-1])+")";
		
		return ans;
    }
}
