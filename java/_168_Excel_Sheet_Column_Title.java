
public class _168_Excel_Sheet_Column_Title {
	public String convertToTitle(int n) {
		StringBuilder res=new StringBuilder();
		while(n!=0) {
			if(n%26==0) {
				res.append(String.valueOf('Z'));
				n=n/26-1;
			}
			else {
				res.append(String.valueOf((char)(n%26+64)));
				n/=26;
			}
		}
		return res.reverse().toString();
    }
}
