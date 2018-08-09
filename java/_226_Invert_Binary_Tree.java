import java.util.LinkedList;
import java.util.Queue;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


public class _226_Invert_Binary_Tree {
	// 尝试一下非递归实现
    public TreeNode invertTree(TreeNode root) {
    	if (root == null)
    		return root;
        Queue<TreeNode>queue = new LinkedList<>();
        queue.add(root);
        while(!queue.isEmpty()) {
        	TreeNode tmp = queue.poll();
        	TreeNode leftNode = tmp.left;
        	tmp.left = tmp.right;
        	tmp.right = leftNode;
        	if (tmp.left != null)
        		queue.add(tmp.left);
        	if (tmp.right != null)
        		queue.add(tmp.right);
        }
        return root;
    }	
}
