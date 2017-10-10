
public class _35_Search_Insert_Position {
	public int searchInsert(int[] nums, int target) {
		if (nums.length==0)
			return 0;
        int left=0;
        int right=nums.length-1;
        return searchIndex(nums,target,left,right);
    }

	private int searchIndex(int[] nums, int target, int left, int right) {
		System.out.println(left+":"+right);
		// TODO Auto-generated method stub
		int mid=(left+right)/2;
		System.out.println(nums[mid]+":"+target);
		if (nums[mid]==target)
			return mid;
		
		else if(nums[mid]>target&&right==left)
			return mid;
		else if(nums[mid]>target&&right-left==1)
			return left;
		else if(nums[mid]<target&&right==left)
			return mid+1;
		else if(nums[mid]<target&&right-left==1)
            if(target>nums[right])
			    return right+1;
            else
                return right;
		else if (nums[mid]>target)
			return searchIndex(nums, target, left, mid-1);
		else 
			return searchIndex(nums, target, mid+1, right);	
	}

}
