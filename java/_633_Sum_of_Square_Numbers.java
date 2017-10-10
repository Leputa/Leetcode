
public class _633_Sum_of_Square_Numbers {
	 public boolean judgeSquareSum(int c) {
		 int high=(int)Math.ceil(Math.sqrt(c));
		 int low=0;
		 while(low<=high) {
			 if(low*low+high*high==c)
				 return true;
			 else if(low*low+high*high<c)
				 low++;
			 else 
				 high--;
		 }
		 return false;  
	 }
}
