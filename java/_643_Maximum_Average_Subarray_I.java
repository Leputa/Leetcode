

public class _643_Maximum_Average_Subarray_I {
	public double findMaxAverage(int[] nums, int k) {
		int len=nums.length;
		int tmp=0;
		for (int i=0;i<k;i++) 
			tmp+=nums[i];
		int max=tmp;
		for(int i=k;i<len;i++) {
			tmp=tmp-nums[i-k]+nums[i];
			if(tmp>max)
				max=tmp;
		}
		return (double)max/(double)k;
    }

}
