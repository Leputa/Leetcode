
public class _58_Length_of_Last_Word {
	 public int lengthOfLastWord(String s) {
		int tag=0;
		for(int i=0;i<s.length();i++) {
			if(s.charAt(i)!=' ') {
				tag=1;
				break;
			}
		}
		if(tag==0)
			return 0;
	    String []ans=s.split(" ");
	    return ans[ans.length-1].length();
	 }
}
