
public class _434_Number_of_Segments_in_a_String {
	 public int countSegments(String s) {
		 if(s.length()==0)
			 return 0;
		 int cnt=0;
		 for(int i=0;i<s.length();i++) {
			 if(s.charAt(i)==' ')
				 continue;
			 cnt++;
			 while(i<s.length()&&s.charAt(i)!=' ')
				 i++;
		 }
		 return cnt;
	 }
}
