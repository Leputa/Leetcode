import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;

public class _347_Top_K_Frequent_Elements {
	 public List<Integer> topKFrequent(int[] nums, int k) {
		 if (nums.length==0)
			 return null;
	     HashMap<Integer, Integer>map=new HashMap<>();
	     for (int i=0;i<nums.length;i++) {
	    	 map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
	     }
	     
	     List<Map.Entry<Integer,Integer>>list=new ArrayList<>(map.entrySet());
	     Collections.sort(list,new Comparator<Map.Entry<Integer,Integer>>() {

			@Override
			public int compare(Map.Entry<Integer, Integer> arg0, Map.Entry<Integer, Integer> arg1) {
				// TODO Auto-generated method stub
				return arg1.getValue()-arg0.getValue();
			}
	     });
	     
	     List<Integer>ans=new ArrayList<>();
	     for (Map.Entry<Integer,Integer>entry:list) {
	    	 if(k>0) {
	    		 ans.add(entry.getKey());
	    		 k--;
	    	 }
	    	 else
	    		 break;
	     }
	     return ans;
	 }
}
