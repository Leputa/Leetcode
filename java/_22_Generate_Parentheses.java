import java.util.ArrayList;
import java.util.List;

public class _22_Generate_Parentheses {
	private StringBuilder stringBuilder;
	private int i;
	private int j;
    public List<String> generateParenthesis(int n) {
    	List<String>ans=new ArrayList<>();
    	stringBuilder=new StringBuilder();
    	i=0;
    	j=0;
    	addParenthese(ans,n);
    	return ans;
    }

	private void addParenthese(List<String> ans,int n) {
		// TODO Auto-generated method stub
		if (stringBuilder.length()==n*2) {
			ans.add(new String(stringBuilder));
			return;
		}
		if (i<n) {
			++i;
			stringBuilder.append('(');
			addParenthese(ans,n);
			//»ØËİ
			--i;
			stringBuilder.deleteCharAt(stringBuilder.length()-1);
		}
		if (j<i) {
			++j;
			stringBuilder.append(')');
			addParenthese(ans, n);
			//»ØËİ
			--j;
			stringBuilder.deleteCharAt(stringBuilder.length()-1);
		}
	}
}
