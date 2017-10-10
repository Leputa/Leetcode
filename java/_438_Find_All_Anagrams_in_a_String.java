import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

public class _438_Find_All_Anagrams_in_a_String {
	public List<Integer> findAnagrams(String s, String p) {
		int len=p.length();
        List<Integer> list=new ArrayList<Integer>();
		if(s.length()<len)
			return list;
		HashMap<String, Integer>map1=new HashMap<>();
        for(int i=0;i<len;i++) {
        	if(map1.getOrDefault(p.substring(i,i+1),0)==0)
        		map1.put(p.substring(i,i+1), 1);
        	else {
        		map1.put(p.substring(i,i+1), map1.get(p.substring(i,i+1))+1);
        	}
        }
        	

        HashMap<String, Integer>map2=new HashMap<>();
        
        for(int i=0;i<len;i++) {
        	if(map2.getOrDefault(s.substring(i,i+1),0)==0)
        		map2.put(s.substring(i,i+1), 1);
        	else {
        		map2.put(s.substring(i,i+1), map2.get(s.substring(i,i+1))+1);
        	}
        }
        for(int i=0;i<s.length()-len;i++) {
        	if(map1.equals(map2))
        		list.add(i);
        	map2.put(s.substring(i, i+1), map2.get(s.substring(i,i+1))-1);
        	if(map2.get(s.substring(i,i+1))==0)
        		map2.remove(s.substring(i,i+1));
        		
        	if(map2.getOrDefault(s.substring(i+len,i+len+1), 0)==0) {
        		map2.put(s.substring(i+len,i+len+1),1);
        	}
        	else {
        		map2.put(s.substring(i+len,i+len+1),map2.get(s.substring(i+len,i+len+1))+1);
        	}	
        }
        if(map1.equals(map2))
        	list.add(s.length()-len);
        return list;
    }
}
