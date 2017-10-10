
public class _268_Missing_Number {
	public int missingNumber(int[] nums) {
        int max=0;
        int sum=0;
        for (int i:nums) {
        	if (i>max)
        		max=i;
        	sum+=i;
        }
        return (nums.length+1)*nums.length/2-sum;
    }
}
