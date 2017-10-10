import java.util.ArrayList;
import java.util.List;

public class _118_Pascals_Triangle {
	public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res =new ArrayList<List<Integer>>();
        if(numRows==0)
        	return res;
        List<Integer> temp=new ArrayList<>();
        temp.add(1);
        res.add(temp);
        if(numRows==1)
        	return res;
        for (int i=2;i<=numRows;i++) {
        	List<Integer> tmp1=res.get(i-2);
        	List<Integer> tmp2=new ArrayList<>();
        	for (int j=-1;j<tmp1.size();j++) {
        		if(j==-1)
        			tmp2.add(1);
        		else if (j!=tmp1.size()-1)
        			tmp2.add(tmp1.get(j)+tmp1.get(j+1));
        		else
        			tmp2.add(1);
        	}
        	res.add(tmp2);
        }
        return res;
    }
}
