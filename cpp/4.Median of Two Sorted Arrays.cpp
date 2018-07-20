# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // &:传引用
		int length1 = nums1.size();
		int length2 = nums2.size();
		if (length1 < length2) return findMedianSortedArrays(nums2, nums1);
		// length1 > length2
		
		int lo = 0, hi = length2 * 2;  //用乘以2来虚拟#号 
		while(lo <= hi){
			int mid2 = (lo + hi) / 2;
			int mid1 = length1 + length2 - mid2;
						
			double L1 = (mid1 == 0) ? INT_MIN : nums1[(mid1-1)/2];
			double L2 = (mid2 == 0) ? INT_MIN : nums2[(mid2-1)/2];
			double R1 = (mid1 == length1 * 2) ? INT_MAX : nums1[(mid1)/2];
			double R2 = (mid2 == length2 * 2) ? INT_MAX : nums2[(mid2)/2];
			
			if (L1 > R2) lo = mid2 + 1;
			else if (L2 > R1) hi = mid2 - 1;
			else return (max(L1, L2) + min(R1, R2))/2;
		}
		return -1;
    }
};


int main(){
	Solution solution = Solution();
	vector<int>nums1 = {1, 3, 5};
	vector<int>nums2 = {2, 4};
	cout << solution.findMedianSortedArrays(nums1, nums2) <<endl;
	
	
}
