class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis_nums = []
        for num in nums:
        	if len(lis_nums) == 0:
        		lis_nums.append(num)
        	elif num > lis_nums[-1]:
        		lis_nums.append(num)
        	else:
        		pos = self.midSearch(lis_nums, num)
        		lis_nums[pos] = num

        return len(lis_nums)


    def midSearch(self, lis_nums, num):
    	low, high = 0, len(lis_nums)-1
    	while(low < high):
    		mid = (low + high) // 2
    		if lis_nums[mid] < num:
    			low = mid + 1
    		elif lis_nums[mid] > num:
    			high = mid - 1
    		else:
    			return mid
    	if num > lis_nums[low]:
    		return low+1
    	else:
    		return low

if __name__ == '__main__': 
	print(Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]))
