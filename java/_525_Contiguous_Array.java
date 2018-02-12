import java.util.HashMap;
import java.util.Map;

public class _525_Contiguous_Array {
    public int findMaxLength(int[] nums) {
    	int max=0,sum=0;
    	Map<Integer, Integer>map=new HashMap<>();   //<sum,起始下标>
    	map.put(0,-1);
        for(int i=0;i<nums.length;i++){
        	if (nums[i]==0)
        		nums[i]=-1;
        	sum+=nums[i];
        	if(map.containsKey(sum))
        		max=Math.max(max, i-map.get(sum));
        	else
        		map.put(sum, i);
        }
        return max;
    }
}
