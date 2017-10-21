import java.util.HashMap;
import java.util.List;
import java.util.Set;



public class _554_Brick_Wall {
    public int leastBricks(List<List<Integer>> wall) {
    	int tag=0;
    	HashMap<Integer, Integer>map=new HashMap<>();
    	for(int i=0;i<wall.size();i++) {
    		int sum=0;
    		List<Integer>row=wall.get(i);
    		int blocks=row.size();
    		if(blocks!=1)
    			tag=1;
    		for(int j=0;j<blocks-1;j++) {
    			sum+=row.get(j);
    			map.put(sum,map.getOrDefault(sum, 0)+1);
    		}
    	}
    	if(tag==0)
    		return wall.size();
    	Set<Integer>keys=map.keySet();
    	int max=Integer.MIN_VALUE;
    	for(Integer key:keys) {
    		int tmp=map.get(key);
    		if(tmp>max) 
    			max=tmp;
    	}
    	return wall.size()-max;
    }
}
