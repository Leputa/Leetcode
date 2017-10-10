import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class _409_Longest_Palindrome {
	 public int longestPalindrome(String s) {
	        HashMap <String,Integer> hashMap=new HashMap<String, Integer>();
	        
	        if (s.length()==0)
	        	return 0;
	        if (s.length()==1)
	        	return 1;
  
	        for (int i=0;i<s.length();i++) {
	        	if (hashMap.get(s.substring(i, i+1))==null)
	        		hashMap.put(s.substring(i, i+1), 1);
	        	else {
					hashMap.put(s.substring(i, i+1), hashMap.get(s.substring(i, i+1))+1);
				}
	        }
	        int cnt=0;
	        int tag=0;
	        
	        Set <String> keys=hashMap.keySet();
	        Iterator <String> it=keys.iterator();
	        
	        while(it.hasNext()) {
	        	int tmp=hashMap.get(it.next());
	        	if(tmp%2==0)
	        		cnt+=tmp;
	        	else if(tmp%2==1) {
	        		tag=1;
	        		cnt+=tmp-1;
	        	}
	        }
	        
	        if (tag==1)
	        	cnt++;

	        return cnt;
	        
	    }
}
