public class _459_Repeated_Substring_Pattern_ {
	public boolean repeatedSubstringPattern(String s) {
		int len=s.length();
		if(len==0||len==1)
			return false;
		for(int i=len/2;i>=1;i--) {
			if(len%i==0) {
				StringBuilder sb=new StringBuilder();
				for(int j=0;j<len/i;j++)
					sb.append(s.substring(0, i));
				if(sb.toString().equals(s))
					return true;
			}
		}
		return false;
    }
}
