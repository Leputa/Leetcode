
public class _338_Counting_Bits {
	public int[] countBits(int num) {
        int[]ans=new int[num+1];
        ans[0]=0;
        for (int i=1;i<=num;i++) 
        	ans[i]=ans[i>>1]+i%2;  
        return ans;
    }
}
