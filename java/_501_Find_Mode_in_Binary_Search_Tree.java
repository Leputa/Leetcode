import java.util.ArrayList;
import java.util.Stack;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


public class _501_Find_Mode_in_Binary_Search_Tree {
	 public int[] findMode(TreeNode root) {
		 ArrayList<Integer>list=new ArrayList<>();
		 Stack<TreeNode> stack=new Stack<>();
		 TreeNode tmp=root;
		 int max=0;
		 int cnt=0;
		 int tag=Integer.MAX_VALUE;
		 while(tmp!=null||!stack.isEmpty()) {
			 while(tmp!=null) {
				 stack.push(tmp);
				 tmp=tmp.left;
			 }
			 if(!stack.isEmpty()) {
				 tmp=stack.pop();
				 if(tmp.val!=tag) {
					 tag=tmp.val;
					 cnt=1;
				 }
				 else if(tmp.val==tag) {
					 cnt++;
				 }
				 if(cnt==max) {
					 list.add(tmp.val);
				 }
				 else if(cnt>max) {
					 max=cnt;
					 list.clear();
					 list.add(tmp.val);
				 }
				 tmp=tmp.right;
			 }
		 }
		 int []ans=new int[list.size()];
		 for(int i=0;i<list.size();i++)
			 ans[i]=list.get(i);
		 return ans;
	 }
}
