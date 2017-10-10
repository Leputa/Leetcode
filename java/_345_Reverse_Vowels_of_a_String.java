
public class _345_Reverse_Vowels_of_a_String {
	public String reverseVowels(String s) {
		StringBuilder ss=new StringBuilder(s);
		s=s.toLowerCase();
		int i=0,j=s.length()-1;
		while(i<j) {
			while ((s.charAt(i)!='a'&&s.charAt(i)!='e'&&s.charAt(i)!='i'&&s.charAt(i)!='o'&&s.charAt(i)!='u')&&(i<j))
				i++;
			while ((s.charAt(j)!='a'&&s.charAt(j)!='e'&&s.charAt(j)!='i'&&s.charAt(j)!='o'&&s.charAt(j)!='u')&&(i<j))
				j--;
			if(i<j) {
				char tmp=ss.charAt(i);
				ss.setCharAt(i, ss.charAt(j));
				ss.setCharAt(j, tmp);
			}
			i++;
			j--;
		}
		s=ss.toString();
		return s;
    }

}
