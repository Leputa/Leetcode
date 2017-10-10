import java.util.HashMap;

public class _219_Contains_Duplicate_II {
	public boolean containsNearbyDuplicate(int[] nums, int k) {
		if(k==0||k==1)
			return false;
		HashMap<Integer, Integer>map=new HashMap<>();
		int len=nums.length;
		int min=Math.min(len, k+1);
		for(int i=0;i<min;i++) {
			if(map.getOrDefault(nums[i], 0)==0)
				map.put(nums[i], 1);
			else
				return true;
		}
		if(k+1>=len)
			return false;
        for(int i=k+1;i<nums.length;i++) {
        	map.remove(nums[i-k-1]);
        	if(map.getOrDefault(nums[i], 0)==0)
        		map.put(nums[i], 1);
        	else
        		return true;
        }
        return false;
    }
}
