import java.util.ArrayList;
import java.util.List;
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
public class _94_Binary_Tree_Inorder_Traversal {
	public List<Integer> inorderTraversal(TreeNode root) {
        TreeNode tmp=root;
        Stack<TreeNode>stack=new Stack<>();
        List<Integer>ans=new ArrayList<>();
        while(tmp!=null || !stack.isEmpty()) {
        	while(tmp!=null) {
        		stack.push(tmp);
        		tmp=tmp.left;
        	}
        	if(!stack.isEmpty()) {
        		tmp=stack.pop();
        		ans.add(tmp.val);
        		tmp=tmp.right;
        	}
        }
        return ans;
    }
}
