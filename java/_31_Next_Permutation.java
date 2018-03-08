import java.util.Arrays;

public class _31_Next_Permutation {
    public void nextPermutation(int[] nums) {
        int len=nums.length;
        if (len==1)
        	return;
        int k=-1;
        for(int i=len-1;i>=1;i--) {
        	if (nums[i-1]<nums[i]) {
        		k=i-1;
        		break;
        	}
        }
        if (k==-1) {
        	reverse(nums);
        	return;
        }
        int l=-1;
        for (int i=len-1;i>k;i--) {
        	if(nums[i]>nums[k]) {
        		l=i;
        		break;
        	}
        }
        swap(nums, k, l);
        Arrays.sort(nums,k+1,len);
        
    }

	private void reverse(int[] nums) {
		// TODO Auto-generated method stub
		int head=0;
		int tail=nums.length-1;
		while(head<tail) {
			swap(nums, head, tail);
			++head;
			--tail;
		}
		
	}

	private void swap(int[] nums, int i, int j) {
		// TODO Auto-generated method stub
		int tmp=nums[i];
		nums[i]=nums[j];
		nums[j]=tmp;
	}
}
