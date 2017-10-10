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

public class _110_Balanced_Binary_Tree {
	public boolean isBalanced(TreeNode root) {
		if(root==null)
			return true;
		Stack<TreeNode>stack=new Stack<>();
		TreeNode tmp=root;
		while(tmp!=null||!stack.isEmpty()) {
			while(tmp!=null) {
				stack.push(tmp);
				tmp=tmp.left;
			}
			if(!stack.isEmpty()) {
				tmp=stack.pop();
				if(Math.abs(getTreeHeight(tmp.left)-getTreeHeight(tmp.right))>1)
					return false;
				tmp=tmp.right;
			}
		}
		return true;
    }
	public int getTreeHeight(TreeNode root) {
		if (root==null)
			return 0;
		return 1+max(getTreeHeight(root.left),getTreeHeight(root.right));
	}
	private int max(int treeHeight, int treeHeight2) {
		// TODO Auto-generated method stub
		return treeHeight>=treeHeight2?treeHeight:treeHeight2;
	}
}
