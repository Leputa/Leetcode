class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        zero_index = []
        tmp_zero = []
        for i in range(0, len(nums)-1):
            if nums[i] == 0:
                tmp_zero.append(i)
                if i == len(nums)-2:
                    zero_index.append(i)
                elif nums[i+1] == 0:
                    continue
                else:
                    zero_index.append(i)

        for i in range(len(zero_index)):
            pos = zero_index[i]

            if i == 0:
                pre_pos = -1
            else:
                pre_pos = zero_index[i-1]

            tag = False
            for i in range(pos-1, -1, -1):
                if nums[i] > pos - i:
                    tag = True
            if tag == False:
                return tag

        return True


if __name__ == '__main__':
    print(Solution().canJump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))

