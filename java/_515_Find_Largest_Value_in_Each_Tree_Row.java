import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import javax.sound.sampled.LineListener;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class _515_Find_Largest_Value_in_Each_Tree_Row {
	 public List<Integer> largestValues(TreeNode root) {
	     List<Integer>ans=new ArrayList<>();
		 if (root==null)
			 return ans;
	     Queue<TreeNode>queue=new LinkedList<>();
	     TreeNode tmp=root;
	     int curLevelCount=1;
	     int nextLevelCount=0;
	     queue.add(tmp);
	     ans.add(tmp.val);
	     
	     ArrayList<Integer>storage=new ArrayList<>();
	     
	     while(!queue.isEmpty()) {
	    	 tmp=queue.poll();
	    	 curLevelCount--;
	    	 
	    	 if(tmp.left!=null) {
	    		 storage.add(tmp.left.val);
	    		 nextLevelCount++;
	    		 queue.add(tmp.left);
	    	 }
	    	 if(tmp.right!=null) {
	    		 storage.add(tmp.right.val);
	    		 nextLevelCount++;
	    		 queue.add(tmp.right);
	    	 }
	    	 
	    	 if(curLevelCount==0) {
	    		 if(!storage.isEmpty()) {
	    			 ans.add(getMax(storage));
		    		 storage.clear();
	    		 }
	    		 curLevelCount=nextLevelCount;
	    		 nextLevelCount=0;
	    	 }
	     }
	     return ans; 
	 }

	private Integer getMax(ArrayList<Integer> storage) {
		// TODO Auto-generated method stub
		int max=Integer.MIN_VALUE;
		for (int i=0;i<storage.size();i++) {
			if (storage.get(i)>max)
				max=storage.get(i);
		}
		return max;
	}
}
