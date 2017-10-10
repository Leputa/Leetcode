import java.util.ArrayList;
import java.util.Iterator;


public class _507_Perfect_Number {
	public boolean checkPerfectNumber(int num) {
        ArrayList<Integer>list=new ArrayList<>();
        for(int i=1;i<=num/2;i++) {
        	if(num%i==0)
        		list.add(i);
        }
        int sum=0;
        Iterator<Integer> it=list.iterator();
        while(it.hasNext()) {
        	sum+=it.next();
        }
        return sum==num;
    }
}
