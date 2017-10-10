/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class _111_Minimum_Depth_of_Binary_Tree {
	public int minDepth(TreeNode root) {
        if(root==null)
        	return 0;
        if(root.left==null&&root.right==null)
        	return 1;
        else if(root.left==null&&root.right!=null)
        	return 1+minDepth(root.right);
        else if(root.left!=null&&root.right==null)
        	return 1+minDepth(root.left);
        else
        	return 1+min(minDepth(root.left),minDepth(root.right));
    }

	private int min(int a, int b) {
		// TODO Auto-generated method stub
		return a<=b?a:b;
	}
}
