

/*class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}*/


public class _437_Path_Sum_III {
	public int pathSum(TreeNode root, int sum) {
		if(root==null)
			return 0;
		
		return dfs(root,sum)+pathSum(root.left,sum)+pathSum(root.right,sum);
    }

	private int dfs(TreeNode root, int sum) {
		// TODO Auto-generated method stub
		int ans=0;
		if(root==null)
			return ans;
		if(sum==root.val)
			ans++;
		ans+=dfs(root.left, sum-root.val);
		ans+=dfs(root.right,sum-root.val);
		return ans;
	}
}
