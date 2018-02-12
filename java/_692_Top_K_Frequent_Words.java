import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class _692_Top_K_Frequent_Words {
    public List<String> topKFrequent(String[] words, int k) {
        Map <String,Integer>map=new HashMap<>();
        for(int i=0;i<words.length;i++){
        	map.put(words[i], map.getOrDefault(words[i],0)+1);
        }
        List<Map.Entry<String, Integer>>sortMap=new ArrayList<>();
        for (Map.Entry<String, Integer>entry:map.entrySet())
        	sortMap.add(entry);
        
        sortMap.sort(new Comparator<Map.Entry<String, Integer>>() {
        	public int compare(Map.Entry<String, Integer>o1,Map.Entry<String, Integer>o2){
        		if (o2.getValue()!=o1.getValue())
        			return o2.getValue()-o1.getValue();
        		else
        			return o1.getKey().compareTo(o2.getKey());
        	}
		});
        List<String>ans=new ArrayList<>();
        for(int i=0;i<k;i++){
        	ans.add(sortMap.get(i).getKey());
        }
        return ans;  
    }
    public static void main(String[] args) {
    	_692_Top_K_Frequent_Words test=new _692_Top_K_Frequent_Words();
    	String[]string={"bb","aa","bb"};
    	System.out.println(test.topKFrequent(string, 1)); 
	}
}
