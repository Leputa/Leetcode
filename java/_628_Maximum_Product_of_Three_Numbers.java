
public class _628_Maximum_Product_of_Three_Numbers {
	 public int maximumProduct(int[] nums) {
		 int tag1=0,tag2=0;
		 int max1=-1000,max2=-1000,max3=-1000;
		 int min1=1000,min2=1000;
		 int mtag=0;
		 for (int i=0;i<nums.length;i++) {
			 if (nums[i]>=max1) {
				 max1=nums[i];
				 tag1=i;
			 }
			 if(nums[i]<=min1) {
				 min1=nums[i];
				 mtag=i;
			 }
		 }
		 for(int i=0;i<nums.length;i++) {
			 if (nums[i]>=max2&&i!=tag1) {
				 max2=nums[i];
				 tag2=i;
			 }
			 if(nums[i]<=min2&&i!=mtag) {
				 min2=nums[i];
			 }
		 }
		 for(int i=0;i<nums.length;i++) {
			 if (nums[i]>=max3&&i!=tag1&&i!=tag2) 
				 max3=nums[i]; 
		 }
		 return max1*max2*max3>min1*min2*max1?max1*max2*max3:min1*min2*max1;    
	 }
}
