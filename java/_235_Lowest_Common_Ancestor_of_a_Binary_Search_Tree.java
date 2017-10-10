
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class _235_Lowest_Common_Ancestor_of_a_Binary_Search_Tree {
	public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p==q)
        	return p;
        if(p==null||q==null)
        	return null;
       
        int minval=min(p,q);
        int maxval=max(p,q);
        
        TreeNode tmp=root;
        
        while(tmp!=null) {
        	if(tmp.val>=minval&&tmp.val<=maxval)
            	return tmp;
        	if(tmp.val<minval)
        		tmp=tmp.right;
        	if(tmp.val>maxval)
        		tmp=tmp.left;
        }
        
        return tmp; 
    }

	private int max(TreeNode p, TreeNode q) {
		// TODO Auto-generated method stub
		return p.val>q.val?p.val:q.val;
	}

	public  int min(TreeNode p, TreeNode q) {
		// TODO Auto-generated method stub
		return p.val<=q.val?p.val:q.val;
	}
}
