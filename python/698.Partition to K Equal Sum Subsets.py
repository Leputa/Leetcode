from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    	sum_num = sum(nums)
    	if sum_num % k != 0:
    		return False
    	num = sum_num // k
    	is_used = [False] * len(nums)
    	nums = sorted(nums, reverse=True). # 没有从大到小排序线上能测过，但线下会死循环
    	def trace_back(nums, num, pre_sum, cnt, start):
	    	if cnt == 1:
	    		return True
	    	for i in range(start, len(nums)):
	    		if is_used[i] == False and pre_sum + nums[i] <= num:
	    			is_used[i] = True
	    			if pre_sum + nums[i] == num:
	    				is_true = trace_back(nums, num, 0, cnt-1, 0)
	    			else:
	    				is_true = trace_back(nums, num, pre_sum + nums[i], cnt, i+1)
	    			if is_true:
	    				return True
	    			is_used[i] = False
	    	return False
    	return trace_back(nums, num, 0, k, 0)
    


if __name__ == "__main__":
	print(Solution().canPartitionKSubsets([4,5,3,2,5,5,5,1,5,5,5,5,3,5,5,2], 13))
