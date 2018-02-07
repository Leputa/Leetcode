import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

import javax.naming.spi.DirStateFactory.Result;


public class _399_Evaluate_Division {
	private Map<String, Map<String, Double>> map = new HashMap<>();
	
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
    	Set<String>set=new HashSet<String>();
    	for (int i=0;i<equations.length;i++){
    		set.add(equations[i][0]);
    		set.add(equations[i][1]);
    		Map<String,Double>m;
    		if (map.containsKey(equations[i][0]))
    			m=map.get(equations[i][0]);
    		else
    			m=new HashMap<String,Double>();
    		m.put(equations[i][1], values[i]);
    		map.put(equations[i][0], m);
    		
    		if (map.containsKey(equations[i][1]))
    			m=map.get(equations[i][1]);
    		else
    			m=new HashMap<String,Double>();
    		m.put(equations[i][0], 1.0/values[i]);
    		map.put(equations[i][1], m);
    	}
    	
    	double ans[]=new double[queries.length];
    	for (int i=0;i<queries.length;i++){
    		Iterator<String>it=set.iterator();
    		Map<String, Boolean>visited=new HashMap<String,Boolean>();
    		while(it.hasNext())
    			visited.put(it.next(), false);
    		if (queries[i][0].equals(queries[i][1])&&set.contains(queries[i][0])){
    			ans[i]=1;
    			continue;
    		}
    		double res=dfs(queries[i][0],queries[i][1],1.0,visited);
    		ans[i]=res;
    	}
    	return ans;
        
    }

	private double dfs(String s, String t, double res, Map<String, Boolean> visited) {
		// TODO Auto-generated method stub
		if(map.containsKey(s)&&!visited.get(s)){  //s·Ö×Ó
			visited.put(s, true);
			Map<String, Double>m=map.get(s);
			if (m.containsKey(t)){
				return res*m.get(t);              //t:·ÖÄ¸   map.get(t):s/t
			}
			else{
				Iterator<String>keys=m.keySet().iterator();
				while(keys.hasNext()){
					String key=keys.next();
					double state=dfs(key, t, res*m.get(key), visited);
					if (state!=-1.0)
						return state;
				}
			}
		}
		else
			return -1.0;
		return -1.0;
	}
}



