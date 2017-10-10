import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}



public class _107_Binary_Tree_Level_Order_Traversal_II {
	public List<List<Integer>> levelOrderBottom(TreeNode root) {

	    List<List<Integer>> ans = new LinkedList<List<Integer>>();
	    if (root==null)
	    	return ans;
	    Queue<TreeNode> queue=new LinkedList<>();	
	    queue.add(root);
	    while(!queue.isEmpty()) {
	    	List<Integer> list=new ArrayList<>();
	    	int size=queue.size();
	    	for (int i=0;i<size;i++) {
	    		TreeNode tmp=queue.poll();
	    		list.add(tmp.val);
	    		if(tmp.left!=null)
	    			queue.add(tmp.left);
	    		if(tmp.right!=null)
	    			queue.add(tmp.right);
	    	}
	    	ans.add(0,list);
	    }
	    return ans;
	}
}
