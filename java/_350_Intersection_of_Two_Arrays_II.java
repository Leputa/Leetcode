import java.util.ArrayList;
import java.util.HashMap;

public class _350_Intersection_of_Two_Arrays_II {
	 public int[] intersect(int[] nums1, int[] nums2) {
	        int len1=nums1.length;
	        int len2=nums2.length;
	        ArrayList<Integer>ans=new ArrayList<>();
	        
	        HashMap<Integer, Integer>map =new HashMap<>();
	        for(int i=0;i<len1;i++) {
	        	map.put(nums1[i], map.getOrDefault(nums1[i], 0)+1);
	        }
	        for (int i=0;i<len2;i++) {
	        	if(map.getOrDefault(nums2[i],0)>0) {
	        		ans.add(nums2[i]);
	        		map.put(nums2[i], map.get(nums2[i])-1);
	        	}
	        }
	        int []res=new int[ans.size()];
	        
	        for (int i=0;i<res.length;i++)
	        	res[i]=ans.get(i);
	        return res;
	    }
}
