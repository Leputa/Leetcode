import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class _47_Permutations_II {
    public List<List<Integer>> permuteUnique(int[] nums) {
    	Arrays.sort(nums);
        List <List<Integer>> res = new ArrayList<>();
        List<Integer> tmpList = new ArrayList<>();
        Boolean[] tag = new Boolean[nums.length];
        for (int i=0; i<tag.length; i++)
        	tag[i] = false;
        traceback(nums, tag, res, tmpList);
        return res;
    }

	private void traceback(int[] nums, Boolean[] tag, List<List<Integer>> res, List<Integer> tmpList) {
		// TODO Auto-generated method stub
		if (tmpList.size() == nums.length) {
			res.add((List<Integer>) ((ArrayList<Integer>) tmpList).clone());
			return;
		}
		
		for (int i=0; i<nums.length; i++) {
			if (i!=0 && nums[i] == nums[i-1])
				continue;
			if (tag[i] == false) {
				tag[i] = true;
				tmpList.add(nums[i]);
				traceback(nums, tag, res, tmpList);
				tmpList.remove(tmpList.size()-1);
				tag[i] = false;
			}
		}
	}
}
