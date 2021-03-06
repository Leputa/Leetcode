
public class _96_Unique_Binary_Search_Trees {
    public int numTrees(int n) {
        if (n==1 || n==0)
        	return 1;
        int []count=new int[n+1];
        count[0]=1;
        count[1]=1;
        for (int i=2;i<=n;i++){
        	for(int j=0;j<i;j++){
        		count[i]+=count[j]*count[i-j-1];
        	}
        }
        return count[n];
    }
}
