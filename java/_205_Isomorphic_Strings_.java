import java.util.HashMap;

public class _205_Isomorphic_Strings_ {
	public boolean isIsomorphic(String s, String t) {
		if(s.length()!=t.length())
			return false;
		HashMap<String, String>map=new HashMap<>();
		for(int i=0;i<s.length();i++) {
			if(map.get(s.substring(i,i+1))!=null) {
				if(!map.get(s.substring(i,i+1)).equals(t.substring(i,i+1)))
					return false;
			}
			map.put(s.substring(i, i+1), t.substring(i, i+1));
		}
		map.clear();
		for(int i=0;i<s.length();i++) {
			if(map.get(t.substring(i,i+1))!=null) {
				if(!map.get(t.substring(i,i+1)).equals(s.substring(i,i+1)))
					return false;
			}
			map.put(t.substring(i, i+1), s.substring(i, i+1));
		}
		return true;
    }
}
