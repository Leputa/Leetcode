import java.util.ArrayList;
import java.util.List;

public class _442_Find_All_Duplicates_in_an_Array_ {
	public List<Integer> findDuplicates(int[] nums) {
		List<Integer>list=new ArrayList<>();
		int len=nums.length;
		for (int i=0;i<len;) {
			if(nums[nums[i]-1]!=nums[i]) {
				//System.out.println(nums[i]);
				int tmp1=nums[i];
				int tmp2=nums[nums[i]-1];
				int tag=nums[i]-1;
				nums[i]=tmp2;
				nums[tag]=tmp1;
			}
			else
			  i++;
		}
		for (int i=0;i<len;i++) {
			//System.out.println(nums[i]);
			if(nums[i]!=i+1)
				list.add(nums[i]);	
		}
		return list;
    }
}
