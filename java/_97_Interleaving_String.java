import java.util.ArrayList;
import java.util.List;

public class _97_Interleaving_String {
    public boolean isInterleave(String s1, String s2, String s3) {    	
    	if (s1.length() + s2.length() != s3.length())
    		return false;
    	
        List<List<Boolean>> dp = new ArrayList<List<Boolean>>();
        for (int i=0; i<s1.length()+1; i++) {
        	List<Boolean>row_dp = new ArrayList<>();
        	for (int j=0; j<s2.length()+1; j++) {
        		row_dp.add(true);
        	}
        	dp.add(row_dp);
        }
        
        for (int i=1; i<=s1.length(); i++) {
        	List<Boolean>row_dp = dp.get(i);
        	row_dp.set(0, (dp.get(i-1).get(0)) & (s1.charAt(i-1)==s3.charAt(i-1)));

        }
        
        List<Boolean>row_dp = dp.get(0);
        for (int j=1; j<=s2.length(); j++) {
        	row_dp.set(j, (row_dp.get(j-1)) & (s2.charAt(j-1) == s3.charAt(j-1)));
        }
        
        for (int i=1; i<=s1.length(); i++) {
        	row_dp = dp.get(i);
        	for (int j=1; j<=s2.length(); j++) {
        		row_dp.set(j, ((s1.charAt(i-1)==s3.charAt(i+j-1)) & dp.get(i-1).get(j)) || ((s2.charAt(j-1)==s3.charAt(i+j-1)) & row_dp.get(j-1)));
        	}
        }
        
        System.out.println(dp);
        return dp.get(s1.length()).get(s2.length());
    }
    
    
    public static void main(String[] args) {
		String s1 = new String("aacaac");
		String s2 = new String("aacaaeaac");
		String s3 = new String("aacaaeaaeaacaac");
		
		_97_Interleaving_String solution = new _97_Interleaving_String();
		System.out.println(solution.isInterleave(s1, s2, s3));
	}
}
