import java.util.ArrayList;

public class _9_Palindrome_Number_ {
	public boolean isPalindrome(int x) {
		if(x<0)
			return false;
		if(x<10)
			return true;
		ArrayList<Integer>list=new ArrayList<>();
		while(x!=0) {
			list.add(x%10);
			x/=10;
		}
		int i=0,j=list.size()-1;
		while(i<=j) {
			if(list.get(i)!=list.get(j))
				return false;
			i++;
			j--;
		}
		return true;
    }
}
