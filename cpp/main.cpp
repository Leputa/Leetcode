#include <iostream>
#include "4.Median_of_Two_Sorted_Arrays.cpp"

using namespace std;

int main() {
    Solution solution = Solution();
    vector <int> nums1 = {1, 3, 5};
    vector <int> nums2 = {2, 4};
    cout << solution.findMedianSortedArrays(nums1, nums2) <<endl;
}