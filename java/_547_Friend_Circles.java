public class _547_Friend_Circles {
	private int[]id;
    
	public int findCircleNum(int[][] M) {
    	int count=M.length;
    	id =new int[count];
    	for (int i=0;i<count;i++)
    		id[i]=i;
    	
    	for(int i=0;i<M.length;i++) {
    		for(int j=i;j<M.length;j++) {
    			if(M[i][j]==1) {
    				//System.out.println(i+"   "+j);
    				if(union(i, j)==1)
    					count--;
    			}
    		}
    	}
    	
    	return count;
    }
    
    private int find(int p) {
    	while(p!=id[p]) //寻找根节点
    		p=id[p];
    	return p;
    }
    
    private int union(int p,int q) {
    	int pRoot=find(p);
    	int qRoot=find(q);
    	//System.out.println(pRoot+"   "+qRoot+"hahaha");
    	if(pRoot==qRoot)
    		return 0;
    	id[pRoot]=qRoot;
    	return 1;
    }
    
    /*//路径压缩版本
    private int find(int p,int[]id) {
    	while(p!=id[p])
    		id[p]=find(id[p], id);
    	return id[p];
    }*/
}
