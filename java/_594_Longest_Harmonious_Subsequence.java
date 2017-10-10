import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class _594_Longest_Harmonious_Subsequence {
public int findLHS(int[] nums) {
        int max=0;
        if(nums.length==0)
        	return max;
        HashMap<Integer, Integer>map=new HashMap<>();
        for(int i=0;i<nums.length;i++) {
        	map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
        }
        int cnt=0;
        Set<Integer>keys=map.keySet();
		Iterator<Integer>it=keys.iterator();
		while(it.hasNext()) {
			int tmp=it.next();
			if(map.getOrDefault(tmp+1, 0)!=0){
				cnt=map.get(tmp)+map.getOrDefault(tmp+1, 0);
				if(cnt>max)
					max=cnt;
			}
			if(map.getOrDefault(tmp-1, 0)!=0) {
				cnt=map.get(tmp)+map.getOrDefault(tmp-1, 0);
				if(cnt>max)
					max=cnt;
			}
			cnt=0;
		}
		return max;
    }
}
