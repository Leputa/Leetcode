import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class _447_Number_of_Boomerangs {
	public int numberOfBoomerangs(int[][] points) {
		int ans=0;
		if(points.length<3)
			return ans;
		HashMap<Integer, Integer>map=new HashMap<Integer,Integer>();
		for (int i=0;i<points.length;i++) {
			for(int j=0;j<points.length;j++) {
				if(i==j)
					continue;
				int d=getDistance(points[i], points[j]);
				map.put(d, map.getOrDefault(d, 0)+1);  //dict.get() in python
			}
			Set<Integer>keys=map.keySet();
			Iterator<Integer>it=keys.iterator();
			while(it.hasNext()) {
				int tmp=it.next(); 
				ans+=map.get(tmp)*(map.get(tmp)-1);//C(2 N)*2/2
			}
			map.clear();
		}
        return ans;
    }
	private int getDistance(int []a,int []b) {
		return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]);
	}
}

