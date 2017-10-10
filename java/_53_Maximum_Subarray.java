
public class _53_Maximum_Subarray {
	public int maxSubArray(int[] nums) {
		if(nums==null)
			return 0;
		int max=Integer.MIN_VALUE;
		int sum=0;
		for (int i=0;i<nums.length;i++) {
			sum+=nums[i];
			if(sum>max)
				max=sum;
			if(sum<0)
				sum=0;
		}
		return max;
    }

}
