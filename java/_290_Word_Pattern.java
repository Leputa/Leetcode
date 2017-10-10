import java.util.HashMap;

public class _290_Word_Pattern {
	 public boolean wordPattern(String pattern, String str) {
		 String[] newstr=str.split(" ");
		 if(pattern.length()!=newstr.length)
			 return false;
		 if(pattern.length()==0&&newstr.length==0)
			 return true;
		 HashMap<String,String>map=new HashMap<>();
		 
		 for(int i=0;i<pattern.length();i++) {
			 String tmp=map.getOrDefault(pattern.substring(i, i+1), " ");
			 if(tmp==" ")
				 map.put(pattern.substring(i, i+1), newstr[i]);
			 else {
				 if(!tmp.equals(newstr[i]))
					 return false;
			 }
		 }
		 
		 map.clear();
		 
		 for(int i=0;i<pattern.length();i++) {
			 String tmp=map.getOrDefault(newstr[i], " ");
			 if(tmp==" ")
				 map.put(newstr[i], pattern.substring(i, i+1));
			 else {
				 if(!tmp.equals(pattern.substring(i, i+1)))
					 return false;
			 }
		 }
		 return true;
	 }
}
