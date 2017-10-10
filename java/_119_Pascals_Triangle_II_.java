import java.util.ArrayList;
import java.util.List;

public class _119_Pascals_Triangle_II_ {
	public List<Integer> getRow(int rowIndex) {
		List<Integer>ans=new ArrayList<>();
	    ans.add(1);
	    if(rowIndex==0)
	        return ans;
	    for (int i=2;i<=rowIndex+1;i++) {
	        List<Integer> tmp=new ArrayList<>(ans);
	        ans.clear();
	        for (int j=-1;j<tmp.size();j++) {
	        	if(j==-1)
	        		ans.add(1);
	        	else if (j!=tmp.size()-1)
	        		ans.add(tmp.get(j)+tmp.get(j+1));
	        	else
	        		ans.add(1);
	        }
	    }
	    return ans;   
    }
}
