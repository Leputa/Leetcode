
public class _171_Excel_Sheet_Column_Number {
	public int titleToNumber(String s) {
        int len=s.length();
        int res=0;
        int j=len-1;
        for (int i=0;i<len;i++) {
        	res+=((int)(s.charAt(i))-64)*Math.pow(26, j);
        	j--;
        }
        return res;
    }

}
