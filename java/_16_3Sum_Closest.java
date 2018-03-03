import java.util.TreeMap;

public class _16_3Sum_Closest {
    public int threeSumClosest(int[] nums, int target) {
        int ans=Integer.MAX_VALUE;
        int res=0;
        TreeMap<Integer, Integer>map=new TreeMap<Integer, Integer>();
        for(int i=0;i<nums.length;i++) {
        	map.put(nums[i], map.getOrDefault(nums[i], 0)+1);
        }
        for(int i=0;i<nums.length-1;i++) {
        	map.put(nums[i], map.get(nums[i])-1);
        	for(int j=i+1;j<nums.length;j++) {
        		map.put(nums[j], map.get(nums[j])-1);
        		int sumTwo=nums[i]+nums[j];
        		int residual=target-sumTwo;
        		if (map.ceilingKey(residual)!=null&&map.get(map.ceilingKey(residual))!=0) {
        			int ceil=map.ceilingKey(residual);
        			int differCeil=Math.abs(residual-ceil);
        			if (differCeil==0)
        				return target;
        			else if(differCeil<ans) {
        					ans=differCeil;
        					res=target+differCeil;
        			}
        		}
        		if (map.floorKey(residual)!=null&&map.get(map.floorKey(residual))!=0) {
        			int floor=map.floorKey(residual);
        			int differFloor=Math.abs(residual-floor);
        			if (differFloor==0)
        				return target;
        			else if(differFloor<ans) {
        				ans=differFloor;
        				res=target-differFloor;
        			}
        				
        		}
        		map.put(nums[j], map.get(nums[j])+1);
        	}
        	map.put(nums[i], map.get(nums[i])+1);
        }
        return res;
    }
}
