import java.util.ArrayList;
import java.util.List;

public class _872_Leaf_Similar_Trees {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
    	if (root1 == null && root2 == null)
    		return true;
    	if (root1 == null)
    		return false;
    	if (root2 == null)
    		return false;
    	
        List<Integer>res1 = new ArrayList<>();
        List<Integer>res2 = new ArrayList<>();
        order(root1, res1);
        order(root2, res2);
        if (res1.size() != res2.size())
        	return false;
        for (int i=0; i<res1.size(); i++)
        	if (res1.get(i) != res2.get(i))
        		return false;
        return true;
        
    }
    private void order(TreeNode root, List<Integer>res){
    	if (root.left == null && root.right == null)
    		res.add(root.val);
    	if (root.left != null)
    		order(root.left, res);
    	if (root.right != null)
    		order(root.right, res);	
    }
}
