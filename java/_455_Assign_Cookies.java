import java.util.Arrays;

public class _455_Assign_Cookies {
	public int findContentChildren(int[] g, int[] s) {
		Arrays.sort(g);
		Arrays.sort(s);
		int res=0;
		for (int i=0,j=0;i<s.length&&j<g.length;i++) {
			if(s[i]>=g[j]) {
				res++;
				j++;
			}
		}
		return res;
    }

}
