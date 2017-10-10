import java.util.List;
import java.util.ArrayList;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


public class _257_Binary_Tree_Paths {
	  public List<String> binaryTreePaths(TreeNode root) {
			 List<String> ans=new ArrayList<>();
			 if (root==null)
				 return ans; 
			 StringBuilder sb=new StringBuilder();
			 rec(root,ans,sb);
			 return ans;
		 }

		private void rec(TreeNode root, List<String> ans, StringBuilder sb) {
			// TODO Auto-generated method stub
			if(root.left==null&&root.right==null) {
				sb.append(root.val);
				ans.add(sb.toString());
				return;
			}
			
			sb.append(root.val);
			sb.append("->");
			int len=sb.length();
			
			if(root.left!=null)
				rec(root.left, ans, sb);
			sb.setLength(len);
			if(root.right!=null)
				rec(root.right, ans, sb);
			
		}

}
