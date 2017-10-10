import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;

public class _451_Sort_Characters_By_Frequency {
	public String frequencySort(String s) {
        TreeMap<String, Integer>map=new TreeMap<>();
        for (int i=0;i<s.length();i++) {
        	map.put(s.substring(i, i+1), map.getOrDefault(s.substring(i, i+1), 0)+1);
        }
        
        List<Map.Entry<String,Integer>>list=new ArrayList<>(map.entrySet());
        Collections.sort(list,new Comparator<Map.Entry<String, Integer>>() {
        	public int compare(Map.Entry<String, Integer> o1,Map.Entry<String, Integer> o2) {
        		return o2.getValue()-o1.getValue();
        	}
        });
   
        StringBuffer ansbuffer=new StringBuffer();
        
        for (Map.Entry<String, Integer>entry:list) {
        	String key=entry.getKey();
        	int value=entry.getValue();
        	for (int i=0;i<value;i++) {
        		ansbuffer.append(key);
        	}
        }
        
        String ans=new String(ansbuffer);
        
        return ans;
    }
}
