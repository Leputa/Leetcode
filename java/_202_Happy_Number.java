import java.util.ArrayList;
import java.util.HashSet;

public class _202_Happy_Number {
	public boolean isHappy(int n) {
        ArrayList<Integer>list=new ArrayList<>();
        HashSet<Integer>set=new HashSet<>();
        int length=0;
        while(true) {
        	if(n==1)
        		return true;
        	list.clear();
        	set.add(n);
        	while(set.size()==length)
        		return false;
        	while(n!=0) {
                list.add(n%10);
                n/=10;
            }
        	for(int i=0;i<list.size();i++)
        		n+=list.get(i)*list.get(i);	
        	length++;
        }     	
    }
}
